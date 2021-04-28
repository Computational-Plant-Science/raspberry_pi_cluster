# ******************************
# These steps will allow you to configure SSH on every device
# Run the commands below from PiController device
# Author: suxing liu
# Author-email: suxingliu@gmail.com
# ******************************

# PiController (192.168.1.110)
ssh-keygen
cd ~
cd .ssh
cp id_rsa.pub PiController

# pi01 (192.168.1.101)

ssh pi@192.168.1.101
ssh-keygen
cd .ssh
cp id_rsa.pub pi01
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi02 192.168.1.102

ssh pi@192.168.1.102
ssh-keygen
cd .ssh
cp id_rsa.pub pi02
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi03 192.168.1.103

ssh pi@192.168.1.103
ssh-keygen
cd .ssh
cp id_rsa.pub pi03
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi04 192.168.1.104

ssh pi@192.168.1.104
ssh-keygen
cd .ssh
cp id_rsa.pub pi04
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi05 192.168.1.105

ssh pi@192.168.1.105
ssh-keygen
cd .ssh
cp id_rsa.pub pi05
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi06 192.168.1.106

ssh pi@192.168.1.106
ssh-keygen
cd .ssh
cp id_rsa.pub pi06
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi07 192.168.1.107

ssh pi@192.168.1.107
ssh-keygen
cd .ssh
cp id_rsa.pub pi07
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi08 192.168.1.108

ssh pi@192.168.1.108
ssh-keygen
cd .ssh
cp id_rsa.pub pi08
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit

# pi09 192.168.1.109

ssh pi@192.168.1.109
ssh-keygen
cd .ssh
cp id_rsa.pub pi09
scp 192.168.1.110:/home/pi/.ssh/PiController .
cat PiController >> authorized_keys
exit
