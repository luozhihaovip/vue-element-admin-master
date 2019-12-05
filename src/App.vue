<template>
  <div class="App">
    <HomeLayout/>
  </div>
</template>

<script>
import HomeLayout from '@/layout/home-layout.vue'
export default {
  name: 'App',

  components: {
    HomeLayout
  },

  filters: {
  },

  mixins: [
  ],

  props: {
  },

  data () {
    return {
    }
  },

  computed: {
  },

  watch: {
  },

  created () {
  },

  mounted () {
  },

  methods: {
    init () {}
  }
}
</script>

<style lang="scss">
*{
  margin: 0;
  padding: 0;
}
html,body{
  height: 100%;
  width: 100%;
}
.App {
  height: 100%;
  width: 100%;
}
</style>
