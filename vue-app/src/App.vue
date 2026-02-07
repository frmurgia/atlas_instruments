<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import GridBackground from './components/GridBackground.vue'
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import ModelViewer from './components/ModelViewer.vue'
import SpecsSection from './components/SpecsSection.vue'
import CtaSection from './components/CtaSection.vue'
import FeaturesListSection from './components/FeaturesListSection.vue'
import MailingSection from './components/MailingSection.vue'
import FloatingButton from './components/FloatingButton.vue'

const modelScrollProgress = ref(0)
const modelSection = ref(null)

function onScroll() {
  if (!modelSection.value) return
  const rect = modelSection.value.getBoundingClientRect()
  const sectionH = modelSection.value.scrollHeight - window.innerHeight
  if (sectionH <= 0) return
  const rawProgress = -rect.top / sectionH
  modelScrollProgress.value = Math.max(0, Math.min(1, rawProgress))
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<template>
  <GridBackground />
  <NavBar />
  <FloatingButton />
  <main>
    <HeroSection />

    <!-- Sticky 3D model section: tall scroll area with fixed viewport -->
    <div ref="modelSection" class="model-scroll-area">
      <div class="model-sticky">
        <ModelViewer :scroll-progress="modelScrollProgress" />
      </div>
    </div>

    <SpecsSection />
    <CtaSection />
    <FeaturesListSection />
    <MailingSection />
  </main>
</template>

<style>
main {
  position: relative;
  z-index: 1;
}

.model-scroll-area {
  position: relative;
  height: 400vh; /* tall enough for 3 feature sections worth of scroll */
}

.model-sticky {
  position: sticky;
  top: 0;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}
</style>
