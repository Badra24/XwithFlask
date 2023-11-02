<template>
  <!-- <button :type="buttonType" class="bg-green-500 p-2 mt-3 rounded-md text-white hover:bg-green-800" > {{ name }}</button> -->
  <button
    :type="buttonType"
    class="mt-5 relative py-2 px-8 text-black text-base font-bold uppercase rounded-[50px] overflow-hidden bg-white transition-all duration-400 ease-in-out shadow-md hover:scale-105 hover:text-white hover:shadow-lg active:scale-90 before:absolute before:top-0 before:-left-full before:w-full before:h-full before:bg-gradient-to-r before:from-pink-500 before:to-pink-300 before:transition-all before:duration-500 before:ease-in-out before:z-[-1] before:rounded-[50px] hover:before:left-0"
  >
    {{ name }}
  </button>
</template>

<script setup>
defineProps({
  class: String,
  isClicked: Boolean,
  buttonType: String,
  name: {
    type: String,
    defaul: "Submit",
  },
});
</script>
