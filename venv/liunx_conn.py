import paramiko
import os
class ParamikoHelper():

    def __init__(self,remote_ip, remote_ssh_port, ssh_password, ssh_username ):
        self.remote_ip = remote_ip
        self.remote_ssh_port = remote_ssh_port
        self.ssh_password = ssh_password
        self.ssh_username = ssh_username

    def connect_ssh(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.remote_ip, port=self.remote_ssh_port, username=self.ssh_username,
                             password=self.ssh_password)
        except Exception as e:
            print(e)
        return self.ssh

    def close_ssh(self):
        try:
            self.ssh.close()
        except Exception as e:
            print(e)

    def exec_shell(self, shell):
        ssh = self.connect_ssh()
        try:
            stdin, stdout, stderr = ssh.exec_command(shell)
            return stdin, stdout, stderr
        except Exception as e:
            print(e)

    def sftp_put_file(self, file, local_dir, remote_dir):
        try:
            t = paramiko.Transport((self.remote_ip, self.remote_ssh_port))
            t.connect(username=self.ssh_username, password=self.ssh_password)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put(os.path.join(local_dir, file), remote_dir)
            t.close()
        except Exception:
            print("connect error!")

    def sftp_get_file(self, file, local_dir, remote_dir):
        try:
            t = paramiko.Transport((self.remote_ip, self.remote_ssh_port))
            t.connect(username=self.ssh_username, password=self.ssh_password)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.get(remote_dir, os.path.join(local_dir, file))
            t.close()
        except Exception:
            print("connect error!")

def main():
    remote_ip = '10.55.253.75'
    remote_ssh_port = 22
    ssh_password = '!taiwu@345'
    ssh_username = 'root'
    ph = ParamikoHelper(remote_ip=remote_ip,remote_ssh_port=remote_ssh_port,ssh_password=ssh_password,ssh_username=ssh_username)
    star_time="2019-11-07 12:00"
    end_time="2019-11-07 15:00"
    tomcat="tomcat1026"
    # 远程执行ssh命令
    shell = " sed -n '/"+star_time+":/,/"+end_time+":/p' /usr/local/rsp/"+tomcat+"/logs/catalina.out > /usr/local/rsp/"+tomcat+"/webapps/log"
    print(shell)
    stdin, stdout, stderr = ph.exec_shell(shell)
    for line in stdout.readlines():
        print(line)
    ph.close_ssh()
    # 上传文件file2.txt到远程服务器上
    # file = 'file2.txt'
    # remote_dir = '/root/test_log/' + file
    # local_dir = os.getcwd()
    # ph.sftp_put_file(file=file, local_dir=local_dir, remote_dir=remote_dir)

    # 下载文件file3.txt
    # file = 'test3.txt'
    # remote_dir = '/usr/local/rsp/tomcat1046/logs/' + file
    # local_dir = os.getcwd()
    # ph.sftp_get_file(file=file, local_dir=local_dir, remote_dir=remote_dir)


if __name__ == '__main__':
    main()