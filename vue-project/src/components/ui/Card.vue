<template>
  <div
    class="bg-white rounded-lg shadow-lg mb-10 mt-5 hover:bg-gray-100 transform transition-transform duration-300 hover:scale-105"
  >
    <!-- Card Body -->
    <div class="p-4">
      <img v-if="imgPath" :src="imgPath" :alt="imgName" />
      <p class="text-gray-800 font-bold text-2xl">
        {{ tweet }}
      </p>
    </div>
    <div class="ml-2 mb-2">
      <div class="flex items-center">
        <Button
          name="Like"
          :is-clicked="isClicked"
          class="p-2 rounded-md transition-transform duration-300 transform hover:scale-110"
          :class="{
            'bg-pink-500 text-white': !isClicked,
            'border-2 border-pink-500 text-pink-500': isClicked,
          }"
          @click="buttonClicked"
        />
        <span class="ml-2 text-pink-500">{{ likes }}</span>
      </div>
    </div>

    <!-- Card Caption -->
    <div class="bg-gray-200 p-3 text-gray-600">
      <p>Tweet From {{ user }}</p>
    </div>
  </div>
</template>

<script setup>
import Button from "./Button.vue";
import { ref } from "vue";
import { useFetch } from "../../composable/useFetch";
const msg = ref("");
const { user, tweet, imgPath, imgName, tweetId, likes } = defineProps([
  "user",
  "tweet",
  "imgPath",
  "imgName",
  "tweetId",
  "likes",
]);

const { tryLike, success } = useFetch();

const isClicked = ref(false);
const handleLike = async () => {
  try {
    // Kirim permintaan untuk menambah jumlah "Like" ke server
    const response = await tryLike(`api/tweets/like/${tweetId}`);

    if (response.success) {
      // Jika permintaan berhasil, tambahkan jumlah "Like" secara lokal
      msg.value = "Liked post";
    }
  } catch (error) {
    console.error(error);
  }
};

const buttonClicked = () => {
  if (!isClicked.value) {
    handleLike();
    console.log(likes); // Panggil fungsi handleLike saat tombol "Like" diklik
  }
  isClicked.value = !isClicked.value;
};
</script>
