<template>
  <section class="section-orange">
    <div ref="el" class="device-outline" :style="style">
      <svg viewBox="0 0 1200 400" fill="none" stroke="white" stroke-width="2">
        <rect x="50" y="50" width="1100" height="300" rx="8"/>
        <rect x="100" y="100" width="100" height="200" rx="4"/>
        <rect x="220" y="100" width="100" height="200" rx="4"/>
        <rect x="340" y="100" width="100" height="200" rx="4"/>
        <rect x="460" y="100" width="100" height="200" rx="4"/>
        <rect x="580" y="100" width="100" height="200" rx="4"/>
        <rect x="700" y="100" width="100" height="200" rx="4"/>
        <rect x="820" y="100" width="100" height="200" rx="4"/>
        <rect x="940" y="100" width="100" height="200" rx="4"/>
        <rect x="100" y="120" width="940" height="3"/>
        <circle cx="120" cy="110" r="3"/>
        <circle cx="240" cy="110" r="3"/>
        <circle cx="360" cy="110" r="3"/>
        <circle cx="480" cy="110" r="3"/>
        <circle cx="600" cy="110" r="3"/>
        <circle cx="720" cy="110" r="3"/>
        <circle cx="840" cy="110" r="3"/>
        <circle cx="960" cy="110" r="3"/>
        <circle cx="1080" cy="110" r="3"/>
        <circle cx="1100" cy="110" r="3"/>
      </svg>
    </div>
  </section>
</template>

<script setup>
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const { el, style } = useScrollAnimation({
  rotateXRange: [-20, 0, 15],
  rotateYRange: [30, 0, -25],
  scaleRange: [0.5, 1, 0.7],
  translateZRange: [-300, 0, -150],
  easing: 0.06
})
</script>

<style scoped>
.section-orange {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3rem;
  background: var(--orange);
  color: var(--white);
  overflow: hidden;
}

.device-outline {
  max-width: 1200px;
  width: 100%;
  padding: 4rem;
  will-change: transform;
  transform-style: preserve-3d;
}

.device-outline svg {
  width: 100%;
  height: auto;
  filter: drop-shadow(0 0 30px rgba(255,255,255,0.15));
}

@media (max-width: 768px) {
  .section-orange {
    padding: 0 1.5rem;
  }
  .device-outline {
    padding: 2rem;
  }
}
</style>
