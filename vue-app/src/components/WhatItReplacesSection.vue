<template>
  <section class="replaces-section">
    <div class="replaces-wrapper">
      <h2 ref="titleEl" class="section-title proto-mono" :style="titleStyle">WHAT IT REPLACES</h2>
      <div class="replaces-body">
        <p>You're using a €2,000 laptop, a €750 Ableton Live license and an external audio interface just to play back loops and send MIDI clock. TenLooper does that one job — and only that job — in a dedicated box that doesn't crash, doesn't need updates and doesn't need you to look at it.</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const { el: titleEl, style: titleStyle } = useScrollAnimation({
  rotateXRange: [-2, 0, 1],
  rotateYRange: [2, 0, -1],
  scaleRange: [0.97, 1, 0.99],
  translateZRange: [-15, 0, -5],
  easing: 0.06
})
</script>

<style scoped>
.replaces-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 3rem;
  overflow: hidden;
}

.replaces-wrapper {
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

.replaces-body {
  max-width: 800px;
}

.replaces-body p {
  font-size: 1.15rem;
  line-height: 1.7;
}

@media (max-width: 768px) {
  .replaces-section {
    padding: 4rem 1.5rem;
  }
}
</style>
