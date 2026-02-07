<template>
  <section class="feature-section">
    <div ref="el" class="features-split" :class="{ 'image-right': !imageLeft }" :style="style">
      <div v-if="imageLeft" class="feature-image-wrapper">
        <div class="feature-image-placeholder">
          [{{ placeholder }}]
        </div>
      </div>
      <div class="feature-text">
        <h2 class="feature-title proto-mono">
          <span>{{ titleNumber }}</span><br>{{ titleText }}
        </h2>
        <p class="feature-description">{{ description }}</p>
        <div class="feature-label proto-mono">{{ label }}</div>
      </div>
      <div v-if="!imageLeft" class="feature-image-wrapper">
        <div class="feature-image-placeholder">
          [{{ placeholder }}]
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const props = defineProps({
  titleNumber: String,
  titleText: String,
  description: String,
  label: String,
  placeholder: String,
  imageLeft: { type: Boolean, default: true },
  animateConfig: { type: Object, default: () => ({}) }
})

const { el, style } = useScrollAnimation({
  rotateXRange: props.animateConfig.rotateXRange || [-12, 0, 8],
  rotateYRange: props.animateConfig.rotateYRange || [20, 0, -15],
  scaleRange: props.animateConfig.scaleRange || [0.65, 1, 0.9],
  translateZRange: props.animateConfig.translateZRange || [-250, 0, -80],
  easing: 0.06
})
</script>

<style scoped>
.feature-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 3rem;
  overflow: hidden;
}

.features-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  width: 100%;
  max-width: 1400px;
  will-change: transform;
  transform-style: preserve-3d;
}

.feature-image-wrapper {
  overflow: hidden;
}

.feature-image-placeholder {
  width: 100%;
  min-height: 600px;
  background: var(--gray-light);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 1rem;
}

.feature-text {
  padding: 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.feature-title {
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 900;
  line-height: 0.95;
  letter-spacing: -0.02em;
  margin-bottom: 2rem;
}

.feature-title span {
  color: var(--orange);
}

.feature-description {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.feature-label {
  font-size: 0.9rem;
  color: var(--orange);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

@media (max-width: 768px) {
  .feature-section {
    padding: 0 1.5rem;
  }
  .features-split {
    grid-template-columns: 1fr;
  }
  .feature-text {
    padding: 2rem;
  }
  .feature-image-placeholder {
    min-height: 300px;
  }
}
</style>
