<template>
  <div ref="container" class="model-viewer">
    <canvas ref="canvas"></canvas>
    <!-- Feature text overlays -->
    <transition name="fade">
      <div v-if="activeSection === 0" class="overlay-text overlay-top" key="s0">
        <div class="overlay-label proto-mono">FEATURE 1/3</div>
        <h2 class="overlay-title proto-mono"><span>10</span><br>TRACKS</h2>
        <p class="overlay-desc">Ten independent audio tracks with individual control. 75mm linear faders, RGB LED VU meters for real-time monitoring. 24-bit/48kHz WAV recording.</p>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="activeSection === 1" class="overlay-text overlay-back" key="s1">
        <div class="overlay-label proto-mono">FEATURE 2/3</div>
        <h2 class="overlay-title proto-mono"><span>3 MIDI</span><br>OUTPUTS</h2>
        <p class="overlay-desc">Three fully independent MIDI 5-pin DIN outputs. Sync modular synths, drum machines and external effects with your loops. Customizable MIDI CC control.</p>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="activeSection === 2" class="overlay-text overlay-quarter" key="s2">
        <div class="overlay-label proto-mono">FEATURE 3/3</div>
        <h2 class="overlay-title proto-mono"><span>NO</span><br>SCREEN</h2>
        <p class="overlay-desc">Fully physical interface. Zero menus, zero distractions. Immediate control with faders, rotary encoders, toggle switches and multicolor LEDs. Tactile and intuitive workflow.</p>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import * as THREE from 'three'
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'

const props = defineProps({
  scrollProgress: { type: Number, default: 0 }
})

const container = ref(null)
const canvas = ref(null)

const activeSection = computed(() => {
  const p = props.scrollProgress
  if (p < 0.15) return -1      // transitioning in
  if (p < 0.38) return 0       // top view — 10 TRACKS
  if (p < 0.62) return 1       // back view — 3 MIDI OUTPUTS
  if (p < 0.88) return 2       // 3/4 view — NO SCREEN
  return -1                     // transitioning out
})

// Camera keyframes: [scrollProgress, cameraX, cameraY, cameraZ, lookAtX, lookAtY, lookAtZ]
const keyframes = [
  { t: 0.00, pos: [0,  3.0,  0.5], look: [0, 0, 0] },   // top-ish (entering)
  { t: 0.15, pos: [0,  2.8,  0.3], look: [0, 0, 0] },   // top view — 10 TRACKS
  { t: 0.38, pos: [0,  2.8,  0.3], look: [0, 0, 0] },   // hold top view
  { t: 0.50, pos: [0,  0.3, -2.5], look: [0, 0, 0] },   // back view — 3 MIDI OUTPUTS
  { t: 0.62, pos: [0,  0.3, -2.5], look: [0, 0, 0] },   // hold back view
  { t: 0.75, pos: [1.8, 1.5,  1.8], look: [0, 0, 0] },  // 3/4 view — NO SCREEN
  { t: 0.88, pos: [1.8, 1.5,  1.8], look: [0, 0, 0] },  // hold 3/4
  { t: 1.00, pos: [2.5, 2.0,  2.5], look: [0, 0, 0] },  // zoom out exit
]

let renderer, scene, camera, model
let animationId
let currentPos = new THREE.Vector3(0, 3.0, 0.5)
let currentLook = new THREE.Vector3(0, 0, 0)

function lerpKeyframes(progress) {
  // Find the two keyframes we're between
  let k0 = keyframes[0]
  let k1 = keyframes[keyframes.length - 1]

  for (let i = 0; i < keyframes.length - 1; i++) {
    if (progress >= keyframes[i].t && progress <= keyframes[i + 1].t) {
      k0 = keyframes[i]
      k1 = keyframes[i + 1]
      break
    }
  }

  const range = k1.t - k0.t
  const localT = range > 0 ? (progress - k0.t) / range : 0
  // Smooth step easing
  const t = localT * localT * (3 - 2 * localT)

  return {
    pos: [
      k0.pos[0] + (k1.pos[0] - k0.pos[0]) * t,
      k0.pos[1] + (k1.pos[1] - k0.pos[1]) * t,
      k0.pos[2] + (k1.pos[2] - k0.pos[2]) * t,
    ],
    look: [
      k0.look[0] + (k1.look[0] - k0.look[0]) * t,
      k0.look[1] + (k1.look[1] - k0.look[1]) * t,
      k0.look[2] + (k1.look[2] - k0.look[2]) * t,
    ]
  }
}

