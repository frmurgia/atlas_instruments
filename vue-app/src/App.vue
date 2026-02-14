<script setup>
import GridBackground from './components/GridBackground.vue'
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
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

    <FeatureSection
      title-number="10"
      title-text="TRACKS"
      description="Ten independent audio tracks with individual control. 75mm linear faders, RGB LED VU meters for real-time monitoring. 24-bit/48kHz WAV recording."
      label="FEATURE 1/3"
      placeholder="FEATURE PHOTO 1"
      :image-left="true"
    />
    <FeatureSection
      title-number="3 MIDI"
      title-text="OUTPUTS"
      description="Three fully independent MIDI 5-pin DIN outputs. Sync modular synths, drum machines and external effects with your loops. Customizable MIDI CC control."
      label="FEATURE 2/3"
      placeholder="FEATURE PHOTO 2"
      :image-left="false"
    />
    <FeatureSection
      title-number="NO"
      title-text="SCREEN"
      description="Fully physical interface. Zero menus, zero distractions. Immediate control with faders, rotary encoders, toggle switches and multicolor LEDs. Tactile and intuitive workflow."
      label="FEATURE 3/3"
      placeholder="FEATURE PHOTO 3"
      :image-left="true"
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
