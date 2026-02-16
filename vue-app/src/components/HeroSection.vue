<template>
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-top">
        <div class="hero-left">
        
          <h1 ref="el" class="hero-title proto-mono" :style="style">
            TENLOOPER
          </h1>
        </div>
        <div ref="modelEl" class="model-number proto-mono" :style="modelStyle">TL-01</div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const { el, style } = useScrollAnimation({
  rotateXRange: [0, 0, 2],
  rotateYRange: [0, 0, -1],
  scaleRange: [1, 1, 0.98],
  translateZRange: [0, 0, -15],
  easing: 0.05
})

const { el: modelEl, style: modelStyle } = useScrollAnimation({
  rotateXRange: [0, 0, 3],
  rotateYRange: [0, 0, 2],
  scaleRange: [1, 1, 0.97],
  translateZRange: [0, 0, -20],
  easing: 0.04
})
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3rem;
  padding-top: 5rem;
}

.hero-inner {
  max-width: 1400px;
  width: 100%;
}

.hero-top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.hero-tagline {
  font-size: 1rem;
  margin-bottom: 1.5rem;
  letter-spacing: 0.1em;
}

.hero-title {
  font-size: clamp(5rem, 15vw, 12rem);
  font-weight: 900;
  line-height: 0.9;
  letter-spacing: -0.02em;
  margin-bottom: 1rem;
  will-change: transform;
}

.model-number {
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 700;
  text-align: right;
  will-change: transform;
}

@media (max-width: 768px) {
  .hero {
    padding: 0 1.5rem;
    padding-top: 5rem;
  }

  .hero-top {
    flex-direction: column;
    gap: 1rem;
  }

  .hero-title {
    font-size: clamp(2.5rem, 12vw, 5rem);
    word-break: break-word;
  }

  .model-number {
    text-align: left;
  }
}
</style>
