from fabric import Connection, Config
import getpass
import re
password = getpass.getpass("Enter your root password: ")
configure = Config(overrides={'sudo': {'password': password}})
conn = Connection(host="<IP>", user="ubuntu", connect_kwargs={"password": password}, config=configure)

#conn.run("sudo su -")
conn.sudo("apt update -y")
conn.sudo("apt install python3")
#conn.sudo("apt install net-tools")
ip_address = "<IP>"

desktop_path = "~/"

with conn.cd(desktop_path):
    conn.run("rm -rf test_folder")
    conn.run("mkdir test_folder")
    with conn.cd(desktop_path+"/test_folder"):
        conn.run("rm -rf *")
        conn.run('echo "Hello World From inside\
            the Ubuntu Terminal" > hello.txt')
        conn.run("cat hello.txt")
        conn.run(f'echo "Your IP Address is: {ip_address}" > ip.txt')
        conn.run("cat ip.txt")
