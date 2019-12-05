import paramiko
class sss_con(self):
    def conn(self,ip):
        # 创建SSHClient实例对象
        ssh = paramiko.SSHClient()

        # 调用方法，表示没有存储远程机器的公钥，允许访问
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接远程机器：地址、端口、用户名、密码
        ssh.connect(ip, 22, 'root', '!taiwu@345')

        # 创建目录
        cmd = 'mkdir jcy2'
        ssh.exec_command(cmd)

        # 如果命令跨行
        # cmd = '''echo '1234
        # 5678
        # 90abc' > myfile
        # '''
        # ssh.exec_command(cmd)
        #
        # # 获取命令的执行结果
        cmd = 'cat myfile'
        stdin, stdout, stderr = ssh.exec_command(cmd)  # stdin-输入,stdout-输出,stderr-错误

        print(stdout.read() + stderr.read())  # 此时返回的是字节串，可加
        ssh.close()


if __name__ == '__main__':
    kk = sss_con()
    c=kk.conn('10.10.203.77')

