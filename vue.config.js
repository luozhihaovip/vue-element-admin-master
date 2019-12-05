// vue.config.js
var path = require('path')
function resolve (dir) {
  console.log(__dirname)
  return path.join(__dirname, dir)
}
module.exports = {
  // 选项...
  chainWebpack: config => {
    config.resolve.alias
      .set('@', resolve('src')) // key,value自行定义，比如.set('@@', resolve('src/components'))
  },
  devServer: {
    proxy: {
      '/mock': {
        target: 'http://yapi.demo.qunar.com',
        changeOrigin: true,
        pathRewrite: { 
          // '^/mock': ''
        }
      }
    }
  }
}