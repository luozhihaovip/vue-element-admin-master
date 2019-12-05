<template>
	<div class="view-froms">
		<el-button type="text" @click="dialogFormVisible = true">打开嵌套表单的 Dialog</el-button>
		<el-dialog class="el-dialog__headers" title="新增项目:" :visible.sync="dialogFormVisible">
			<el-form :model="form">
				<el-form-item class="ef-from-items" label="ip:" :label-width="formLabelWidth">
					<el-input v-model="form.name" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item class="ef-from-items" label="tomcat编号:" :label-width="formLabelWidth">
					<el-input v-model="form.name" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item class="ef-from-items" label="项目名称:" :label-width="formLabelWidth">
					<el-input v-model="form.name" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item class="ef-from-items" label="环境:" :label-width="formLabelWidth">
					<el-select v-model="form.region" placeholder="请选择活动区域">
						<el-option label="beta环境" value="beta"></el-option>
						<el-option label="site环境" value="site"></el-option>
					</el-select>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click="dialogFormVisible = false">取 消</el-button>
				<el-button type="primary" @click="dialogFormadd">确 定</el-button>
			</div>
		</el-dialog>
	</div>
</template>

<script>
import { setIpConfig } from '@/api/common.js'
export default {
	name: "view-froms-add",

	components: {},

	filters: {},

	mixins: [],

	props: {},

	data() {
		return {
			dialogTableVisible: false,
			dialogFormVisible: false,
			form: {
				name: "1",
				region: "",
				date1: "",
				date2: "",
				delivery: false,
				type: [],
				resource: "",
				desc: ""
			},
			formLabelWidth: "120px"
		};
	},

	computed: {},

	watch: {},

	created() {},

	mounted() {},

	methods: {
		init() {},
		setIpConfig(){
        setIpConfig({
          ipName:this.ipName
        })
        .then((data)=>{
          console.log(data)
          debugger
        })
      },
		dialogFormadd() {
			console.log(name);
			this.setIpConfig();
		}
	}
};
</script>

<style lang="scss" scoped>
.el-dialog__headers {
	width: 80%;
}
.ef-from-items {
	width: 90%;
}
</style>