function initScene() {
  const w = container.value.clientWidth
  const h = container.value.clientHeight

  // Renderer
  renderer = new THREE.WebGLRenderer({
    canvas: canvas.value,
    antialias: true,
    alpha: true
  })
  renderer.setSize(w, h)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.4

  // Scene — no background so the CSS mint + grid shows through
  scene = new THREE.Scene()
  renderer.setClearColor(0x000000, 0)

  // Camera
  camera = new THREE.PerspectiveCamera(40, w / h, 0.1, 100)
  camera.position.set(0, 3.0, 0.5)
  camera.lookAt(0, 0, 0)

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6)
  scene.add(ambientLight)

  const dirLight1 = new THREE.DirectionalLight(0xffffff, 1.5)
  dirLight1.position.set(3, 5, 4)
  scene.add(dirLight1)

  const dirLight2 = new THREE.DirectionalLight(0xfff4b0, 0.8)
  dirLight2.position.set(-3, 2, -2)
  scene.add(dirLight2)

  const dirLight3 = new THREE.DirectionalLight(0xffffff, 0.4)
  dirLight3.position.set(0, -3, 0)
  scene.add(dirLight3)

  // Load model
  const loader = new GLTFLoader()
  loader.load('/tenlooper.glb', (gltf) => {
    model = gltf.scene

    // Override material for nicer look
    model.traverse((child) => {
      if (child.isMesh) {
        child.material = new THREE.MeshStandardMaterial({
          color: 0xE8D44D,
          metalness: 0.15,
          roughness: 0.65,
        })
      }
    })

    scene.add(model)
  })

  animate()
}

function animate() {
  if (!renderer) return

  const target = lerpKeyframes(props.scrollProgress)

  // Smooth interpolation toward target
  currentPos.x += (target.pos[0] - currentPos.x) * 0.08
  currentPos.y += (target.pos[1] - currentPos.y) * 0.08
  currentPos.z += (target.pos[2] - currentPos.z) * 0.08

  currentLook.x += (target.look[0] - currentLook.x) * 0.08
  currentLook.y += (target.look[1] - currentLook.y) * 0.08
  currentLook.z += (target.look[2] - currentLook.z) * 0.08

  camera.position.copy(currentPos)
  camera.lookAt(currentLook)

  renderer.render(scene, camera)
  animationId = requestAnimationFrame(animate)
}

function onResize() {
  if (!container.value || !renderer) return
  const w = container.value.clientWidth
  const h = container.value.clientHeight
  renderer.setSize(w, h)
  camera.aspect = w / h
  camera.updateProjectionMatrix()
}

onMounted(() => {
  initScene()
  window.addEventListener('resize', onResize)
})

onUnmounted(() => {
  cancelAnimationFrame(animationId)
  window.removeEventListener('resize', onResize)
  if (renderer) {
    renderer.dispose()
  }
})
</script>

<style scoped>
.model-viewer {
  position: relative;
  width: 100%;
  height: 100%;
}

canvas {
  display: block;
  width: 100%;
  height: 100%;
}

.overlay-text {
  position: absolute;
  max-width: 650px;
  pointer-events: none;
}

.overlay-top {
  bottom: 8%;
  left: 6%;
}

.overlay-back {
  top: 10%;
  right: 6%;
  text-align: right;
}

.overlay-quarter {
  bottom: 10%;
  left: 6%;
}

.overlay-label {
  font-size: 1rem;
  color: var(--yellow);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 1rem;
}

.overlay-title {
  font-size: clamp(4rem, 12vw, 10rem);
  font-weight: 900;
  line-height: 0.95;
  letter-spacing: -0.02em;
  margin-bottom: 1.5rem;
}

.overlay-title span {
  color: var(--yellow);
}

.overlay-desc {
  font-size: 1.15rem;
  line-height: 1.6;
  max-width: 520px;
}

.overlay-back .overlay-desc {
  margin-left: auto;
}

/* Fade transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(30px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

@media (max-width: 768px) {
  .overlay-text {
    max-width: 280px;
  }
  .overlay-top {
    bottom: 5%;
    left: 4%;
  }
  .overlay-back {
    top: 5%;
    right: 4%;
  }
  .overlay-quarter {
    bottom: 5%;
    left: 4%;
  }
  .overlay-desc {
    font-size: 0.9rem;
  }
}
</style>
