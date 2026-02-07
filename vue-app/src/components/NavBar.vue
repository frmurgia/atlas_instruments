<template>
  <nav>
    <div class="logo proto-mono">
      <span>ATLAS INSTRUMENTS</span>
    </div>
    <a href="#preorder" class="btn-preorder proto-mono" @click.prevent="scrollTo('#preorder')">PRE-ORDER</a>
  </nav>
</template>

<script setup>
function scrollTo(selector) {
  document.querySelector(selector)?.scrollIntoView({ behavior: 'smooth' })
}
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
  background: transparent;
  z-index: 1000;
  transition: padding 0.3s ease;
}

.logo {
  display: flex;
  align-items: center;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.05em;
}

.btn-preorder {
  background: var(--yellow);
  color: var(--black);
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
  box-shadow: 0 6px 20px rgba(232, 212, 77, 0.4);
}

@media (max-width: 768px) {
  nav {
    padding: 1.5rem 1.5rem;
  }
}
</style>
