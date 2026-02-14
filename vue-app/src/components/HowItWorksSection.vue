<template>
  <section class="how-section">
    <div class="how-wrapper">
      <h2 ref="titleEl" class="section-title proto-mono" :style="titleStyle">HOW IT WORKS</h2>
      <div class="how-body">
        <p>At home, load WAV files via the web interface or the Max for Live plugin. Assign tracks to banks — done.</p>
        <p>On stage, flip the switch. Ten faders, ten LED meters, zero screens. Everything plays in sync.</p>
        <p>Need more? Chain multiple TenLoopers via the Sync port. 20, 30, 40+ tracks — zero computers.</p>
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
.how-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 3rem;
  overflow: hidden;
}

.how-wrapper {
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

.how-body {
  max-width: 800px;
}

.how-body p {
  font-size: 1.15rem;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.how-body p:last-child {
  margin-bottom: 0;
}

@media (max-width: 768px) {
  .how-section {
    padding: 4rem 1.5rem;
  }
}
</style>
