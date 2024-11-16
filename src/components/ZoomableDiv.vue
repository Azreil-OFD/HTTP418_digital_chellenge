<template>
  <div class="container" @wheel="zoom" @mousedown="startDrag" @mouseup="stopDrag" @mousemove="drag" 
       @touchstart="startDrag" @touchend="stopDrag" @touchmove="drag">
    <div
      class="zoomable-object"
      :style="objectStyle"
      ref="object"
    >
      <slot></slot> <!-- Слот для передачи содержимого -->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      scale: 1,
      isDragging: false,
      lastMousePosition: { x: 0, y: 0 },
      position: { x: 0, y: 0 }
    };
  },
  computed: {
    objectStyle() {
      return {
        transform: `translate(${this.position.x}px, ${this.position.y}px) scale(${this.scale})`,
        transition: 'transform 0.1s'
      };
    }
  },
  methods: {
    zoom(event) {
      event.preventDefault();
      const delta = event.deltaY > 0 ? -0.1 : 0.1;
      this.scale = Math.max(0.1, this.scale + delta);
    },
    startDrag(event) {
      this.isDragging = true;
      const touch = event.touches ? event.touches[0] : event;
      this.lastMousePosition = { x: touch.clientX, y: touch.clientY };
    },
    stopDrag() {
      this.isDragging = false;
    },
    drag(event) {
      if (this.isDragging) {
        const touch = event.touches ? event.touches[0] : event;
        const dx = touch.clientX - this.lastMousePosition.x;
        const dy = touch.clientY - this.lastMousePosition.y;
        this.position.x += dx;
        this.position.y += dy;
        this.lastMousePosition = { x: touch.clientX, y: touch.clientY };
      }
    }
  }
};
</script>

<style scoped>
.container {
  width: 100%;
  height: 50vh;
  overflow: hidden;
  position: relative;
  border: 1px solid #ccc;
}

.zoomable-object {
  position: absolute;
  left: 50%;
  top: 50%;
  transform-origin: top left;
}
</style>
