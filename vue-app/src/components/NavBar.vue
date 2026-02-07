<template>
  <nav :class="{ 'nav-scrolled': hasScrolled }">
    <div class="logo proto-mono">
      <div class="logo-circle"></div>
      <span>ATLAS INSTRUMENTS</span>
    </div>
    <a href="#preorder" class="btn-preorder proto-mono" @click.prevent="scrollTo('#preorder')">PRE-ORDER</a>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const hasScrolled = ref(false)

function onScroll() {
  hasScrolled.value = window.scrollY > 50
}

function scrollTo(selector) {
  document.querySelector(selector)?.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<style scoped>
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 2rem 3rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  z-index: 1000;
  transition: padding 0.3s ease, box-shadow 0.3s ease;
}

nav.nav-scrolled {
  padding: 1rem 3rem;
  box-shadow: 0 1px 0 rgba(0,0,0,0.08);
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.05em;
}

.logo-circle {
  width: 32px;
  height: 32px;
  background: var(--orange);
  border-radius: 50%;
  transition: transform 0.3s ease;
}

nav:hover .logo-circle {
  transform: scale(1.1);
}

.btn-preorder {
  background: var(--orange);
  color: var(--white);
  padding: 0.8rem 2rem;
  border: none;
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.05em;
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
  border-radius: 50px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-preorder:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255, 69, 0, 0.3);
}

@media (max-width: 768px) {
  nav {
    padding: 1.5rem 1.5rem;
  }
  nav.nav-scrolled {
    padding: 1rem 1.5rem;
  }
}
</style>
