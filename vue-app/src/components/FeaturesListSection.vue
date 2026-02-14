<template>
  <section class="section-orange">
    <div class="features-wrapper">
      <h2 ref="titleEl" class="section-title proto-mono" :style="titleStyle">FEATURES</h2>
      <div class="specs-list">
        <div
          v-for="(feat, i) in features"
          :key="i"
          :ref="el => setFeatRef(el, i)"
          class="spec-item proto-mono"
          :style="featStyles[i]"
        >
          <span class="spec-label">{{ feat.label }}</span>
          <span class="spec-value">{{ feat.value }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const features = [
  { label: '10-track looping', value: 'Independent overdub & sync' },
  { label: '3 MIDI outputs', value: 'Control modular synths' },
  { label: 'No screen design', value: 'Physical interface only' },
  { label: 'LED VU meters', value: 'Real-time monitoring' },
  { label: 'Embedded Linux', value: 'Updatable via USB' },
  { label: 'Web interface', value: 'Upload WAV files' },
  { label: 'Mixer integration', value: 'Dedicated audio outs' },
  { label: 'Live performance', value: 'Zero latency' }
]

const { el: titleEl, style: titleStyle } = useScrollAnimation({
  rotateXRange: [-2, 0, 1],
  rotateYRange: [2, 0, -1],
  scaleRange: [0.97, 1, 0.99],
  translateZRange: [-15, 0, -5],
  easing: 0.06
})

const featRefs = ref([])
const featStyles = reactive(Array(features.length).fill(null).map(() => ({
  transform: '',
  opacity: 0
})))

let raf = null

function setFeatRef(el, i) {
  if (el) featRefs.value[i] = el
}

function lerp(a, b, t) {
  return a + (b - a) * t
}

const currents = features.map(() => ({ x: 0, opacity: 0 }))
const targets = features.map(() => ({ x: 20, opacity: 0 }))

function animate() {
  featRefs.value.forEach((el, i) => {
    if (!el) return
    const rect = el.getBoundingClientRect()
    const wh = window.innerHeight

    const progress = 1 - (rect.top / wh)

    if (progress > 0.1) {
      targets[i].x = 0
      targets[i].opacity = 1
    } else {
      targets[i].x = 20 + i * 4
      targets[i].opacity = 0
    }

    currents[i].x = lerp(currents[i].x, targets[i].x, 0.08)
    currents[i].opacity = lerp(currents[i].opacity, targets[i].opacity, 0.08)

    featStyles[i] = {
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

.features-wrapper {
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
