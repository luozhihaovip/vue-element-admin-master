<template>
	<div class="the-page">
		<div class="the-a">
			<div class="the-b">
				<a>项目搜索：</a>
				<el-input v-model="input" placeholder="请输入内容" class="input-name"></el-input>
				<ViewFromsAdd>默认按钮</ViewFromsAdd>
				<el-button type="primary" @click="addItme">主要按钮</el-button>
			</div>
		</div>
		<div class="the-one">
			<el-table :data="tableData" border style="width: 100%">
				<el-table-column prop="ip" label="ip" width="180"></el-table-column>
				<el-table-column prop="tomcat" label="tomcat编号" width="180"></el-table-column>
				<el-table-column prop="name" label="项目名称"></el-table-column>
				<el-table-column prop="“batasite”" label="环境"></el-table-column>
				<el-table-column prop="“run”" label="操作">
					<ViewFroms></ViewFroms>
				</el-table-column>
			</el-table>
		</div>
	</div>
</template>

<script>
import ViewFroms from "@/components/view-froms.vue";
import ViewFromsAdd from "@/components/view-froms-add.vue";
import { getbyfrom } from '@/api/common.js';
export default {
	name: "the-page",
	
	components: {
		ViewFroms,
		ViewFromsAdd
	},

	filters: {},

	mixins: [],

	props: {},

	data() {
		
		return {
			// info :"",
			input: "",
			
			tableData: [
				{
					ip: "2016-05-02",
					tomcat: "王小虎",
					name:"namec"
				}
			]
		};
	},

	computed: {},

	watch: {},

	created() {
		this.getbyfrom()
		console.log(this.info+"12515")
		
	},

	mounted() {
		console.log(this.info+"12515")
	},

	methods: {
		getbyfrom(){
        getbyfrom({
          ipName:this.ipName
        })
        .then((data)=>{
          console.log(data.data.properties[0])
          this.tableData.push(data.data.properties[0])
        })
      },
		addItme() {
			this.tableData.push({
				date: "2016-05-02",
				name: this.input,
				address: this.address,
				dj: 1
			});
		}
	}
};
</script>

<style lang="scss" scoped>
.input-name {
	width: 100px;
}
.the-a {
	width: 100%;
	height: 60px;
	padding: 10px;

}
.the-b {
	width: 20%;
	height: 60px;
	padding: 10px;
	float:right 
}
</style>
