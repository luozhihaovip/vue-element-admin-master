<template>
<div class="home">

  <el-col :span="24"><div class="grid-content bg-purple-dark"></div></el-col>

  <div class="home_body">
    
    <el-input v-model="input" placeholder="请输入内容">名称搜索:</el-input>
    <el-input v-model="address" placeholder="请输入内容">diz:</el-input>
    <el-button type="primary" @click="addItme">主要按钮</el-button>
  </div>
    <el-table
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
    <el-table-column
      prop="date"
      label="日期"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="address"
      label="地址"
       width="180">
    </el-table-column>
    <el-table-column
      prop="run"
      label="操作"
      width="180">
      <el-button type="success">成功按钮</el-button>
    </el-table-column>
    
  </el-table>
  </div>
</template>

<style>
  .home_body {
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)  
  }
  .el-row {
    margin-bottom: 20px;

  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
    width: 1464px;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
</style>

<script>
  import { setIpConfig } from '@/api/common.js'
  export default {
    created(){
      this.setIpConfig()
    },
    methods: {
      setIpConfig(){
        setIpConfig({
          ipName:this.ipName
        })
        .then((data)=>{
          console.log(data)
          debugger
        })
      },
      addItme(){
        this.tableData.push({
          ip: this.input,
          name: this.input,
          address: this.address,
          dj:1
        })
      },
      tableRowClassName(rowIndex) {
        if (rowIndex === 1) {
          return 'warning-row';
        } else if (rowIndex === 3) {
          return 'success-row';
        }
        return '';
      }
    },
    data() {
      return {
        input:'',
        address:'dizi',
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          dj:1
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          dj:1
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          dj:3
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          dj:3
        }]
      }
    }
  }
</script>