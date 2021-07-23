import getpass
import sys
import telnetlib

user = input('Enter your Creds: ')
password = getpass.getpass()
third_octet = input('Enter the third octet of the subnet you are trying to manage: ')
single_or_mul = input('Are you trying to configure one or multiple devices? ')
if single_or_mul == 'one':
    single_ip = input('What is the 4th octet IP?')

    tn_one = telnetlib.Telnet(single_ip)
    tn.read_until('Username: ')
    tn.write(user + '\n')
    if password:
        tn.read_until("Password: ")
    tn.write(password + "\n")

elif single_or_mul == 'multiple' or 'mul':
    range_or_skips


for i in range(2,40):
    HOST = f'192.168.{third_octet}.' + str(i)
    tn = telnetlib.Telnet(HOST)
print(tn)

'''    tn.read_until('Username: ')
    tn.write(user + '\n')
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")'''
