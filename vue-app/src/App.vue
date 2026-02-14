<script setup>
import GridBackground from './components/GridBackground.vue'
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import FeatureSection from './components/FeatureSection.vue'
import HowItWorksSection from './components/HowItWorksSection.vue'
import WhatItReplacesSection from './components/WhatItReplacesSection.vue'
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
      description="Ten independent audio tracks, each with its own 75mm linear fader and RGB LED meter. Load your set, press play, perform. Every track starts and stops in perfect sync with a single button press."
      label="FEATURE 1/3"
      placeholder="FEATURE PHOTO 1"
      :image-left="true"
    />
    <FeatureSection
      title-number="2 MIDI"
      title-text="OUTPUTS"
      description="Two independent MIDI 5-pin DIN outputs to sync your modular synths, drum machines and external gear. TenLooper sits at the center of your setup and keeps everything locked in time."
      label="FEATURE 2/3"
      placeholder="FEATURE PHOTO 2"
      :image-left="false"
    />
    <FeatureSection
      title-number="NO"
      title-text="SCREEN"
      description="No menus. No submenus. No scrolling. Every control does one thing. After a few sessions you'll operate it without looking — muscle memory takes over and your attention stays where it belongs: on the music."
      label="FEATURE 3/3"
      placeholder="FEATURE PHOTO 3"
      :image-left="true"
    />

    <HowItWorksSection />
    <WhatItReplacesSection />
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
