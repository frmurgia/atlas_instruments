<template>
  <div class="grid-bg" aria-hidden="true">
    <div class="grid-lines"></div>
  </div>
</template>

<style scoped>
.grid-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.grid-lines {
  width: 100%;
  height: 100%;
  background-image:
    linear-gradient(to right, var(--grid-color) 1px, transparent 1px),
    linear-gradient(to bottom, var(--grid-color) 1px, transparent 1px);
  background-size: var(--grid-size) var(--grid-size);
}
</style>
