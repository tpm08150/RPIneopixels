# RPIneopixels

#Clone github repository to RPI Desktop folder:

cd Desktop
git clone https://github.com/tpm08150/RPIneopixels.git

#Install pip:

sudo apt update
sudo apt install python3-setuptools git-core python3-dev


#Installation Instructions
Install Kivy from terminal:

pip3 install Kivy


#Install Kivy Dependencies:

sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev \
   xclip xsel libjpeg-dev
   
#Install Kivy for RPI Desktop Environment:

sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

#Install CircuitPython Libraries:

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel


