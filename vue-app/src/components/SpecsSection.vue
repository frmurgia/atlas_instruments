<template>
  <section class="section-orange">
    <div class="specs-wrapper">
      <h2 ref="titleEl" class="section-title proto-mono" :style="titleStyle">SPECIFICATIONS</h2>
      <div class="specs-list">
        <div
          v-for="(spec, i) in specs"
          :key="i"
          :ref="el => setSpecRef(el, i)"
          class="spec-item proto-mono"
          :style="specStyles[i]"
        >
          <span class="spec-label">{{ spec.label }}</span>
          <span class="spec-value" v-html="spec.value"></span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const specs = [
  { label: 'Type of device', value: 'Audio Looper' },
  { label: 'Audio tracks', value: '10 Independent' },
  { label: 'MIDI outputs', value: '3 x 5-pin DIN' },
  { label: 'Audio quality', value: '24-bit / 48kHz' },
  { label: 'DAC', value: 'PCM5102A Professional' },
  { label: 'Processor', value: 'RK3506G ARM Cortex-A7' },
  { label: 'Inputs', value: '10 Faders 75mm<br>1 Rotary encoder<br>1 Toggle switch' },
  { label: 'Outputs', value: '10 LED VU meters WS2812B RGB' },
  { label: 'Connectivity', value: 'USB Type-C<br>Ethernet gadget' },
  { label: 'Power', value: 'USB-C 5V' }
]

const { el: titleEl, style: titleStyle } = useScrollAnimation({
  rotateXRange: [-10, 0, 5],
  rotateYRange: [15, 0, -10],
  scaleRange: [0.6, 1, 0.95],
  translateZRange: [-200, 0, -50],
  easing: 0.07
})

// Per-row staggered animations
const specRefs = ref([])
const specStyles = reactive(Array(specs.length).fill(null).map(() => ({
  transform: '',
  opacity: 0
})))

let raf = null

function setSpecRef(el, i) {
  if (el) specRefs.value[i] = el
}

function lerp(a, b, t) {
  return a + (b - a) * t
}

const currents = specs.map(() => ({ x: 0, opacity: 0 }))
const targets = specs.map(() => ({ x: 60, opacity: 0 }))

function animate() {
  specRefs.value.forEach((el, i) => {
    if (!el) return
    const rect = el.getBoundingClientRect()
    const wh = window.innerHeight
    const progress = 1 - (rect.top / wh)

    if (progress > 0.1) {
      targets[i].x = 0
      targets[i].opacity = 1
    } else {
      targets[i].x = 60 + i * 10
      targets[i].opacity = 0
    }

    currents[i].x = lerp(currents[i].x, targets[i].x, 0.08)
    currents[i].opacity = lerp(currents[i].opacity, targets[i].opacity, 0.08)

    specStyles[i] = {
      transform: `translateX(${currents[i].x.toFixed(1)}px)`,
      opacity: currents[i].opacity.toFixed(3)
    }
  })

  raf = requestAnimationFrame(animate)
}

onMounted(() => {
  raf = requestAnimationFrame(animate)
})

onUnmounted(() => {
  if (raf) cancelAnimationFrame(raf)
})
</script>

<style scoped>
.section-orange {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4rem 3rem;
  background: var(--yellow);
  color: var(--black);
  overflow: hidden;
}

.specs-wrapper {
  width: 100%;
  max-width: 1400px;
}

.section-title {
  font-size: clamp(4rem, 10vw, 8rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: -0.02em;
  margin-bottom: 3rem;
  will-change: transform;
}

.specs-list {
  width: 100%;
}

.spec-item {
  display: flex;
  justify-content: space-between;
  padding: 2rem 0;
  border-bottom: 1px solid rgba(0,0,0,0.15);
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  will-change: transform, opacity;
}

.spec-label {
  font-weight: 400;
}

.spec-value {
  font-weight: 700;
  text-align: right;
}

@media (max-width: 768px) {
  .section-orange {
    padding: 4rem 1.5rem;
  }
}
</style>
