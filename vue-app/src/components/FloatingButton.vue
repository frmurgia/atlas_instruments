<template>
  <button class="floating-button proto-mono" @click="scrollToMailing">
    MAILING LIST
  </button>
</template>

<script setup>
function scrollToMailing() {
  document.getElementById('mailing')?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped>
.floating-button {
  position: fixed;
  bottom: 3rem;
  right: 3rem;
  width: 150px;
  height: 150px;
  background: var(--yellow);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--black);
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  cursor: pointer;
  z-index: 999;
  border: none;
  text-transform: uppercase;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.floating-button:hover {
  transform: scale(1.08);
  box-shadow: 0 10px 40px rgba(232, 212, 77, 0.4);
}

@media (max-width: 768px) {
  .floating-button {
    width: 120px;
    height: 120px;
    bottom: 2rem;
    right: 2rem;
    font-size: 0.75rem;
  }
}
</style>
