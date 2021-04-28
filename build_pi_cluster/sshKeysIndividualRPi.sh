# ******************************
# These steps will allow you to configure SSH on every device
# Author: suxing liu
# Author-email: suxingliu@gmail.com
# ******************************

# run this from PiController using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi01 using PuTTY
cd ~
cd .ssh
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi02 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi03 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi04 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi05 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi06 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi07 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi08 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.109:/home/pi/.ssh/pi09 .
cat pi09 >> authorized_keys

# run this from pi09 using PuTTY
cd ~
cd .ssh
scp 192.168.1.101:/home/pi/.ssh/pi01 .
cat pi01 >> authorized_keys
scp 192.168.1.102:/home/pi/.ssh/pi02 .
cat pi02 >> authorized_keys
scp 192.168.1.103:/home/pi/.ssh/pi03 .
cat pi03 >> authorized_keys
scp 192.168.1.104:/home/pi/.ssh/pi04 .
cat pi04 >> authorized_keys
scp 192.168.1.105:/home/pi/.ssh/pi05 .
cat pi05 >> authorized_keys
scp 192.168.1.106:/home/pi/.ssh/pi06 .
cat pi06 >> authorized_keys
scp 192.168.1.107:/home/pi/.ssh/pi07 .
cat pi07 >> authorized_keys
scp 192.168.1.108:/home/pi/.ssh/pi08 .
cat pi08 >> authorized_keys


# Inspect each authorized_keys file on each device and you will see the keys there for every device