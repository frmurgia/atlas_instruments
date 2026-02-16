<template>
  <div class="floating-wrapper" :class="{ expanded: isOpen }">
    <!-- Collapsed circle button -->
    <button v-if="!isOpen" class="floating-button proto-mono" @click="open">
      MAILING LIST
    </button>

    <!-- Expanded form -->
    <div v-else class="floating-form">
      <button class="close-btn proto-mono" @click="close" aria-label="Close">&times;</button>
      <div class="form-inner">
        <label class="form-label proto-mono">STAY IN THE LOOP</label>
        <div class="input-row">
          <input
            ref="emailInput"
            v-model="email"
            type="email"
            placeholder="YOUR@EMAIL.COM"
            class="email-input proto-mono"
            @keydown.enter="submit"
          />
          <button class="submit-btn proto-mono" @click="submit" :disabled="!isValid">
            &rarr;
          </button>
        </div>
        <transition name="msg">
          <p v-if="submitted" class="success-msg proto-mono">THANK YOU!</p>
        </transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick } from 'vue'

const isOpen = ref(false)
const email = ref('')
const submitted = ref(false)
const emailInput = ref(null)

const isValid = computed(() => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)
})

async function open() {
  isOpen.value = true
  await nextTick()
  emailInput.value?.focus()
}

function close() {
  isOpen.value = false
  submitted.value = false
  email.value = ''
}

function submit() {
  if (!isValid.value) return
  submitted.value = true
  email.value = ''
}
</script>

<style scoped>
.floating-wrapper {
  position: fixed;
  bottom: 3rem;
  right: 3rem;
  z-index: 999;
}

/* --- Circle button --- */
.floating-button {
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
  border: none;
  text-transform: uppercase;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  animation: floatIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}

.floating-button:hover {
  transform: scale(1.08);
  box-shadow: 0 10px 40px rgba(232, 212, 77, 0.4);
}

/* --- Expanded form --- */
.floating-form {
  background: var(--yellow);
  border-radius: 28px;
  padding: 2rem 2.5rem;
  min-width: 380px;
  animation: expandIn 0.45s cubic-bezier(0.34, 1.56, 0.64, 1) both;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1.2rem;
  background: none;
  border: none;
  font-size: 1.6rem;
  cursor: pointer;
  color: var(--black);
  line-height: 1;
  opacity: 0.5;
  transition: opacity 0.2s;
}

.close-btn:hover {
  opacity: 1;
}

.form-inner {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-label {
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.input-row {
  display: flex;
  gap: 0.5rem;
}

.email-input {
  flex: 1;
  background: rgba(0, 0, 0, 0.08);
  border: 2px solid transparent;
  border-radius: 50px;
  padding: 0.9rem 1.4rem;
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  color: var(--black);
  outline: none;
  transition: border-color 0.2s;
}

.email-input::placeholder {
  color: rgba(0, 0, 0, 0.3);
}

.email-input:focus {
  border-color: var(--black);
}

.submit-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: var(--black);
  color: var(--yellow);
  border: none;
  font-size: 1.4rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s, opacity 0.2s;
  flex-shrink: 0;
}

.submit-btn:hover:not(:disabled) {
  transform: scale(1.1);
}

.submit-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.success-msg {
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.1em;
}

/* --- Animations --- */
@keyframes floatIn {
  from {
    opacity: 0;
    transform: scale(0) translateY(20px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

@keyframes expandIn {
  from {
    opacity: 0;
    transform: scale(0.3);
    border-radius: 50%;
  }
  to {
    opacity: 1;
    transform: scale(1);
    border-radius: 28px;
  }
}

.msg-enter-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.msg-enter-from {
  opacity: 0;
  transform: translateY(8px);
}

/* --- Mobile --- */
@media (max-width: 768px) {
  .floating-wrapper {
    bottom: 1.5rem;
    right: 1.5rem;
  }
  .floating-wrapper.expanded {
    left: 1.5rem;
    right: 1.5rem;
  }
  .floating-button {
    width: 90px;
    height: 90px;
    font-size: 0.65rem;
  }
  .floating-form {
    min-width: auto;
    width: 100%;
    padding: 1.2rem;
    border-radius: 20px;
  }
  .email-input {
    padding: 0.7rem 1rem;
    font-size: 0.8rem;
  }
  .submit-btn {
    width: 42px;
    height: 42px;
    font-size: 1.2rem;
  }
}
</style>
