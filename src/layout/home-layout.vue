<template>
  <div class="home-layout">
    <el-container class="home-layout__container">
      <el-header class="home-layout__header"></el-header>
        <el-container>
            <el-aside class="home-layout__aside" width="200px">
              <AsideMenu/>
            </el-aside>
            <el-main class="home-layout__main">
              <MainBreadcrumb></MainBreadcrumb>
              <router-view>
              </router-view>
            </el-main>
        </el-container>
    </el-container>
  </div>
</template>

<script>
import AsideMenu from "./aside-menu.vue";
import MainBreadcrumb from "./main-breadcrumb.vue";
export default {
  name: 'home-layout',
  components: {
    AsideMenu,
    MainBreadcrumb
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

<style lang="scss" scoped>
.home-layout {
  height: 100%;
  &>.home-layout__container{
      height: 100%;
      width: 100%;
    &>.home-layout__header{
      background:rgba(54, 43, 43, 0.685);
    }
    .home-layout__aside{
      height: 100%;
    }
    .home-layout__main{
      padding: 0px;
    }
  }
}
</style>
