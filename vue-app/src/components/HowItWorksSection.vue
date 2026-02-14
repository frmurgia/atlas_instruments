<template>
  <section class="how-section">
    <div class="how-wrapper">
      <h2 ref="titleEl" class="section-title proto-mono" :style="titleStyle">HOW IT WORKS</h2>
      <div class="how-body">
        <p>TenLooper separates two moments that other devices mix together: preparing and performing.</p>
        <p>At home, press the rear button during startup to enter configuration mode. TenLooper creates a local web page — open it from any browser on your phone, tablet or computer, drag your WAV files in, assign them to tracks and banks. If you work in Ableton Live, a dedicated Max for Live plugin lets you manage everything without leaving your session.</p>
        <p>On stage, none of that exists. You get one toggle switch, ten faders and ten LED meters. That's it. Flip the switch, the entire set starts in sync. Adjust levels on the fly. Read the LEDs to see what each track is doing — a rhythmic pattern looks different from a pad or a melodic line. No configuration, no troubleshooting, no laptop.</p>
        <p>Need more than 10 tracks? Connect two or more TenLoopers via the Sync port. 20, 30 or more tracks, perfectly synchronized, zero computers.</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useScrollAnimation } from '../composables/useScrollAnimation.js'

const { el: titleEl, style: titleStyle } = useScrollAnimation({
  rotateXRange: [-2, 0, 1],
  rotateYRange: [2, 0, -1],
  scaleRange: [0.97, 1, 0.99],
  translateZRange: [-15, 0, -5],
  easing: 0.06
})
</script>

<style scoped>
.how-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6rem 3rem;
  overflow: hidden;
}

.how-wrapper {
  width: 100%;
  max-width: 1400px;
}

.section-title {
  font-size: clamp(4rem, 10vw, 8rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: -0.02em;
  margin-bottom: 3rem;
  will-change: transform;
}

.how-body {
  max-width: 800px;
}

.how-body p {
  font-size: 1.15rem;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.how-body p:last-child {
  margin-bottom: 0;
}

@media (max-width: 768px) {
  .how-section {
    padding: 4rem 1.5rem;
  }
}
</style>
