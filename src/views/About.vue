<template>
<div id="about">
  <h1><router-view class="view one">one</router-view>
<router-view class="view two" name="a">a</router-view>
<router-view class="view three" name="b">b</router-view></h1>
  <p>

  </p>
  <!-- 路由出口 -->
  <!-- 路由匹配到的组件将渲染在这里 -->
  <router-view></router-view>
</div>
</template>
<script>
export default {
  computed: {
    username() {
      // 我们很快就会看到 `params` 是什么
      return this.$route.params.username
    }
  },
  methods: {
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push('/')
    }
  }
}
  
</script>