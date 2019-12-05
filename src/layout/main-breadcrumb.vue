<template>
  <div class="main-breadcrumb">
    <el-breadcrumb separator="/">
  <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
  <el-breadcrumb-item :to="{ path: '/page' }">活动管理</el-breadcrumb-item>
  <el-breadcrumb-item>活动列表</el-breadcrumb-item>
  <el-breadcrumb-item>活动详情</el-breadcrumb-item>
</el-breadcrumb>
  </div>
</template>

<script>
export default {
  name: 'main-breadcrumb',

  components: {
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
.main-breadcrumb {
  height: 30px;
  width: 100%;
  background:#409EFF  ;
}
</style>
