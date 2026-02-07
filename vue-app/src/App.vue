<script setup>
import GridBackground from './components/GridBackground.vue'
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import DeviceOutline from './components/DeviceOutline.vue'
import FeatureSection from './components/FeatureSection.vue'
import SpecsSection from './components/SpecsSection.vue'
import CtaSection from './components/CtaSection.vue'
import FeaturesListSection from './components/FeaturesListSection.vue'
import MailingSection from './components/MailingSection.vue'
import FloatingButton from './components/FloatingButton.vue'
</script>

<template>
  <GridBackground />
  <NavBar />
  <FloatingButton />
  <main>
    <HeroSection />
    <DeviceOutline />
    <FeatureSection
      title-number="10"
      title-text="TRACKS"
      description="Dieci tracce audio indipendenti con controllo individuale. Fader lineari da 75mm, VU meter LED RGB per monitoring in tempo reale. Registrazione WAV 24-bit/48kHz."
      label="FEATURE 1/3"
      placeholder="FEATURE PHOTO 1"
      :image-left="true"
      :animate-config="{ rotateXRange: [-12, 0, 8], rotateYRange: [25, 0, -15], scaleRange: [0.65, 1, 0.9] }"
    />
    <FeatureSection
      title-number="3 MIDI"
      title-text="OUTPUTS"
      description="Tre uscite MIDI 5-pin DIN completamente indipendenti. Sincronizza synth modulari, drum machine ed effetti esterni con i tuoi loop. Controllo MIDI CC personalizzabile."
      label="FEATURE 2/3"
      placeholder="FEATURE PHOTO 2"
      :image-left="false"
      :animate-config="{ rotateXRange: [-10, 0, 12], rotateYRange: [-20, 0, 18], scaleRange: [0.6, 1, 0.85] }"
    />
    <FeatureSection
      title-number="NO"
      title-text="SCREEN"
      description="Interfaccia completamente fisica. Zero menu, zero distrazione. Controllo immediato con fader, encoder rotativi, toggle switch e LED multicolore. Workflow tattile e intuitivo."
      label="FEATURE 3/3"
      placeholder="FEATURE PHOTO 3"
      :image-left="true"
      :animate-config="{ rotateXRange: [-8, 0, 15], rotateYRange: [30, 0, -10], scaleRange: [0.7, 1, 0.88] }"
    />
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
</style>
