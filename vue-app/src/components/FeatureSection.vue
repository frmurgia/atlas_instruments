<template>
  <section class="feature-section">
    <div class="features-split" :class="{ 'image-right': !imageLeft }">
      <div class="feature-image-wrapper">
        <img
          v-if="!imgError"
          :src="image"
          :alt="titleNumber + ' ' + titleText"
          class="feature-image"
          @error="imgError = true"
        >
        <div v-else class="feature-image-placeholder">
          [{{ placeholder }}]
        </div>
      </div>
      <div class="feature-text">
        <div class="feature-text-top">
          <h2 class="feature-title proto-mono">
            <span>{{ titleNumber }}</span><br>{{ titleText }}
          </h2>
        </div>
        <div class="feature-text-bottom">
          <p class="feature-description">{{ description }}</p>
          <div class="feature-label proto-mono">{{ label }}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  titleNumber: String,
  titleText: String,
  description: String,
  label: String,
  placeholder: String,
  image: String,
  imageLeft: { type: Boolean, default: true }
})

const imgError = ref(false)
</script>

<style scoped>
.feature-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 2rem 2rem;
  overflow: hidden;
}

.features-split {
  display: grid;
  grid-template-columns: 55% 1fr;
  gap: 3rem;
  width: 100%;
}

.features-split.image-right {
  grid-template-columns: 1fr 55%;
}

.features-split.image-right .feature-image-wrapper {
  order: 2;
}

.features-split.image-right .feature-text {
  order: 1;
}

.feature-image-wrapper {
  overflow: hidden;
  border-radius: 16px;
}

.feature-image {
  width: 100%;
  height: 100%;
  min-height: 85vh;
  object-fit: cover;
  display: block;
}

.feature-image-placeholder {
  width: 100%;
  height: 100%;
  min-height: 85vh;
  background: var(--gray-light);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #999;
  font-size: 1rem;
}

.feature-text {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 1rem 0;
}

.feature-text-top {
  padding-top: 1rem;
}

.feature-title {
  font-size: clamp(5rem, 12vw, 10rem);
  font-weight: 900;
  line-height: 0.95;
  letter-spacing: -0.02em;
}

.feature-title span {
  color: var(--yellow);
}

.feature-text-bottom {
  padding-bottom: 1rem;
}

.feature-description {
  font-size: 1.1rem;
  line-height: 1.5;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  margin-bottom: 1rem;
  max-width: 520px;
}

.feature-label {
  font-size: 1rem;
  color: var(--black);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  background: var(--yellow);
  display: inline;
  padding: 0.2em 0.4em;
}

@media (max-width: 768px) {
  .feature-section {
    padding: 1rem 1rem;
  }
  .features-split,
  .features-split.image-right {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  .features-split.image-right .feature-image-wrapper {
    order: 0;
  }
  .features-split.image-right .feature-text {
    order: 0;
  }
  .feature-image-placeholder {
    min-height: 50vh;
  }
  .feature-title {
    font-size: clamp(3.5rem, 12vw, 6rem);
  }
  .feature-text {
    padding: 0 0.5rem;
    gap: 2rem;
  }
}
</style>
