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
  { label: 'Type', value: 'Audio track player' },
  { label: 'Audio tracks', value: '10 independent' },
  { label: 'Audio output', value: '1 stereo (PCM5102A 32-bit DAC)' },
  { label: 'MIDI outputs', value: '2 × 5-pin DIN' },
  { label: 'Sync', value: 'Proprietary Sync Out/In (3.3V) for cascading multiple units' },
  { label: 'Storage', value: '8 GB eMMC — over 14 min per track across all 100 slots' },
  { label: 'Banks', value: '10 banks × 10 tracks = 100 tracks total' },
  { label: 'Controls', value: '10 × 75mm linear faders, 1 rotary encoder,<br>1 toggle switch, 1 rear button' },
  { label: 'Feedback', value: '10 × RGB LED meters (WS2812B)' },
  { label: 'Track loading', value: 'Embedded web interface (any browser)<br>or Max for Live plugin' },
  { label: 'Connectivity', value: 'USB Type-C (power + data)' },
  { label: 'Power', value: 'USB-C 5V' },
  { label: 'Case', value: 'SLS Nylon PA 11 (bio-based)' },
  { label: 'Designed and assembled', value: 'Sardinia, Italy' }
]

const { el: titleEl, style: titleStyle } = useScrollAnimation({
  rotateXRange: [-2, 0, 1],
  rotateYRange: [2, 0, -1],
  scaleRange: [0.97, 1, 0.99],
  translateZRange: [-15, 0, -5],
  easing: 0.06
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
const targets = specs.map(() => ({ x: 20, opacity: 0 }))

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
      targets[i].x = 20 + i * 4
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
