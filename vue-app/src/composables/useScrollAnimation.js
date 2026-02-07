import { ref, onMounted, onUnmounted } from 'vue'

export function useScrollAnimation(options = {}) {
  const {
    rotateXRange = [-15, 0, 10],
    rotateYRange = [20, 0, -20],
    scaleRange = [0.7, 1, 0.85],
    translateZRange = [-200, 0, -100],
    easing = 0.08
  } = options

  const el = ref(null)
  const style = ref({
    transform: '',
    opacity: 0
  })

  let raf = null
  let current = { rotateX: 0, rotateY: 0, scale: 0.7, translateZ: -200, opacity: 0 }
  let target = { ...current }

  function lerp(a, b, t) {
    return a + (b - a) * t
  }

  function mapRange(value, inMin, inMax, outArray) {
    const t = Math.max(0, Math.min(1, (value - inMin) / (inMax - inMin)))
    if (t <= 0.5) {
      const localT = t / 0.5
      return lerp(outArray[0], outArray[1], localT)
    } else {
      const localT = (t - 0.5) / 0.5
      return lerp(outArray[1], outArray[2], localT)
    }
  }

  function update() {
    if (!el.value) {
      raf = requestAnimationFrame(update)
      return
    }

    const rect = el.value.getBoundingClientRect()
    const windowH = window.innerHeight
    const elementCenter = rect.top + rect.height / 2
    const progress = 1 - (elementCenter / windowH)

    target.rotateX = mapRange(progress, -0.5, 1.5, rotateXRange)
    target.rotateY = mapRange(progress, -0.5, 1.5, rotateYRange)
    target.scale = mapRange(progress, -0.5, 1.5, scaleRange)
    target.translateZ = mapRange(progress, -0.5, 1.5, translateZRange)
    target.opacity = Math.max(0, Math.min(1, mapRange(progress, -0.3, 1.3, [0, 1, 0.3])))

    current.rotateX = lerp(current.rotateX, target.rotateX, easing)
    current.rotateY = lerp(current.rotateY, target.rotateY, easing)
    current.scale = lerp(current.scale, target.scale, easing)
    current.translateZ = lerp(current.translateZ, target.translateZ, easing)
    current.opacity = lerp(current.opacity, target.opacity, easing)

    style.value = {
      transform: `perspective(1200px) rotateX(${current.rotateX.toFixed(2)}deg) rotateY(${current.rotateY.toFixed(2)}deg) scale(${current.scale.toFixed(4)}) translateZ(${current.translateZ.toFixed(1)}px)`,
      opacity: current.opacity.toFixed(3)
    }

    raf = requestAnimationFrame(update)
  }

  onMounted(() => {
    raf = requestAnimationFrame(update)
  })

  onUnmounted(() => {
    if (raf) cancelAnimationFrame(raf)
  })

  return { el, style }
}

export function useScrollProgress() {
  const scrollY = ref(0)
  const scrollProgress = ref(0)

  function onScroll() {
    scrollY.value = window.scrollY
    const docH = document.documentElement.scrollHeight - window.innerHeight
    scrollProgress.value = docH > 0 ? window.scrollY / docH : 0
  }

  onMounted(() => {
    window.addEventListener('scroll', onScroll, { passive: true })
    onScroll()
  })

  onUnmounted(() => {
    window.removeEventListener('scroll', onScroll)
  })

  return { scrollY, scrollProgress }
}
