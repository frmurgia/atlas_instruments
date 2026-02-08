<template>
  <div ref="container" class="model-viewer">
    <div class="split-layout" :class="layoutClass">
      <!-- Text panel -->
      <div class="text-panel">
        <transition name="fade" mode="out-in">
          <div v-if="activeSection === 0" key="s0" class="text-content">
            <div class="overlay-label proto-mono">FEATURE 1/3</div>
            <h2 class="overlay-title proto-mono"><span>10</span><br>TRACKS</h2>
            <p class="overlay-desc">Ten independent audio tracks with individual control. 75mm linear faders, RGB LED VU meters for real-time monitoring. 24-bit/48kHz WAV recording.</p>
          </div>
          <div v-else-if="activeSection === 1" key="s1" class="text-content">
            <div class="overlay-label proto-mono">FEATURE 2/3</div>
            <h2 class="overlay-title proto-mono"><span>3 MIDI</span><br>OUTPUTS</h2>
            <p class="overlay-desc">Three fully independent MIDI 5-pin DIN outputs. Sync modular synths, drum machines and external effects with your loops. Customizable MIDI CC control.</p>
          </div>
          <div v-else-if="activeSection === 2" key="s2" class="text-content">
            <div class="overlay-label proto-mono">FEATURE 3/3</div>
            <h2 class="overlay-title proto-mono"><span>NO</span><br>SCREEN</h2>
            <p class="overlay-desc">Fully physical interface. Zero menus, zero distractions. Immediate control with faders, rotary encoders, toggle switches and multicolor LEDs. Tactile and intuitive workflow.</p>
          </div>
          <div v-else key="empty" class="text-content"></div>
        </transition>
      </div>
      <!-- 3D canvas panel -->
      <div class="canvas-panel">
        <canvas ref="canvas"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import * as THREE from 'three'
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'

const props = defineProps({
  scrollProgress: { type: Number, default: 0 }
})

const container = ref(null)
const canvas = ref(null)

const activeSection = computed(() => {
  const p = props.scrollProgress
  if (p < 0.10) return -1
  if (p < 0.35) return 0     // 10 TRACKS — model RIGHT
  if (p < 0.60) return 1     // 3 MIDI OUTPUTS — model LEFT
  if (p < 0.90) return 2     // NO SCREEN — model RIGHT
  return -1
})

// Layout flips: model-right, model-left, model-right
const layoutClass = computed(() => {
  const s = activeSection.value
  if (s === 1) return 'model-left'
  return 'model-right'
})

// Camera keyframes — top view, back view, 3/4 view
const keyframes = [
  { t: 0.00, pos: [0,  3.0,  0.5], look: [0, 0, 0] },
  { t: 0.10, pos: [0,  2.8,  0.3], look: [0, 0, 0] },   // top view
  { t: 0.35, pos: [0,  2.8,  0.3], look: [0, 0, 0] },   // hold
  { t: 0.48, pos: [0,  0.3, -2.5], look: [0, 0, 0] },   // back view
  { t: 0.60, pos: [0,  0.3, -2.5], look: [0, 0, 0] },   // hold
  { t: 0.73, pos: [1.8, 1.5,  1.8], look: [0, 0, 0] },  // 3/4 view
  { t: 0.90, pos: [1.8, 1.5,  1.8], look: [0, 0, 0] },  // hold
  { t: 1.00, pos: [2.5, 2.0,  2.5], look: [0, 0, 0] },  // exit
]

let renderer, scene, camera, model
let animationId
let currentPos = new THREE.Vector3(0, 3.0, 0.5)
let currentLook = new THREE.Vector3(0, 0, 0)

function lerpKeyframes(progress) {
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
  const canvasEl = canvas.value
  const panel = canvasEl.parentElement
  const w = panel.clientWidth
  const h = panel.clientHeight

  renderer = new THREE.WebGLRenderer({
    canvas: canvasEl,
    antialias: true,
    alpha: true
  })
  renderer.setSize(w, h)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.4

  scene = new THREE.Scene()
  renderer.setClearColor(0x000000, 0)

  camera = new THREE.PerspectiveCamera(40, w / h, 0.1, 100)
  camera.position.set(0, 3.0, 0.5)
  camera.lookAt(0, 0, 0)

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

  const loader = new GLTFLoader()
  loader.load('/tenlooper.glb', (gltf) => {
    model = gltf.scene
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
  if (!canvas.value || !renderer) return
  const panel = canvas.value.parentElement
  const w = panel.clientWidth
  const h = panel.clientHeight
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
  if (renderer) renderer.dispose()
})
</script>

<style scoped>
.model-viewer {
  position: relative;
  width: 100%;
  height: 100%;
}

.split-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  height: 100%;
  transition: none;
}

/* model-right: text LEFT, canvas RIGHT */
.split-layout.model-right .text-panel { order: 1; }
.split-layout.model-right .canvas-panel { order: 2; }

/* model-left: canvas LEFT, text RIGHT */
.split-layout.model-left .text-panel { order: 2; }
.split-layout.model-left .canvas-panel { order: 1; }

.text-panel {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 4rem;
}

.text-content {
  max-width: 600px;
}

.canvas-panel {
  position: relative;
  overflow: hidden;
}

canvas {
  display: block;
  width: 100%;
  height: 100%;
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
  font-size: clamp(4rem, 10vw, 8rem);
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

/* Fade transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(25px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-15px);
}

@media (max-width: 768px) {
  .split-layout {
    grid-template-columns: 1fr;
  }
  .text-panel {
    padding: 2rem 1.5rem;
    order: 2 !important;
  }
  .canvas-panel {
    order: 1 !important;
    min-height: 50vh;
  }
  .overlay-title {
    font-size: clamp(3rem, 10vw, 5rem);
  }
  .overlay-desc {
    font-size: 0.95rem;
  }
}
</style>
