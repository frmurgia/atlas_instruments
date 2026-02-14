<template>
  <section class="feature-section">
    <div class="features-split" :class="{ 'image-right': !imageLeft }">
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
defineProps({
  titleNumber: String,
  titleText: String,
  description: String,
  label: String,
  placeholder: String,
  imageLeft: { type: Boolean, default: true }
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
  border-radius: 16px;
}

.feature-text {
  padding: 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.feature-title {
  font-size: clamp(4rem, 10vw, 8rem);
  font-weight: 900;
  line-height: 0.95;
  letter-spacing: -0.02em;
  margin-bottom: 2rem;
}

.feature-title span {
  color: var(--yellow);
}

.feature-description {
  font-size: 1.15rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.feature-label {
  font-size: 1rem;
  color: var(--yellow);
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
  .feature-title {
    font-size: clamp(3rem, 10vw, 5rem);
  }
}
</style>
