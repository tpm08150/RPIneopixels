# RPIneopixels

Note: you will need to connect your Data to GPIO pin 18 on the Raspberry Pi

**1. Clone github repository to RPI Desktop folder:**

cd Desktop

git clone https://github.com/tpm08150/RPIneopixels.git

**2. Install pip:**

sudo apt update
sudo apt install python3-setuptools git-core python3-dev


**3. Install Kivy:**

pip3 install Kivy


**4. Install Kivy Dependencies:**

sudo apt install pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   libgstreamer1.0-dev \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} libmtdev-dev \
   xclip xsel libjpeg-dev
   
**5. Install Kivy for RPI Desktop Environment:**

sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

**6. Install CircuitPython Libraries:**

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

**7. To run the program from the terminal:**

sudo -E python3 /home/pi/Desktop/RPIneopixels/piPixels1_0.py


