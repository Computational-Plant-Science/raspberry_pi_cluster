#!/usr/bin/env sh

# This example creates a live stream of the camera.

# usage:
# ./live-stream.sh <serial of your camera>
# e.g.:
# ./live-stream.sh 51310104

# variables used to describe the video
WIDTH=1920
HEIGHT=1080
FPS=15/1
SERIAL=

# assure we have a serial number
if [ -z "$1" ]; then
    echo "please provide the serial number of the camera."
    exit 1
else
    SERIAL="$1"
fi

# the actual pipeline
gst-launch-1.0 \
    tcamsrc serial=${SERIAL} \
    ! video/x-bayer,width=$WIDTH,height=$HEIGHT,framerate=$FPS \
    ! bayer2rgb \
    ! videoconvert \
    ! autovideosink

# for mono images please use this pipeline instead

# gst-launch-1.0 \
#     tcamsrc serial=${SERIAL} \
#     ! video/x-raw,format=GRAY8,width=$WIDTH,height=$HEIGHT,framerate=$FPS \
#     ! videoconvert \
#     ! autovideosink

gst-launch-1.0 tcamsrc serial=12810399 ! videoconvert ! jpegenc ! filesink location=/home/pi/frame.jpg

gst-launch-1.0 tcamsrc serial=12810399 ! jpegenc ! multifilesink location=/home/pi/test/frame_%04d.jpg

gst-launch-1.0 tcambin ! video/x-raw, format=BGRA,width=3872,height=2764,framerate=3/1 ! videoconvert ! jpegenc ! multifilesink location=/home/pi/test/frame_%04d.jpg

gst-launch-1.0 tcambin serial=12810399 ! video/x-raw,format=BGRx,width=3872,height=2764,framerate=1/1 ! videoconvert ! jpegenc ! filesink location=/home/pi/frame.jpg

gst-launch-1.0 tcambin serial=12810399 ! video/x-raw,format=BGRx,width=3872,height=2764,framerate=1/1 ! jpegenc ! filesink location=/home/pi/frame.jpg

gst-launch-1.0 tcambin serial=12810399 num-buffer=1 ! video/x-raw,format=BGRx,width=3872,height=2764,framerate=1/1 ! jpegenc ! filesink location=/home/pi/frame.jpg




pyicmd put now supports copying folders with the -R flag:


pyicmd put -R [dir] [file(s) or folder(s)]

pip3 install -e git+https://github.com/cottersci/irods_python_client.git#egg=pyicmd --upgrade

pyicmd --host data.cyverse.org --port 1247 --user lsx1980 --passwd lsx6327903 --zone iplant put -R /iplant/home/lsx1980/root-images 2018-11-09



ssh-keygen

cd .ssh

cp id_rsa.pub pi09

scp 192.168.1.110:/home/pi/.ssh/PiController .

cat PiController>>authorized_keys

ls -la

exit





cd code/cam

scp 192.168.1.110:/home/pi/code/cam/*.py .





cd ~

cd .ssh

scp 192.168.1.101:/home/pi/.ssh/pi01 .

cat pi01>>authorized_keys

scp 192.168.1.102:/home/pi/.ssh/pi02 .

cat pi02>>authorized_keys

scp 192.168.1.103:/home/pi/.ssh/pi03 .

cat pi03>>authorized_keys

scp 192.168.1.104:/home/pi/.ssh/pi04 .

cat pi04>>authorized_keys

scp 192.168.1.105:/home/pi/.ssh/pi05 .

cat pi05>>authorized_keys

scp 192.168.1.106:/home/pi/.ssh/pi06 .

cat pi06>>authorized_keys

scp 192.168.1.107:/home/pi/.ssh/pi07 .

cat pi07>>authorized_keys

scp 192.168.1.108:/home/pi/.ssh/pi08 .

cat pi08>>authorized_keys

scp 192.168.1.109:/home/pi/.ssh/pi09 .

cat pi09>>authorized_keys



ls -la

exit




