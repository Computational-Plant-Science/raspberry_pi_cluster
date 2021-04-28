# ******************************
# These steps will allow you to install MPICH3 to your Raspbian Jessie distro
# Author: suxing liu
# Author-email: suxingliu@gmail.com
# ******************************

# update the system
sudo apt-get update

# update packages
sudo apt-get dist-upgrade

# create the folder for mpich3
sudo mkdir mpich3
cd ~/mpich3

# download the version 3.2 of mpich
sudo wget http://www.mpich.org/static/downloads/3.2/mpich-3.2.tar.gz

# unzip it
sudo tar xfz mpich-3.2.tar.gz

# create folders for mpi
sudo mkdir /home/rpimpi/
sudo mkdir /home/rpimpi/mpi-install
mkdir /home/pi/mpi-build

# install gfortran
sudo apt-get install gfortran

# configure and isntall mpich
sudo /home/pi/mpich3/mpich-3.2/configure -prefix=/home/rpimpi/mpi-install
sudo make
sudo make install

# edit the bash script using nano editor that runs everytime the Pi starts
cd ..
nano .bashrc

# Add the following to the end of the file
# PATH=$PATH:/home/rpimpi/mpi-install/bin
# to save the details press "CTRL + ^x" -> using CTRL 6 and x
# press "y" and hit enter to leave.

# Reboot the Pi
sudo reboot

# Test that MPI works
mpiexec -n 1 hostname



# ******************************
# These steps will allow you to install MPI4PY to your Raspbian Jessie distro
# ******************************

# download mpi4py
wget https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-2.0.0.tar.gz

#unzip the file
sudo tar -zxf mpi4py-2.0.0.tar.gz

# go to the directory
cd mpi4py-2.0.0

# install python-dev package
sudo aptitude install python-dev

# run the setup
python setup.py build
sudo python setup.py install

# Set the python path
export PYTHONPATH=/home/pi/mpi4py-2.0.0

# Test that MPI works on your device
mpiexec -n 5 python demo/helloworld.py

