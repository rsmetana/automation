import getpass
import sys
import telnetlib

user = raw_input('Enter your Creds: ')
password = getpass.getpass()

for i in range(2,40):
    HOST = '192.168.30.' + str(i)
    tn = telnetlib.Telnet(HOST)

    tn.read_until('Username: ')
    tn.write(user + '\n')
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
