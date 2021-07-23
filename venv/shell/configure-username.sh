
#!/bin/bash
 # Collect the current user's ssh and enable passwords
 echo -n "Enter the username "
 echo -ne '\n'
 read -s -e username
 echo -n "Enter the SSH password  "
 read -s -e password
 echo -ne '\n'
# Feed the expect script a device list & the collected passwords
for device in `cat device-list.txt`; do
 ./configure-nortel.exp $device $username $password   ;
 done