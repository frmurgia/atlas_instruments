<template>
  <section class="cta-section" id="mailing">
    <div ref="el" class="cta-inner" :style="style">
      <h2 class="cta-title proto-mono">
        <span>SIGN UP</span> TO THE MAILING LIST TO STAY IN TUNE WITH THE LAST UPDATES
      </h2>
    </div>
  </section>
</template>

<script setup>
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const { el, style } = useScrollAnimation({
  rotateXRange: [-6, 0, 4],
  rotateYRange: [12, 0, -6],
  scaleRange: [0.8, 1, 0.95],
  translateZRange: [-100, 0, -30],
  easing: 0.07
})
</script>

<style scoped>
.cta-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3rem;
  background: var(--white);
  overflow: hidden;
}

.cta-inner {
  max-width: 1200px;
  text-align: left;
  will-change: transform;
}

.cta-title {
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -0.02em;
  max-width: 900px;
  margin-bottom: 2rem;
}

.cta-title span {
  color: var(--orange);
}

@media (max-width: 768px) {
  .cta-section {
    padding: 0 1.5rem;
  }
}
</style>
