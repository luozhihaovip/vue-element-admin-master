import axios from 'axios'

export function setIpConfig(data){
  return axios({
    url:'/ipConfig/set',
    method:'post',
    data
  })
}

export function getbyfrom(data){
  return axios({
    url:'/mock/33062/ipConfig/getbyfrom',
    method:'post', 
    data
  })
}