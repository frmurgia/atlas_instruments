<template>
  <section class="section-orange">
    <div class="specs-wrapper">
      <h2 ref="titleEl" class="section-title proto-mono" :style="titleStyle">FEATURES &amp; SPECS</h2>
      <div class="specs-list">
        <template v-for="(spec, i) in specs" :key="i">
          <div
            v-if="i === specsStartIndex"
            class="sub-header proto-mono"
          >SPECIFICATIONS</div>
          <div
            :ref="el => setSpecRef(el, i)"
            class="spec-item proto-mono"
            :style="specStyles[i]"
          >
            <span class="spec-label">{{ spec.label }}</span>
            <span class="spec-value" v-html="spec.value"></span>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue'
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const specs = [
  { label: '10-track playback', value: 'Independent volume per track', section: 'features' },
  { label: '2 MIDI outputs', value: 'Sync your entire modular setup', section: 'features' },
  { label: 'No screen', value: 'Physical-only, muscle memory operation', section: 'features' },
  { label: 'LED meters', value: 'Real-time visual feedback per track', section: 'features' },
  { label: '100 track slots', value: '10 banks × 10 tracks', section: 'features' },
  { label: 'Sync cascade', value: 'Connect multiple units for 20+ tracks', section: 'features' },
  { label: 'Web interface', value: 'Load WAV files from any browser', section: 'features' },
  { label: 'Max for Live', value: 'Manage tracks directly from Ableton', section: 'features' },
  { label: 'Embedded Linux', value: 'Updatable firmware via USB', section: 'features' },
  { label: 'Bio-based case', value: 'Nylon PA 11, printed in Sardinia', section: 'features' },
  { label: 'Type', value: 'Audio track player', section: 'specs' },
  { label: 'Audio tracks', value: '10 independent', section: 'specs' },
  { label: 'Audio output', value: '1 stereo (PCM5102A 32-bit DAC)', section: 'specs' },
  { label: 'MIDI outputs', value: '2 × 5-pin DIN', section: 'specs' },
  { label: 'Sync', value: 'Proprietary Sync Out/In (3.3V) for cascading multiple units', section: 'specs' },
  { label: 'Storage', value: '8 GB eMMC — over 14 min per track across all 100 slots', section: 'specs' },
  { label: 'Banks', value: '10 banks × 10 tracks = 100 tracks total', section: 'specs' },
  { label: 'Controls', value: '10 × 75mm linear faders, 1 rotary encoder,<br>1 toggle switch, 1 rear button', section: 'specs' },
  { label: 'Feedback', value: '10 × RGB LED meters (WS2812B)', section: 'specs' },
  { label: 'Track loading', value: 'Embedded web interface (any browser)<br>or Max for Live plugin', section: 'specs' },
  { label: 'Connectivity', value: 'USB Type-C (power + data)', section: 'specs' },
  { label: 'Power', value: 'USB-C 5V', section: 'specs' },
  { label: 'Case', value: 'SLS Nylon PA 11 (bio-based)', section: 'specs' },
  { label: 'Designed and assembled', value: 'Sardinia, Italy', section: 'specs' }
]

const specsStartIndex = computed(() => specs.findIndex(s => s.section === 'specs'))

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

.sub-header {
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 900;
  letter-spacing: -0.02em;
  padding-top: 4rem;
  padding-bottom: 1rem;
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
