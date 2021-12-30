#!/usr/bin/env python3

# kivy_GPIO.py
# 2016-11-12
# Public Domain

# sudo apt-get install python-kivy python3-kivy


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
import time
import board
import neopixel
import RPi.GPIO as GPIO
import kivySaveFileDefault
from kivySaveFileDefault import *

Window.size = (1280, 1080)
s1 = 50
s2 = 100
note_on = 0
note_off = 0
track = 0

Builder.load_file('sliderR.kv')

# LED strip configuration:
LED_COUNT = int(input("number of LEDS: "))  # Number of LED pixels.
LED_PIN = board.D18  # GPIO pin
LED_BRIGHTNESS = 0.1  # LED brightness
LED_ORDER = neopixel.RGB  # order of LED colours. May also be RGB, GRBW, or RGBW
LED_ORDER2 = neopixel.GRB  # order of LED colours. May also be RGB, GRBW, or RGBW
# The colour selection selected for this project: red, blue, yellow, green, pink, and silver respectively


# Create NeoPixel object with appropriate configuration.
np = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset1 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset2 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset3 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset4 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset5 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset6 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset7 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset8 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset9 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset10 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset11 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset12 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset13 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset14 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset15 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset16 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset17 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset18 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset19 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset20 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset21 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset22 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset23 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset24 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset25 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset26 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset27 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset28 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset29 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset30 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset31 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset32 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset33 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset34 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset35 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset36 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset37 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset38 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset39 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset40 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset41 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset42 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset43 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset44 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset45 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset46 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset47 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset48 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset49 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset50 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset51 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset52 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset53 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset54 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset55 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset56 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset57 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset58 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset59 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset60 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset61 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset62 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset63 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)
preset64 = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=LED_ORDER)




x = 0
y = 0



# superCue1 = []
# superCue2 = []
# superCue3 = []
# superCue4 = []
# superCue5 = []
# superCue6 = []
# superCue7 = []
# superCue8 = []
# superCue9 = []
# superCue10 = []
# superCue11 = []
# superCue12 = []
# superCue13 = []
# superCue14 = []
# superCue15 = []
# superCue16 = []

superCueList = [superCue1, superCue2, superCue3, superCue4, superCue5, superCue6, superCue7, superCue8,
                superCue9, superCue10, superCue11, superCue12, superCue13, superCue14, superCue15, superCue16]
presetList = [preset1, preset2, preset3, preset4, preset5, preset6, preset7, preset8, preset9, preset10, preset11, preset12, preset13, preset14, preset15, preset16,
              preset17, preset18, preset19, preset20, preset21, preset22, preset23, preset24, preset25, preset26, preset27, preset28, preset29, preset30, preset31, preset32,
              preset33, preset34, preset35, preset36, preset37, preset38, preset39, preset40, preset41, preset42, preset43, preset44, preset45, preset46, preset47, preset48,
              preset49, preset50, preset51, preset52, preset53, preset54, preset55, preset56, preset57, preset58, preset59, preset60, preset61, preset62, preset63, preset64]

# programCue1 = []
# programCue2 = []
# programCue3 = []
# programCue4 = []
# programCue5 = []
# programCue6 = []
# programCue7 = []
# programCue8 = []

programCueList = [programCue1, programCue2, programCue3, programCue4, programCue5, programCue6, programCue7, programCue8]

# group1 = [0,0]
# group2 = [0,0]
# group3 = [0,0]
# group4 = [0,0]
# group5 = [0,0]
# group6 = [0,0]
# group7 = [0,0]
# group8 = [0,0]
# group9 = [0,0]
# group10 = [0,0]
# group11 = [0,0]
# group12 = [0,0]
# group13 = [0,0]
# group14 = [0,0]
# group15 = [0,0]
# group16 = [0,0]
# group17 = [0,0]
# group18 = [0,0]
# group19 = [0,0]
# group20 = [0,0]
# group21 = [0,0]
# group22 = [0,0]
# group23 = [0,0]
# group24 = [0,0]
# group25 = [0,0]
# group26 = [0,0]
# group27 = [0,0]
# group28 = [0,0]
# group29 = [0,0]
# group30 = [0,0]
# group31 = [0,0]
# group32 = [0,0]
# group33 = [0,0]
# group34 = [0,0]
# group35 = [0,0]
# group36 = [0,0]
# group37 = [0,0]
# group38 = [0,0]
# group39 = [0,0]
# group40 = [0,0]
# group41 = [0,0]
# group42 = [0,0]
# group43 = [0,0]
# group44 = [0,0]
# group45 = [0,0]
# group46 = [0,0]
# group47 = [0,0]
# group48 = [0,0]
# group49 = [0,0]
# group50 = [0,0]
# group51 = [0,0]
# group52 = [0,0]
# group53 = [0,0]
# group54 = [0,0]
# group55 = [0,0]
# group56 = [0,0]
# group57 = [0,0]
# group58 = [0,0]
# group59 = [0,0]
# group60 = [0,0]
# group61 = [0,0]
# group62 = [0,0]
# group63 = [0,0]
# group64 = [0,0]

groupList = [group1, group2, group3, group4, group5, group6, group7, group8,
             group9, group10, group11, group12, group13, group14, group15, group16,
             group17, group18, group19, group20, group21, group22, group23, group24,
             group25, group26, group27, group28, group29, group30, group31, group32,
             group33, group34, group35, group36, group37, group38, group39, group40,
             group41, group42, group43, group44, group45, group46, group47, group48,
             group49, group50, group51, group52, group53, group54, group55, group56,
             group57, group58, group59, group60, group61, group62, group63, group64]
# groupNamesList = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6', 'Group 7', 'Group 8',
#                   'Group 9', 'Group 10', 'Group 11', 'Group 12', 'Group 13', 'Group 14', 'Group 15', 'Group 16',
#                   'Group 17', 'Group 18', 'Group 19', 'Group 20', 'Group 21', 'Group 22', 'Group 23', 'Group 24',
#                   'Group 25', 'Group 26', 'Group 27', 'Group 28', 'Group 29', 'Group 30', 'Group 31', 'Group 32',
#                   'Group 33', 'Group 34', 'Group 35', 'Group 36', 'Group 37', 'Group 38', 'Group 39', 'Group 40',
#                   'Group 41', 'Group 42', 'Group 43', 'Group 44', 'Group 45', 'Group 46', 'Group 47', 'Group 48',
#                   'Group 49', 'Group 50', 'Group 51', 'Group 52', 'Group 53', 'Group 54', 'Group 55', 'Group 56',
#                   'Group 57', 'Group 58', 'Group 59', 'Group 60', 'Group 61', 'Group 62', 'Group 63', 'Group 64',]

group = 0
saveGroup = 0
selectGroup = 0
nameGroup = 0

copy = []
paste = []

copyList = [copy,paste]

z = 0
y = 0
x = 0
t = 0

play = 0
key = 0
seqLen = 16
notes = 's'
master = 0
speed = 1/8

brightness = 0
brightnessWeight = 1

Rcolor = 0
Rslider = 0
r = 0
rS = 0
Gcolor = 0
g = 0
Bcolor = 0
b = 0
d = 0
pixelLow = 1
pixelHigh = LED_COUNT
setPixel = 0
c = 0
sC = 0
sR = 0
pC = 0
pR = 0
p = 0
sM = 1
pM = 0
RGB = 0
skip = 0

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 125, 0)
yellow = (255,255,0)
purple = (125, 0 , 255)
black = (0, 0, 0)

presetCall1 = 0

color = 0

# color1 = (0, 0, 0)
# color2 = (0, 0, 0)
# color3 = (0, 0, 0)
# color4 = (0, 0, 0)
# color5 = (0, 0, 0)
# color6 = (0, 0, 0)
# color7 = (0, 0, 0)
# color8 = (0, 0, 0)
colorBlank = (0, 0, 0)
# color9 = (0, 0, 0)
# color10 = (0, 0, 0)
# color11 = (0, 0, 0)
# color12 = (0, 0, 0)
# color13 = (0, 0, 0)
# color14 = (0, 0, 0)
# color15 = (0, 0, 0)
# color16 = (0, 0, 0)

colorList = [color1, color2, color3, color4, color5, color6, color7, color8, colorBlank,
             color9, color10, color11, color12, color13, color14, color15, color16]


def superCueRecording():
    global x
    global cue
    x = 0
    for i in superCueList:
        if sR % 2 == 1 and sC == x:
            superCueList[x].append(cue)
            if superCueList[x][0] == 10:
                superCueList[x].pop(0)
        x += 1
    presetList[cue - 1].show()

x = 0
def programCueRecording():
    global x
    global sC
    global cue
    x = 0
    for i in programCueList:
        if pR % 2 == 1 and pC == x:
            programCueList[x].append(sC)
            print(programCueList[x])
            if programCueList[x][0] == 10:
                programCueList[x].pop(0)
        x += 1
    presetList[cue - 1].show()

def presetLoad():
    global x
    global y
    x = 0
    for preset in presetSaveList:
        y = 0
        for pixel in presetList[x]:
            presetList[x]._set_item(y,presetSaveList[x][y][0],presetSaveList[x][y][1],presetSaveList[x][y][2],0)
            y += 1
        x += 1

presetLoad()

sliderStop = 0

saveColorList = 0
clNumber = 0
cl = 0
color1List = [black]
color2List = [black]
color3List = [black]
color4List = [black]
color5List = [black]
color6List = [black]
color7List = [black]
color8List = [black]

colorLists = [color1List, color2List, color3List, color4List, color5List, color6List, color7List, color8List]

groupNameList = []

e1 = 0

RGBlist = [(0, 0, 0)]

save = 0
cue = 0


class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        global x
        global z
        super(MyLayout, self).__init__(**kwargs)

        self.cols = 1
        self.z = 40

        self.textGrid = GridLayout()
        self.textGrid.cols = 6
        self.textGrid.padding = 4
        self.textGrid.spacing = 2
        self.textGrid.size_hint_y = 1
        self.add_widget(self.textGrid)

        self.RGBinputRed = TextInput(multiline=False, size_hint_x=0.2, font_size=14)
        self.textGrid.add_widget(self.RGBinputRed)

        self.RGBinputGreen = TextInput(multiline=False, size_hint_x=0.2, font_size=14)
        self.textGrid.add_widget(self.RGBinputGreen)

        self.RGBinputBlue = TextInput(multiline=False, size_hint_x=0.2, font_size=14)
        self.textGrid.add_widget(self.RGBinputBlue)
        
        self.RGBbrightness = TextInput(multiline=False, size_hint_x=0.1, font_size=14)
        self.textGrid.add_widget(self.RGBbrightness)
        
        self.RGBbrightnessWeight = TextInput(text= "100", multiline=False, size_hint_x=0.1, font_size=14)
        self.textGrid.add_widget(self.RGBbrightnessWeight)
        
        self.RGBspeed = TextInput(multiline=False, size_hint_x=0.2, font_size=14)
        self.textGrid.add_widget(self.RGBspeed)

        self.pixelGrid = GridLayout()
        self.pixelGrid.cols = 10
        self.pixelGrid.padding = 4
        self.pixelGrid.spacing = 2
        self.pixelGrid.size_hint_y = 1
        self.add_widget(self.pixelGrid)
        
        
#         self.loadFileButton = Button(text='Load File', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
#         self.pixelGrid.add_widget(self.loadFileButton)
#         self.loadFileButton.bind(on_press=self.loadFile)

        self.setRangeButton = Button(text='Set Pixels', background_color='gray', size_hint_x=0.16, size_hint_y=0.1)
        self.pixelGrid.add_widget(self.setRangeButton)
        self.setRangeButton.bind(on_press=self.setRange)

        self.pixelLow = TextInput(multiline=False, font_size=14, size_hint_x=0.16, size_hint_y=0.2)
        self.pixelGrid.add_widget(self.pixelLow)

        self.pixelHigh = TextInput(multiline=False, font_size=14, size_hint_x=0.16, size_hint_y=0.2)
        self.pixelGrid.add_widget(self.pixelHigh)
        
        self.saveFileButton = Button(text='Save File', background_color='gray', size_hint_x=0.1, size_hint_y=0.1)
        self.pixelGrid.add_widget(self.saveFileButton)
        self.saveFileButton.bind(on_press=self.saveFile)
        
        self.RGBPixelsButton = Button(text='RGB', background_color='gray', size_hint_x=0.04, size_hint_y=0.1)
        self.pixelGrid.add_widget(self.RGBPixelsButton)
        self.RGBPixelsButton.bind(on_press=self.RGBPixels)
        
        self.GRBPixelsButton = Button(text='GRB', background_color='gray', size_hint_x=0.04, size_hint_y=0.1)
        self.pixelGrid.add_widget(self.GRBPixelsButton)
        self.GRBPixelsButton.bind(on_press=self.GRBPixels)
        
        self.BGRPixelsButton = Button(text='BGR', background_color='gray', size_hint_x=0.04, size_hint_y=0.1)
        self.pixelGrid.add_widget(self.BGRPixelsButton)
        self.BGRPixelsButton.bind(on_press=self.BGRPixels)
        
#         self.setPixelCount = Button(text='Ttl Pxls', background_color='gray', size_hint_x=0.04, size_hint_y=0.1)
#         self.pixelGrid.add_widget(self.setPixelCount)
#         self.setPixelCount.bind(on_press=self.setPixelAmount)
        
        self.pixelCountText = TextInput(text = f"{LED_COUNT}", multiline=False, font_size=14, size_hint_x=0.04, size_hint_y=0.1)
        self.pixelGrid.add_widget(self.pixelCountText)
        
        self.skip1Pixel = Button(text='skp 1p', background_color='gray', size_hint_x=0.04, size_hint_y=0.1)
        self.pixelGrid.add_widget(self.skip1Pixel)
        self.skip1Pixel.bind(on_press=self.skip1P)
        
        self.groupControlGrid = GridLayout()
        self.groupControlGrid.cols = 5
        self.groupControlGrid.padding = 4
        self.groupControlGrid.spacing = 2
        self.add_widget(self.groupControlGrid)  
        
        self.saveGroupButton = Button(text='Save Group', background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.groupControlGrid.add_widget(self.saveGroupButton)
        self.saveGroupButton.bind(on_press=self.saveGroup)
        
        self.groupOnButton = Button(text='Group Off', background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.groupControlGrid.add_widget(self.groupOnButton)
        self.groupOnButton.bind(on_press=self.groupOn)
        
        self.nameGroupButton = Button(text='Click to Name Selected Group', background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.groupControlGrid.add_widget(self.nameGroupButton)
        self.nameGroupButton.bind(on_press=self.nameGroup)
        
        self.nameGroupText = TextInput(multiline=False, font_size=14, size_hint=(.3, .25))
        self.groupControlGrid.add_widget(self.nameGroupText)
        
        self.saveClearButton = Button(text='Clear Group', background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.groupControlGrid.add_widget(self.saveClearButton)
        self.saveClearButton.bind(on_press=self.clearGroup)

        self.groupGrid = GridLayout()
        self.groupGrid.cols = 8
        self.groupGrid.padding = 4
        self.groupGrid.spacing = 2
        self.add_widget(self.groupGrid)
        
        self.group1Button = Button(text=groupNamesList[0], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group2Button = Button(text=groupNamesList[1], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group3Button = Button(text=groupNamesList[2], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group4Button = Button(text=groupNamesList[3], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group5Button = Button(text=groupNamesList[4], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group6Button = Button(text=groupNamesList[5], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group7Button = Button(text=groupNamesList[6], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group8Button = Button(text=groupNamesList[7], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group9Button = Button(text=groupNamesList[8], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group10Button = Button(text=groupNamesList[9], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group11Button = Button(text=groupNamesList[10], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group12Button = Button(text=groupNamesList[11], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group13Button = Button(text=groupNamesList[12], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group14Button = Button(text=groupNamesList[13], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group15Button = Button(text=groupNamesList[14], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group16Button = Button(text=groupNamesList[15], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        
        
        groupButtonList = [self.group1Button, self.group2Button, self.group3Button, self.group4Button,
                           self.group5Button, self.group6Button, self.group7Button, self.group8Button,
                           self.group9Button, self.group10Button, self.group11Button, self.group12Button,
                           self.group13Button, self.group14Button, self.group15Button, self.group16Button]
        groupFunctionList = [self.group1, self.group2, self.group3, self.group4,
                             self.group5, self.group6, self.group7, self.group8,
                             self.group9, self.group10, self.group11, self.group12,
                             self.group13, self.group14, self.group15, self.group16]
        #groupTextList = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
        

        x = 0
        for i in groupButtonList:

            self.groupGrid.add_widget(groupButtonList[x])
            groupButtonList[x].bind(on_press=groupFunctionList[x])

            x += 1
        
        self.groupGrid2 = GridLayout()
        self.groupGrid2.cols = 8
        self.groupGrid2.padding = 4
        self.groupGrid2.spacing = 2
        self.add_widget(self.groupGrid2)
            
        self.group17Button = Button(text=groupNamesList[16], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group18Button = Button(text=groupNamesList[17], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group19Button = Button(text=groupNamesList[18], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group20Button = Button(text=groupNamesList[19], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group21Button = Button(text=groupNamesList[20], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group22Button = Button(text=groupNamesList[21], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group23Button = Button(text=groupNamesList[22], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group24Button = Button(text=groupNamesList[23], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group25Button = Button(text=groupNamesList[24], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group26Button = Button(text=groupNamesList[25], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group27Button = Button(text=groupNamesList[26], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group28Button = Button(text=groupNamesList[27], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group29Button = Button(text=groupNamesList[28], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group30Button = Button(text=groupNamesList[29], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group31Button = Button(text=groupNamesList[20], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group32Button = Button(text=groupNamesList[31], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        
                
        groupButtonList2 = [self.group17Button, self.group18Button, self.group19Button, self.group20Button,
                           self.group21Button, self.group22Button, self.group23Button, self.group24Button,
                           self.group25Button, self.group26Button, self.group27Button, self.group28Button,
                           self.group29Button, self.group30Button, self.group31Button, self.group32Button]
        groupFunctionList2 = [self.group17, self.group18, self.group19, self.group20,
                             self.group21, self.group22, self.group23, self.group24,
                             self.group25, self.group26, self.group27, self.group28,
                             self.group29, self.group30, self.group31, self.group32]
        #groupTextList = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
        
        x = 0
        for i in groupButtonList2:
            self.groupGrid2.add_widget(groupButtonList2[x])
            groupButtonList2[x].bind(on_press=groupFunctionList2[x])
            x += 1
            
            
        
        self.groupGrid3 = GridLayout()
        self.groupGrid3.cols = 8
        self.groupGrid3.padding = 4
        self.groupGrid3.spacing = 2
        self.add_widget(self.groupGrid3)
            
        self.group33Button = Button(text=groupNamesList[32], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group34Button = Button(text=groupNamesList[33], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group35Button = Button(text=groupNamesList[34], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group36Button = Button(text=groupNamesList[35], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group37Button = Button(text=groupNamesList[36], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group38Button = Button(text=groupNamesList[37], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group39Button = Button(text=groupNamesList[38], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group40Button = Button(text=groupNamesList[39], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group41Button = Button(text=groupNamesList[40], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group42Button = Button(text=groupNamesList[41], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group43Button = Button(text=groupNamesList[42], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group44Button = Button(text=groupNamesList[43], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group45Button = Button(text=groupNamesList[44], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group46Button = Button(text=groupNamesList[45], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group47Button = Button(text=groupNamesList[46], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group48Button = Button(text=groupNamesList[47], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        
                
        groupButtonList3 = [self.group33Button, self.group34Button, self.group35Button, self.group36Button,
                           self.group37Button, self.group38Button, self.group39Button, self.group40Button,
                           self.group41Button, self.group42Button, self.group43Button, self.group44Button,
                           self.group45Button, self.group46Button, self.group47Button, self.group48Button]
        groupFunctionList3 = [self.group33, self.group34, self.group35, self.group36,
                             self.group37, self.group38, self.group39, self.group40,
                             self.group41, self.group42, self.group43, self.group44,
                             self.group45, self.group46, self.group47, self.group48]
        #groupTextList = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
        
        x = 0
        for i in groupButtonList3:
            self.groupGrid3.add_widget(groupButtonList3[x])
            groupButtonList3[x].bind(on_press=groupFunctionList3[x])
            x += 1
            
            
            
        self.groupGrid4 = GridLayout()
        self.groupGrid4.cols = 8
        self.groupGrid4.padding = 4
        self.groupGrid4.spacing = 2
        self.add_widget(self.groupGrid4)
            
        self.group49Button = Button(text=groupNamesList[48], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group50Button = Button(text=groupNamesList[49], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group51Button = Button(text=groupNamesList[50], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group52Button = Button(text=groupNamesList[51], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group53Button = Button(text=groupNamesList[52], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group54Button = Button(text=groupNamesList[53], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group55Button = Button(text=groupNamesList[54], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group56Button = Button(text=groupNamesList[55], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group57Button = Button(text=groupNamesList[56], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group58Button = Button(text=groupNamesList[57], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group59Button = Button(text=groupNamesList[58], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group60Button = Button(text=groupNamesList[59], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group61Button = Button(text=groupNamesList[60], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group62Button = Button(text=groupNamesList[61], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group63Button = Button(text=groupNamesList[62], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.group64Button = Button(text=groupNamesList[63], background_color='gray', size_hint=(.3, .25), pos=(0, 1))
    
                
        groupButtonList4 = [self.group49Button, self.group50Button, self.group51Button, self.group52Button,
                           self.group53Button, self.group54Button, self.group55Button, self.group56Button,
                           self.group57Button, self.group58Button, self.group59Button, self.group60Button,
                           self.group61Button, self.group62Button, self.group63Button, self.group64Button]
        groupFunctionList4 = [self.group49, self.group50, self.group51, self.group52,
                             self.group53, self.group54, self.group55, self.group56,
                             self.group57, self.group58, self.group59, self.group60,
                             self.group61, self.group62, self.group63, self.group64]
        #groupTextList = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
        
        x = 0
        for i in groupButtonList4:
            self.groupGrid4.add_widget(groupButtonList4[x])
            groupButtonList4[x].bind(on_press=groupFunctionList4[x])
            x += 1


        self.colorGrid = GridLayout()
        self.colorGrid.cols = 9
        self.colorGrid.padding = 4
        self.colorGrid.spacing = 2
        self.add_widget(self.colorGrid)
                   
        self.color1Button = Button(text='Color 1', background_color='gray', background_normal='', size_hint=(.3, .25), pos=(0, 1))
        self.color2Button = Button(text='Color 2', background_color='gray', background_normal='', size_hint=(.3, .25), pos=(0, 1))
        self.color3Button = Button(text='Color 3', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color4Button = Button(text='Color 4', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color5Button = Button(text='Color 5', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color6Button = Button(text='Color 6', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color7Button = Button(text='Color 7', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color8Button = Button(text='Color 8', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.colorBlankButton = Button(text='', background_color='black', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color9Button = Button(text='Color 9', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color10Button = Button(text='Color 10', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color11Button = Button(text='Color 11', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color12Button = Button(text='Color 12', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color13Button = Button(text='Color 13', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color14Button = Button(text='Color 14', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color15Button = Button(text='Color 15', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
        self.color16Button = Button(text='Color 16', background_color='gray', background_normal='',size_hint=(.3, .25), pos=(0, 1))
       
        colorButtonList1 = [self.color1Button, self.color2Button, self.color3Button, self.color4Button,
                           self.color5Button, self.color6Button, self.color7Button, self.color8Button, self.colorBlankButton,
                           self.color9Button, self.color10Button, self.color11Button, self.color12Button,
                           self.color13Button, self.color14Button, self.color15Button, self.color16Button]
        colorFunctionList1 = [self.color1, self.color2, self.color3, self.color4,
                             self.color5, self.color6, self.color7, self.color8, self.colorBlank,
                             self.color9, self.color10, self.color11, self.color12,
                             self.color13, self.color14, self.color15, self.color16]
        
        x = 0
        for i in colorButtonList1:
            self.colorGrid.add_widget(colorButtonList1[x])
            colorButtonList1[x].bind(on_press=colorFunctionList1[x])
            x += 1

        self.saveButton = Button(text='Save Color', background_color='gray', size_hint=(.3, .25), pos=(0, 1))
        self.colorGrid.add_widget(self.saveButton)
        self.saveButton.bind(on_press=self.saveColor)


        # transport buttons
        self.transportGrid = GridLayout()
        self.transportGrid.cols = 8
        self.transportGrid.padding = 4
        self.transportGrid.spacing = 2
        self.add_widget(self.transportGrid)

        self.playButton = Button(text='Play', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
        self.transportGrid.add_widget(self.playButton)
        self.playButton.bind(on_press=self.play)

        self.copyButton = Button(text='Copy', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
        self.transportGrid.add_widget(self.copyButton)
        self.copyButton.bind(on_press=self.clear)

        self.clearButton = Button(text='Clear Cue', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
        self.transportGrid.add_widget(self.clearButton)
        self.clearButton.bind(on_press=self.clear)
        
        self.superModeButton = Button(text='Super Mode', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
        self.transportGrid.add_widget(self.superModeButton)
        self.superModeButton.bind(on_press=self.superMode)
        
        self.programModeButton = Button(text='Program Mode', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
        self.transportGrid.add_widget(self.programModeButton)
        self.programModeButton.bind(on_press=self.programMode)

        # step buttons

        self.cueGrid = GridLayout()
        self.cueGrid.cols = 8
        self.cueGrid.padding = 4
        self.cueGrid.spacing = 2
        self.add_widget(self.cueGrid)
                   
        self.cue1Button = Button(text='Cue 1', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue2Button = Button(text='Cue 2', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue3Button = Button(text='Cue 3', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue4Button = Button(text='Cue 4', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue5Button = Button(text='Cue 5', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue6Button = Button(text='Cue 6', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue7Button = Button(text='Cue 7', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue8Button = Button(text='Cue 8', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue9Button = Button(text='Cue 9', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue10Button = Button(text='Cue 10', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue11Button = Button(text='Cue 11', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue12Button = Button(text='Cue 12', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue13Button = Button(text='Cue 13', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue14Button = Button(text='Cue 14', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue15Button = Button(text='Cue 15', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue16Button = Button(text='Cue 16', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
       
        cueButtonList1 = [self.cue1Button, self.cue2Button, self.cue3Button, self.cue4Button,
                           self.cue5Button, self.cue6Button, self.cue7Button, self.cue8Button,
                           self.cue9Button, self.cue10Button, self.cue11Button, self.cue12Button,
                           self.cue13Button, self.cue14Button, self.cue15Button, self.cue16Button]
        cueFunctionList1 = [self.cue1, self.cue2, self.cue3, self.cue4,
                             self.cue5, self.cue6, self.cue7, self.cue8,
                             self.cue9, self.cue10, self.cue11, self.cue12,
                             self.cue13, self.cue14, self.cue15, self.cue16]
        
        x = 0
        for i in cueButtonList1:

            self.cueGrid.add_widget(cueButtonList1[x])
            cueButtonList1[x].bind(on_press=cueFunctionList1[x])

            x += 1
        
        self.cueGrid2 = GridLayout()
        self.cueGrid2.cols = 8
        self.cueGrid2.padding = 4
        self.cueGrid2.spacing = 2
        self.add_widget(self.cueGrid2)
             
        self.cue17Button = Button(text='Cue 17', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue18Button = Button(text='Cue 18', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue19Button = Button(text='Cue 19', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue20Button = Button(text='Cue 20', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue21Button = Button(text='Cue 21', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue22Button = Button(text='Cue 22', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue23Button = Button(text='Cue 23', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue24Button = Button(text='Cue 24', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue25Button = Button(text='Cue 25', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue26Button = Button(text='Cue 26', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue27Button = Button(text='Cue 27', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue28Button = Button(text='Cue 28', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue29Button = Button(text='Cue 29', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue30Button = Button(text='Cue 30', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue31Button = Button(text='Cue 31', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue32Button = Button(text='Cue 32', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
       
        cueButtonList2 = [self.cue17Button, self.cue18Button, self.cue19Button, self.cue20Button,
                           self.cue21Button, self.cue22Button, self.cue23Button, self.cue24Button,
                           self.cue25Button, self.cue26Button, self.cue27Button, self.cue28Button,
                           self.cue29Button, self.cue30Button, self.cue31Button, self.cue32Button]
        cueFunctionList2 = [self.cue17, self.cue18, self.cue19, self.cue20,
                             self.cue21, self.cue22, self.cue23, self.cue24,
                             self.cue25, self.cue26, self.cue27, self.cue28,
                             self.cue29, self.cue30, self.cue31, self.cue32]
        
        x = 0
        for i in cueButtonList2:

            self.cueGrid2.add_widget(cueButtonList2[x])
            cueButtonList2[x].bind(on_press=cueFunctionList2[x])

            x += 1
        
        self.cueGrid3 = GridLayout()
        self.cueGrid3.cols = 8
        self.cueGrid3.padding = 4
        self.cueGrid3.spacing = 2
        self.add_widget(self.cueGrid3)

        self.cue33Button = Button(text='Cue 33', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue34Button = Button(text='Cue 34', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue35Button = Button(text='Cue 35', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue36Button = Button(text='Cue 36', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue37Button = Button(text='Cue 37', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue38Button = Button(text='Cue 38', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue39Button = Button(text='Cue 39', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue40Button = Button(text='Cue 40', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue41Button = Button(text='Cue 41', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue42Button = Button(text='Cue 42', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue43Button = Button(text='Cue 43', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue44Button = Button(text='Cue 44', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue45Button = Button(text='Cue 45', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue46Button = Button(text='Cue 46', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue47Button = Button(text='Cue 47', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue48Button = Button(text='Cue 48', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
       
        cueButtonList3 = [self.cue33Button, self.cue34Button, self.cue35Button, self.cue36Button,
                           self.cue37Button, self.cue38Button, self.cue39Button, self.cue40Button,
                           self.cue41Button, self.cue42Button, self.cue43Button, self.cue44Button,
                           self.cue45Button, self.cue46Button, self.cue47Button, self.cue48Button]
        cueFunctionList3 = [self.cue33, self.cue34, self.cue35, self.cue36,
                             self.cue37, self.cue38, self.cue39, self.cue40,
                             self.cue41, self.cue42, self.cue43, self.cue44,
                             self.cue45, self.cue46, self.cue47, self.cue48]
        
        x = 0
        for i in cueButtonList3:

            self.cueGrid3.add_widget(cueButtonList3[x])
            cueButtonList3[x].bind(on_press=cueFunctionList3[x])

            x += 1
        
        self.cueGrid4 = GridLayout()
        self.cueGrid4.cols = 8
        self.cueGrid4.padding = 4
        self.cueGrid4.spacing = 2
        self.add_widget(self.cueGrid4)
        
        self.cue49Button = Button(text='Cue 49', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue50Button = Button(text='Cue 50', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue51Button = Button(text='Cue 51', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue52Button = Button(text='Cue 52', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue53Button = Button(text='Cue 53', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue54Button = Button(text='Cue 54', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue55Button = Button(text='Cue 55', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue56Button = Button(text='Cue 56', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue57Button = Button(text='Cue 57', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue58Button = Button(text='Cue 58', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue59Button = Button(text='Cue 59', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue60Button = Button(text='Cue 60', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue61Button = Button(text='Cue 61', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue62Button = Button(text='Cue 62', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue63Button = Button(text='Cue 63', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
        self.cue64Button = Button(text='Cue 64', background_color='gray', size_hint=(.3, 1), pos=(0, 35))
       
        cueButtonList4 = [self.cue49Button, self.cue50Button, self.cue51Button, self.cue52Button,
                           self.cue53Button, self.cue54Button, self.cue55Button, self.cue56Button,
                           self.cue57Button, self.cue58Button, self.cue59Button, self.cue60Button,
                           self.cue61Button, self.cue62Button, self.cue63Button, self.cue64Button]
        cueFunctionList4 = [self.cue49, self.cue50, self.cue51, self.cue52,
                             self.cue53, self.cue54, self.cue55, self.cue56,
                             self.cue57, self.cue58, self.cue59, self.cue60,
                             self.cue61, self.cue62, self.cue63, self.cue64]
        
        x = 0
        for i in cueButtonList4:

            self.cueGrid4.add_widget(cueButtonList4[x])
            cueButtonList4[x].bind(on_press=cueFunctionList4[x])

            x += 1


        self.superCueGrid = GridLayout()
        self.superCueGrid.cols = 10
        self.superCueGrid.padding = 4
        self.superCueGrid.spacing = 2
        self.add_widget(self.superCueGrid)

        self.superCueRecButton = Button(text='Super Cue Record', background_color='gray', size_hint=(.3, .1),
                                        pos=(0, 35))
        self.superCueGrid.add_widget(self.superCueRecButton)
        self.superCueRecButton.bind(on_press=self.superRecord)

        self.superCueClearButton = Button(text='Super Cue Clear', background_color='gray', size_hint=(.3, .1),
                                          pos=(0, 35))
        self.superCueGrid.add_widget(self.superCueClearButton)
        self.superCueClearButton.bind(on_press=self.superClear)

        self.superCue1Button = Button(text='Super Cue 1', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue1Button)
        self.superCue1Button.bind(on_press=self.superCue1)

        self.superCue2Button = Button(text='Super Cue 2', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue2Button)
        self.superCue2Button.bind(on_press=self.superCue2)

        self.superCue3Button = Button(text='Super Cue 3', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue3Button)
        self.superCue3Button.bind(on_press=self.superCue3)

        self.superCue4Button = Button(text='Super Cue 4', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue4Button)
        self.superCue4Button.bind(on_press=self.superCue4)

        self.superCue5Button = Button(text='Super Cue 5', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue5Button)
        self.superCue5Button.bind(on_press=self.superCue5)

        self.superCue6Button = Button(text='Super Cue 6', background_color='gray', size_hint=(.3, .1,), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue6Button)
        self.superCue6Button.bind(on_press=self.superCue6)

        self.superCue7Button = Button(text='Super Cue 7', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue7Button)
        self.superCue7Button.bind(on_press=self.superCue7)

        self.superCue8Button = Button(text='Super Cue 8', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue8Button)
        self.superCue8Button.bind(on_press=self.superCue8)
        
        self.superBlank1Button = Button(text='', background_color='black', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superBlank1Button)
        
        self.superBlank1Button = Button(text='', background_color='black', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superBlank1Button)

        
        self.superCue9Button = Button(text='Super Cue 9', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue9Button)
        self.superCue9Button.bind(on_press=self.superCue9)

        self.superCue10Button = Button(text='Super Cue 10', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue10Button)
        self.superCue10Button.bind(on_press=self.superCue10)

        self.superCue11Button = Button(text='Super Cue 11', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue11Button)
        self.superCue11Button.bind(on_press=self.superCue11)

        self.superCue12Button = Button(text='Super Cue 12', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue12Button)
        self.superCue12Button.bind(on_press=self.superCue12)

        self.superCue13Button = Button(text='Super Cue 13', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue13Button)
        self.superCue13Button.bind(on_press=self.superCue13)

        self.superCue14Button = Button(text='Super Cue 14', background_color='gray', size_hint=(.3, .1,), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue14Button)
        self.superCue14Button.bind(on_press=self.superCue14)

        self.superCue15Button = Button(text='Super Cue 15', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue15Button)
        self.superCue15Button.bind(on_press=self.superCue15)

        self.superCue16Button = Button(text='Super Cue 16', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.superCueGrid.add_widget(self.superCue16Button)
        self.superCue16Button.bind(on_press=self.superCue16)
        
        self.programCueGrid = GridLayout()
        self.programCueGrid.cols = 10
        self.programCueGrid.padding = 4
        self.programCueGrid.spacing = 2
        self.add_widget(self.programCueGrid)

        self.programCueRecButton = Button(text='program Cue \n   Record', background_color='gray', size_hint=(.3, .1),
                                        pos=(0, 35))
        self.programCueGrid.add_widget(self.programCueRecButton)
        self.programCueRecButton.bind(on_press=self.programRecord)

        self.programCueClearButton = Button(text='program Cue \n   Clear', background_color='gray', size_hint=(.3, .1),
                                          pos=(0, 35))
        self.programCueGrid.add_widget(self.programCueClearButton)
        self.programCueClearButton.bind(on_press=self.programClear)

        self.programCue1Button = Button(text='Program Cue 1', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue1Button)
        self.programCue1Button.bind(on_press=self.programCue1)

        self.programCue2Button = Button(text='Program Cue 2', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue2Button)
        self.programCue2Button.bind(on_press=self.programCue2)

        self.programCue3Button = Button(text='Program Cue 3', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue3Button)
        self.programCue3Button.bind(on_press=self.programCue3)

        self.programCue4Button = Button(text='Program Cue 4', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue4Button)
        self.programCue4Button.bind(on_press=self.programCue4)

        self.programCue5Button = Button(text='Program Cue 5', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue5Button)
        self.programCue5Button.bind(on_press=self.programCue5)

        self.programCue6Button = Button(text='Program Cue 6', background_color='gray', size_hint=(.3, .1,), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue6Button)
        self.programCue6Button.bind(on_press=self.programCue6)

        self.programCue7Button = Button(text='Program Cue 7', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue7Button)
        self.programCue7Button.bind(on_press=self.programCue7)

        self.programCue8Button = Button(text='Program Cue 8', background_color='gray', size_hint=(.3, .1), pos=(0, 35))
        self.programCueGrid.add_widget(self.programCue8Button)
        self.programCue8Button.bind(on_press=self.programCue8)

#         self.effectsGrid = GridLayout()
#         self.effectsGrid.cols = 10
#         self.effectsGrid.padding = 4
#         self.effectsGrid.spacing = 2
#         self.add_widget(self.effectsGrid)
#         
#         self.addColorButton = Button(text='Add Color', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.addColorButton)
#         self.addColorButton.bind(on_press=self.addColor)
#         
#         self.subColorButton = Button(text='Subtract Color', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.subColorButton)
#         self.subColorButton.bind(on_press=self.subColor)
#         
#         self.color1ListButton = Button(text='Color List 1', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color1ListButton)
#         self.color1ListButton.bind(on_press=self.color1List)
#         
#         self.color2ListButton = Button(text='Color List 2', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color2ListButton)
#         self.color2ListButton.bind(on_press=self.color2List)
#         
#         self.color3ListButton = Button(text='Color List 3', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color3ListButton)
#         self.color3ListButton.bind(on_press=self.color3List)
#         
#         self.color4ListButton = Button(text='Color List 4', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color4ListButton)
#         self.color4ListButton.bind(on_press=self.color4List)
#         
#         self.color5ListButton = Button(text='Color List 5', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color5ListButton)
#         self.color5ListButton.bind(on_press=self.color5List)
#         
#         self.color6ListButton = Button(text='Color List 6', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color6ListButton)
#         self.color6ListButton.bind(on_press=self.color6List)
#         
#         self.color7ListButton = Button(text='Color List 7', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color7ListButton)
#         self.color7ListButton.bind(on_press=self.color7List)
#         
#         self.color8ListButton = Button(text='Color List 8', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.color8ListButton)
#         self.color8ListButton.bind(on_press=self.color8List)
#         
#         self.effectOffButton = Button(text='Effects Off', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effectOffButton)
#         self.effectOffButton.bind(on_press=self.effectOff)
#         
#         self.effect1Button = Button(text='Effect 1', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect1Button)
#         self.effect1Button.bind(on_press=self.effect1)
#         
#         self.effect2Button = Button(text='Effect 2', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect2Button)
#         self.effect2Button.bind(on_press=self.effect2)
#         
#         self.effect3Button = Button(text='Effect 3', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect3Button)
#         self.effect3Button.bind(on_press=self.effect3)
#         
#         self.effect4Button = Button(text='Effect 4', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect4Button)
#         self.effect4Button.bind(on_press=self.effect4)
#         
#         self.effect5Button = Button(text='Effect 5', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect5Button)
#         self.effect5Button.bind(on_press=self.effect5)
#         
#         self.effect6Button = Button(text='Effect 6', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect6Button)
#         self.effect6Button.bind(on_press=self.effect6)
#         
#         self.effect7Button = Button(text='Effect 7', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect7Button)
#         self.effect7Button.bind(on_press=self.effect7)
#         
#         self.effect8Button = Button(text='Effect 8', background_color='gray', size_hint=(.3, .25), pos=(0, 35))
#         self.effectsGrid.add_widget(self.effect8Button)
#         self.effect8Button.bind(on_press=self.effect8)

        
        self.color1(self)
        self.RGB(self)
        self.RGBspeed.text = str(10)
        
        x = 0
        


    #         self.step1 = Button(text='1', background_color='red', size_hint=(.3, .25))
    #         self.step1.bind(on_press=self.test)
    #         self.stepGrid.add_widget(self.step1)

#     def loadFile(self, instance):
#         fileOpen = open("/home/pi/Desktop/RPIneopixels-main/kivySaveFileDefault.py", "r")
#         fileOpen.read()
#         print("test")
           
    def saveFile(self, instance):
        global color
        global Rcolor

            
        #print(preset1._set_item(1,255,0,255,0))
        #file = open("/home/pi/Desktop/NeoPixelApp/kivySaveFileDefault.py", "w")
        file = open("/home/pi/Desktop/RPIneopixels/kivySaveFileDefault.py", "w")
        x = 0
        for i in colorList:
            file.write(f"\ncolor{x + 1} = " + str(colorList[x]))
            x += 1
        x = 0
        for i in superCueList:
            file.write(f"\nsuperCue{x + 1} = " + str(superCueList[x]))
            x += 1
        x = 0
        for i in programCueList:
            file.write(f"\nprogramCue{x + 1} = " + str(programCueList[x]))
            x += 1
        x = 0
        for i in groupList:
            file.write(f"\ngroup{x + 1} = " + str(groupList[x]))
            x += 1
        x = 0
        for i in presetList:
            file.write(f"\npresetSave{x + 1} = " + str(presetList[x]))
            x += 1
        x = 0
        #file.write(f"\nLED_COUNT = " + str(preset1._pixels))
        file.write("\npresetSaveList = [presetSave1, presetSave2, presetSave3, presetSave4, presetSave5, presetSave6, presetSave7, presetSave8, \npresetSave9, presetSave10, presetSave11, presetSave12, presetSave13, presetSave14, presetSave15, presetSave16, \npresetSave17, presetSave18, presetSave19, presetSave20, presetSave21, presetSave22, presetSave23, presetSave24, \npresetSave25, presetSave26, presetSave27, presetSave28, presetSave29, presetSave30, presetSave31, \npresetSave32, presetSave33, presetSave34, presetSave35, presetSave36, presetSave37, presetSave38, presetSave39, \npresetSave40, presetSave41, presetSave42, presetSave43, presetSave44, presetSave45, presetSave46, presetSave47, presetSave48, \npresetSave49, presetSave50, presetSave51, presetSave52, presetSave53, presetSave54, presetSave55, presetSave56, \npresetSave57, presetSave58, presetSave59, presetSave60, presetSave61, presetSave62, presetSave63, presetSave64]")
        file.write("\ngroupNamesList = " + str(groupNamesList))
        file.close()
    
#     def setPixelAmount(self, instance):
#         global x
#         global LED_COUNT
#         global preset1
#         LED_COUNT = int(self.pixelCountText.text)
#         x = 0
#         for i in presetList:
#             presetList[x]._pixels = LED_COUNT
#             presetList[x][2].append([0,0,0])
#             x += 1
#         print(preset1._pixels)
#         print(preset1)
    
    def skip1P(self, instance):
        global skip
        skip += 1
        
            
    def saveColor(self, instance):
        global save
        global color
        save += 1
        if save % 2 == 1:
            self.saveButton.background_color = 'red'
            self.RGBinputRed.text = str(int(colorList[color][0]))
            self.RGBinputGreen.text = str(int(colorList[color][1]))
            self.RGBinputBlue.text = str(int(colorList[color][2]))
        if save % 2 == 0:
            colorList[color] = (Rcolor, Gcolor, Bcolor)
            print(colorList[color])
            self.saveButton.background_color = 'gray'
        
    def color1(self, instance):
        global color
        color = 0
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color2(self, instance):
        global color
        color = 1
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color3(self, instance):
        global color
        color = 2
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color4(self, instance):
        global color
        color = 3
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color5(self, instance):
        global color
        color = 4
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color6(self, instance):
        global color
        color = 5
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color7(self, instance):
        global color
        color = 6
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color8(self, instance):
        global color
        color = 7
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))
        
    def colorBlank(self, instance):
        pass
    
    def color9(self, instance):
        global color
        color = 9
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color10(self, instance):
        global color
        color = 10
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color11(self, instance):
        global color
        color = 11
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color12(self, instance):
        global color
        color = 12
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color13(self, instance):
        global color
        color = 13
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color14(self, instance):
        global color
        color = 14
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color15(self, instance):
        global color
        color = 15
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def color16(self, instance):
        global color
        color = 16
        self.RGBinputRed.text = str(int(colorList[color][0]))
        self.RGBinputGreen.text = str(int(colorList[color][1]))
        self.RGBinputBlue.text = str(int(colorList[color][2]))

    def saveGroup(self, instance):
        global saveGroup
        global selectGroup
        global setPixel
        saveGroup += 1
        setPixel = 0
    
    def clearGroup(self, instance):
        global group
        groupList[group].clear()
    
    def groupOn(self, instance):
        global saveGroup
        global selectGroup
        global setPixel
        saveGroup = 0
        selectGroup += 1
        setPixel = 0

    def nameGroup(self, instance):
        global nameGroup
        nameGroup += 1 

    def group1(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 0
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group2(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 1
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group3(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 2
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group4(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 3
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group5(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 4
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group6(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 5
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group7(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 6
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group8(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 7
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group9(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 8
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group10(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 9
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group11(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 10
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group12(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 11
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group13(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 12
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group14(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 13
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group15(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 14
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group16(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 15
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group17(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 16
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group18(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 17
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group19(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 18
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group20(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 19
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group21(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 20
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group22(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 21
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group23(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 22
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group24(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 23
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group25(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 24
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group26(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 25
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group27(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 26
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group28(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 27
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group29(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 28
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group30(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 29
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group31(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 30
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group32(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 31
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group33(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 32
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group34(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 33
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group35(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 34
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group36(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 35
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group37(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 36
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group38(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 37
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group39(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 38
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group40(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 39
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group41(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 40
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group42(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 41
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group43(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 42
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group44(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 43
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group45(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 44
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group46(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 45
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group47(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 46
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group48(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 47
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group49(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 48
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group50(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 49
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group51(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 50
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group52(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 51
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group53(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 52
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group54(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 53
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group55(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 54
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group56(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 55
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group57(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 56
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group58(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 57
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group59(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 58
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)

    def group60(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 59
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
    
    def group61(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 60
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group62(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 61
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group63(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 62
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
            
    def group64(self, instance):
        global saveGroup
        global group
        global pixelHigh
        global pixelLow
        group = 63
        if saveGroup % 2 == 1:
            groupList[group].append(pixelHigh)
            groupList[group].append(pixelLow)
   

    def setRange(self, instance):
        global setPixel
        global selectGroup
        global saveGroup
        self.setRangeButton.background_color = 'red'
        setPixel += 1
        selectGroup = 0
        saveGroup = 0
    
    def RGBPixels(self, instance):
        global RGB
        RGB = 0
    
    def GRBPixels(self, instance):
        global RGB
        RGB = 1
    
    def BGRPixels(self, instance):
        global RGB
        RGB = 2

    def play(self, instance):
        global c
        global p
        global play
        c = 0
        p = 0
        play += 1

    def copy(self, instance):
        global c
        c += 1
        
    def clear(self, instance):
        global cue
        global play
        global x
        x = 0
        for i in presetList:
            if cue == x + 1:
                presetList[x].fill((0, 0, 0))
            x += 1
        presetList[cue - 1].show()
    
    def superMode(self, instance):
        global sM
        sM = 1
        print(sM)
        
    def programMode(self, instance):
        global sM
        sM = 0
        print(sM)

    def cue1(self, instance):
        global cue
        global sR
        global p
        cue = 1
        superCueRecording()

    def cue2(self, instance):
        global cue
        global sR
        global p
        cue = 2
        superCueRecording()

    def cue3(self, instance):
        global cue
        cue = 3
        superCueRecording()

    def cue4(self, instance):
        global cue
        cue = 4
        superCueRecording()

    def cue5(self, instance):
        global cue
        cue = 5
        superCueRecording()

    def cue6(self, instance):
        global cue
        cue = 6
        superCueRecording()

    def cue7(self, instance):
        global cue
        cue = 7
        superCueRecording()

    def cue8(self, instance):
        global cue
        global sR
        cue = 8
        superCueRecording()

    def cue9(self, instance):
        global cue
        cue = 9
        superCueRecording()

    def cue10(self, instance):
        global cue
        cue = 10
        superCueRecording()

    def cue11(self, instance):
        global cue
        cue = 11
        superCueRecording()

    def cue12(self, instance):
        global cue
        global sR
        cue = 12
        superCueRecording()

    def cue13(self, instance):
        global cue
        cue = 13
        superCueRecording()

    def cue14(self, instance):
        global cue
        cue = 14
        superCueRecording()

    def cue15(self, instance):
        global cue
        cue = 15
        superCueRecording()

    def cue16(self, instance):
        global cue
        global sR
        cue = 16
        superCueRecording()
    
    def cue17(self, instance):
        global cue
        global sR
        cue = 17
        superCueRecording()

    def cue18(self, instance):
        global cue
        global sR
        cue = 18
        superCueRecording()

    def cue19(self, instance):
        global cue
        cue = 19
        superCueRecording()

    def cue20(self, instance):
        global cue
        cue = 20
        superCueRecording()

    def cue21(self, instance):
        global cue
        cue = 21
        superCueRecording()

    def cue22(self, instance):
        global cue
        cue = 22
        superCueRecording()

    def cue23(self, instance):
        global cue
        cue = 23
        superCueRecording()

    def cue24(self, instance):
        global cue
        global sR
        cue = 24
        superCueRecording()

    def cue25(self, instance):
        global cue
        cue = 25
        superCueRecording()

    def cue26(self, instance):
        global cue
        cue = 26
        superCueRecording()

    def cue27(self, instance):
        global cue
        cue = 27
        superCueRecording()

    def cue28(self, instance):
        global cue
        global sR
        cue = 28
        superCueRecording()
        
    def cue29(self, instance):
        global cue
        cue = 29
        superCueRecording()
    
    def cue30(self, instance):
        global cue
        cue = 30
        superCueRecording()

    def cue31(self, instance):
        global cue
        cue = 31
        superCueRecording()

    def cue32(self, instance):
        global cue
        cue = 32
        superCueRecording()
    
    def cue33(self, instance):
        global cue
        global sR
        cue = 33
        superCueRecording()

    def cue34(self, instance):
        global cue
        global sR
        cue = 34
        superCueRecording()

    def cue35(self, instance):
        global cue
        cue = 35
        superCueRecording()

    def cue36(self, instance):
        global cue
        cue = 36
        superCueRecording()

    def cue36(self, instance):
        global cue
        cue = 36
        superCueRecording()

    def cue37(self, instance):
        global cue
        cue = 37
        superCueRecording()

    def cue38(self, instance):
        global cue
        cue = 38
        superCueRecording()

    def cue39(self, instance):
        global cue
        global sR
        cue = 39
        superCueRecording()

    def cue40(self, instance):
        global cue
        cue = 40
        superCueRecording()

    def cue41(self, instance):
        global cue
        cue = 41
        superCueRecording()

    def cue42(self, instance):
        global cue
        cue = 42
        superCueRecording()

    def cue43(self, instance):
        global cue
        global sR
        cue = 43
        superCueRecording()

    def cue44(self, instance):
        global cue
        cue = 44
        superCueRecording()

    def cue45(self, instance):
        global cue
        cue = 45
        superCueRecording()
    
    def cue46(self, instance):
        global cue
        cue = 46
        superCueRecording()

    def cue47(self, instance):
        global cue
        cue = 47
        superCueRecording()

    def cue48(self, instance):
        global cue
        cue = 48
        superCueRecording()
    
    def cue49(self, instance):
        global cue
        cue = 49
        superCueRecording()

    def cue50(self, instance):
        global cue
        cue = 50
        superCueRecording()

    def cue51(self, instance):
        global cue
        cue = 51
        superCueRecording()

    def cue52(self, instance):
        global cue
        cue = 52
        superCueRecording()

    def cue53(self, instance):
        global cue
        cue = 53
        superCueRecording()

    def cue54(self, instance):
        global cue
        cue = 54
        superCueRecording()

    def cue55(self, instance):
        global cue
        global sR
        cue = 55
        superCueRecording()

    def cue56(self, instance):
        global cue
        cue = 56
        superCueRecording()

    def cue57(self, instance):
        global cue
        cue = 57
        superCueRecording()

    def cue58(self, instance):
        global cue
        cue = 58
        superCueRecording()

    def cue59(self, instance):
        global cue
        global sR
        cue = 59
        superCueRecording()
        
    def cue60(self, instance):
        global cue
        cue = 60
        superCueRecording()
    
    def cue61(self, instance):
        global cue
        cue = 61
        superCueRecording()

    def cue62(self, instance):
        global cue
        cue = 62
        superCueRecording()

    def cue63(self, instance):
        global cue
        cue = 63
        superCueRecording()
    
    def cue64(self, instance):
        global cue
        cue = 64
        superCueRecording()

    def superRecord(self, instance):
        global sR
        sR += 1

    def superClear(self, instance):
        global sC
        global play
        global x
        play = 0
        x = 0
        for i in superCueList:
            if sC == x:
                superCueList[x].clear()
            x += 1

    def superCue1(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 0
        programCueRecording()

    def superCue2(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 1
        programCueRecording()

    def superCue3(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 2
        programCueRecording()

    def superCue4(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 3
        programCueRecording()

    def superCue5(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 4
        programCueRecording()

    def superCue6(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 5
        programCueRecording()

    def superCue7(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 6
        programCueRecording()

    def superCue8(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 7
        programCueRecording()
    
    def superCue9(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 8
        programCueRecording()

    def superCue10(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 9
        programCueRecording()

    def superCue11(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 10
        programCueRecording()

    def superCue12(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 11
        programCueRecording()

    def superCue13(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 12
        programCueRecording()

    def superCue14(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 13
        programCueRecording()

    def superCue15(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 14
        programCueRecording()

    def superCue16(self, instance):
        global sC
        global play
        global c
        c = 0
        sC = 15
        programCueRecording()
    
    #Program Cues
    def programRecord(self, instance):
        global pR
        pR += 1

    def programClear(self, instance):
        global sC
        global play
        global x
        play = 0
        x = 0
        for i in programCueList:
            if pC == x:
                programCueList[x].clear()
            x += 1
        
    def programCue1(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 0

    def programCue2(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 1

    def programCue3(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 2

    def programCue4(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 3

    def programCue5(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 4

    def programCue6(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 5

    def programCue7(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 6

    def programCue8(self, instance):
        global pC
        global play
        global c
        c = 0
        pC = 7

    def slide_it_red(self, *args):
        global pixelHigh
        global pixelLow
        global sliderStop
        global r
        global Gcolor
        global Bcolor
        global Rcolor
        self.RGBinputRed.text = str(int(args[1]))
        # Rcolor = args[1]
        for i in range(pixelHigh - pixelLow):
            np[pixelLow] = (Rcolor, Gcolor, Bcolor)
            pixelLow += 1
        sliderStop = 1
        # np.show()

    def slide_it_green(self, *args):
        global pixelHigh
        global pixelLow
        global sliderStop
        global r
        global Gcolor
        global Bcolor
        global Rcolor
        self.RGBinputGreen.text = str(int(args[1]))
        # Gcolor = args[1]
        for i in range(pixelHigh - pixelLow):
            np[pixelLow] = (Rcolor, Gcolor, Bcolor)
            pixelLow += 1
        sliderStop = 1
        # np.show()

    def slide_it_blue(self, *args):
        global pixelHigh
        global pixelLow
        global sliderStop
        global r
        global Gcolor
        global Bcolor
        global Rcolor
        print(args[1])
        self.RGBinputBlue.text = str(int(args[1]))
        # Bcolor = args[1]
        for i in range(pixelHigh - pixelLow):
            np[pixelLow] = (Rcolor, Gcolor, Bcolor)
            pixelLow += 1
        sliderStop = 1
        # np.show()

    def slide_it_brightness(self, *args):
        global master
        global brightnessWeight
        master = args[1] * (brightnessWeight * .01)
        self.RGBbrightness.text = str(round(float(args[1]) * 100, 0))
    
    def slide_it_speed(self, *args):
        global speed
        speed = 1/args[1]
        self.RGBspeed.text = str(round(float(args[1]) * 1, 0))

    def Red(self, instance):
        np.fill((255, 0, 0))
        if self.RGBinputRed.text.isdigit() is False:
            self.RGBinputRed.text = 0
        else:
            self.RGBinputRed.text = str(int(255))
        np.show()

    def Green(self, instance):
        np.fill((0, 255, 0))
        self.RGBinputGreen.text = str(int(255))
        np.show()

    def Blue(self, instance):
        np.fill((0, 0, 255))
        self.RGBinputBlue.text = str(int(255))
        np.show()
        
#     def effectOff(self, instance):
#         global e1
#         e1 = 0
#         
#     def effect1(self, instance):
#         global e1
#         e1 = 1
#     def effect2(self, instance):
#         global e1
#         e1 = 2
#     def effect3(self, instance):
#         global e1
#         e1 = 3
#     def effect4(self, instance):
#         global e1
#         e1 = 4
#     def effect5(self, instance):
#         global e1
#         e1 = 5
#     def effect6(self, instance):
#         global e1
#         e1 = 6
#     def effect7(self, instance):
#         global e1
#         e1 = 7
#     def effect8(self, instance):
#         global e1
#         e1 = 8
#     
#     def addColor(self, instance):
#         global saveColorList
#         global clNumber
#         global black
#         colorLists[clNumber].append((Rcolor, Gcolor, Bcolor))
#         if colorLists[clNumber][0] == black:
#             colorLists[clNumber].pop(0)
#         
#     def subColor(self, instance):
#         global saveColorList
#         global clNumber
#         if len(colorLists[clNumber]) > 0:
#             colorLists[clNumber].pop(-1)
#         if len(colorLists[clNumber]) == 0:
#             colorLists[clNumber].append((0,0,0))
#         
#     def color1List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 0
#         
#     def color2List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 1
#  
#     def color3List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 2
#  
#     def color4List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 3
# 
#     def color5List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 4
# 
#     def color6List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 5
# 
#     def color7List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 6
# 
#     def color8List(self, instance):
#         global clNumber
#         global saveColorList
#         clNumber = 7



    def RGB(self, instance):
        global c
        global sC
        global sR
        global cue
        global Rcolor
        global Gcolor
        global Bcolor
        global sliderStop
        global r
        global g
        global b
        global pixelHigh
        global pixelLow
        global cue
        global play
        global brightness
        global e1
        global cl
        global p
        global clNumber
        global x
        global master
        global pR
        global pC
        global sM
        global save
        global group
        global color
        global nameGroup
        global speed
        global RGB
        global LED_COUNT
        global brightnessWeight
        global skip
        global preset1
        start = time.time()
        
        if play % 2 == 0:
            colorSelect = Clock.schedule_once(self.RGB, .001)
        
        RGBButtonListColor = [self.RGBPixelsButton, self.GRBPixelsButton, self.BGRPixelsButton]
        
#         if self.pixelCountText.text.isdigit() is True:
#             if LED_COUNT != int(self.pixelCountText.text):
#                 self.setPixelCount.background_color = 'red'
#             else:
#                 self.setPixelCount.background_color = 'green'
        
        x = 0
        for i in RGBButtonListColor:
            if RGB == x:
                RGBButtonListColor[x].background_color = 'red'
            else:
                RGBButtonListColor[x].background_color = 'gray'
            x += 1
        
        if RGB == 0:
            Rcolor = self.RGBinputRed.text
            Gcolor = self.RGBinputGreen.text
            Bcolor = self.RGBinputBlue.text
        elif RGB == 1:
            Rcolor = self.RGBinputGreen.text
            Gcolor = self.RGBinputRed.text
            Bcolor = self.RGBinputBlue.text
        elif RGB == 2:
            Rcolor = self.RGBinputBlue.text
            Gcolor = self.RGBinputGreen.text
            Bcolor = self.RGBinputRed.text

        if Rcolor.isdigit() is False:
            Rcolor = 0
        else:
            Rcolor = int(Rcolor)
        if Gcolor.isdigit() is False:
            Gcolor = 0
        else:
            Gcolor = int(Gcolor)
        if Bcolor.isdigit() is False:
            Bcolor = 0
        else:
            Bcolor = int(Bcolor)

        if Rcolor > 255:
            Rcolor = 255
        if Gcolor > 255:
            Gcolor = 255
        if Bcolor > 255:
            Bcolor = 255
        if Rcolor < 0:
            Rcolor = 0
        if Gcolor < 0:
            Gcolor = 0
        if Bcolor < 0:
            Bcolor = 0

        pixelLow = self.pixelLow.text
        pixelHigh = self.pixelHigh.text
        if pixelLow.isdigit() is False:
            pixelLow = 0
        if pixelHigh.isdigit() is False:
            pixelHigh = 0
        pixelLow = int(pixelLow) - 1
        pixelHigh = int(pixelHigh)
        if pixelHigh > LED_COUNT:
            pixelHigh = LED_COUNT

        colorButtonList = [color1, color2, color3, color4, color5, color6, color7, color8, colorBlank,
                           color9, color10, color11, color12, color13, color14, color15, color16]
        colorButtonListColor = [self.color1Button, self.color2Button, self.color3Button, self.color4Button,
                                self.color5Button, self.color6Button, self.color7Button, self.color8Button, self.colorBlankButton,
                                self.color9Button, self.color10Button, self.color11Button, self.color12Button,
                                self.color13Button, self.color14Button, self.color15Button, self.color16Button,]
           
        if save % 2 == 1:
            colorButtonList[color] = (Rcolor, Gcolor, Bcolor)
            colorButtonListColor[color].background_color = (Rcolor / 255, Gcolor / 255, Bcolor / 255)
        else:
            x = 0
            for i in colorButtonListColor:
                colorButtonListColor[x].background_color = (colorList[x][0] / 255, colorList[x][1] / 255, colorList[x][2] / 255)
                x += 1
        

        if saveGroup % 2 == 1:
            self.saveGroupButton.background_color = 'red'
            self.saveGroupButton.text = 'To add to Group, Select Pixel Range' + '\n and click on the Group you would' '\nlike to add the range of pixels to'
        else:
            self.saveGroupButton.background_color = 'gray'
            self.saveGroupButton.text = 'Add to Group'
        
        if selectGroup % 2 == 1:
            self.groupOnButton.background_color = 'red'
            self.groupOnButton.text = 'Groups On'
        else:
            self.groupOnButton.background_color = 'gray'
            self.groupOnButton.text = 'Groups Off'

        if skip % 2 == 1:
            self.skip1Pixel.background_color = 'red'
            pixelLow = pixelLow + 1
            pixelHigh = pixelHigh + 1
        else:
            self.skip1Pixel.background_color = 'gray'

        x = 0
        for i in presetList:
            
            if setPixel % 2 == 1 and cue == x + 1:
                for i in range(pixelHigh - pixelLow):
                    presetList[x][pixelLow] = (Rcolor, Gcolor, Bcolor)
                    presetList[x].brightness = master
                    #print(presetList[x]._pixels)
                    pixelLow += 1
                presetList[x].show()
                
            x += 1
        
        x = 0
        for i in presetList:
            if selectGroup % 2 == 1 and cue == x + 1:
                y = 1
                for i in range(int(len(groupList[group]) / 2)):
                    z = groupList[group][y]
                    for i in range(groupList[group][y - 1] - groupList[group][y]):
                        presetList[x][z] = (Rcolor, Gcolor, Bcolor)
                        z += 1
                        presetList[x].brightness = master
                    y += 2
                presetList[x].show()
                
            x += 1

#         x = 0
#         for i in presetList:          
#             if setPixel % 2 == 0 and cue == x + 1:
#                 presetList[x].show()
#             x += 1

        if setPixel % 2 == 0:
            self.setRangeButton.background_color = 'gray'
        
        if sM == 1:
            if play % 2 == 1:
                if len(superCueList[sC]) > 0:
                    cue = superCueList[sC][c]
                    x = 0
                    for i in presetList:          
                        if setPixel % 2 == 0 and cue == x + 1:
                            presetList[x].show()
                        x += 1
                    c += 1
                    colorSelect = Clock.schedule_once(self.RGB, speed)
                    self.playButton.background_color = 'red'
                    if c == len(superCueList[sC]):
                        c = 0
        if sM == 0:
            if play % 2 == 1:
                if len(programCueList[pC]) > 0 and len(superCueList[sC]) > 0:
                    sC = programCueList[pC][p]
                    cue = superCueList[sC][c]
                    x = 0
                    for i in presetList:          
                        if setPixel % 2 == 0 and cue == x + 1:
                            presetList[x].show()
                        x += 1
                    c += 1
                    colorSelect = Clock.schedule_once(self.RGB, speed)
                    self.playButton.background_color = 'red'
                    if c == len(superCueList[sC]):
                        c = 0
                        p += 1
                        if p == len(programCueList[pC]):
                            p = 0

        if play % 2 == 0:
            self.playButton.background_color = 'gray'

        if sR % 2 == 1:
            self.superCueRecButton.background_color = 'red'

        if sR % 2 == 0:
            self.superCueRecButton.background_color = 'gray'
        
        if pR % 2 == 1:
            self.programCueRecButton.background_color = 'red'

        if pR % 2 == 0:
            self.programCueRecButton.background_color = 'gray'

        groupButtonList = [self.group1Button, self.group2Button, self.group3Button, self.group4Button,
                           self.group5Button, self.group6Button, self.group7Button, self.group8Button,
                           self.group9Button, self.group10Button, self.group11Button, self.group12Button,
                           self.group13Button, self.group14Button, self.group15Button, self.group16Button,
                           self.group17Button, self.group18Button, self.group19Button, self.group20Button,
                           self.group21Button, self.group22Button, self.group23Button, self.group24Button,
                           self.group25Button, self.group26Button, self.group27Button, self.group28Button,
                           self.group29Button, self.group30Button, self.group31Button, self.group32Button,
                           self.group33Button, self.group34Button, self.group35Button, self.group36Button,
                           self.group37Button, self.group38Button, self.group39Button, self.group40Button,
                           self.group41Button, self.group42Button, self.group43Button, self.group44Button,
                           self.group45Button, self.group46Button, self.group47Button, self.group48Button,
                           self.group49Button, self.group50Button, self.group51Button, self.group52Button,
                           self.group53Button, self.group54Button, self.group55Button, self.group56Button,
                           self.group57Button, self.group58Button, self.group59Button, self.group60Button,
                           self.group61Button, self.group62Button, self.group63Button, self.group64Button,]

        x = 0
        for i in groupButtonList:
            if group == x:
                groupButtonList[x].background_color = 'red'
            else:
                groupButtonList[x].background_color = 'gray'
            x += 1
        
        x = 0
        if nameGroup % 2 == 1:
            groupButtonList[group].text = self.nameGroupText.text
            groupNamesList.pop(group)
            groupNamesList.insert(group, groupButtonList[group].text)
            print(groupNamesList)
            nameGroup = 0

            
        #effects button Colors
#         effectButtonList = [self.effectOffButton, self.effect1Button, self.effect2Button, self.effect3Button, self.effect4Button, self.effect5Button,
#                             self.effect6Button, self.effect7Button, self.effect8Button]
#                             
#         x = 0
#         for i in effectButtonList: 
#             if e1 == x:
#                 effectButtonList[x].background_color = 'red'
#             else:
#                 effectButtonList[x].background_color = 'gray'
#             x += 1

        
#         colorListList = [self.color1ListButton, self.color2ListButton, self.color3ListButton, self.color4ListButton, self.color5ListButton, self.color6ListButton,
#                          self.color7ListButton, self.color8ListButton]
#         x = 0
#         for i in colorListList:
#             if clNumber == x:
#                 colorListList[x].background_color = 'red'
#             else:
#                 colorListList[x].background_color = 'gray'
#             x += 1
        
        
        cueButtonList = [self.cue1Button, self.cue2Button, self.cue3Button, self.cue4Button, self.cue5Button, self.cue6Button, self.cue7Button, self.cue8Button, self.cue9Button,
                         self.cue10Button, self.cue11Button, self.cue12Button,
                         self.cue13Button, self.cue14Button, self.cue15Button, self.cue16Button, self.cue17Button, self.cue18Button, self.cue19Button, self.cue20Button,
                         self.cue21Button, self.cue22Button, self.cue23Button, self.cue24Button, self.cue25Button, self.cue26Button, self.cue27Button, self.cue28Button,
                         self.cue29Button, self.cue30Button, self.cue31Button, self.cue32Button, self.cue33Button, self.cue34Button, self.cue35Button, self.cue36Button,
                         self.cue37Button, self.cue38Button, self.cue39Button, self.cue40Button, self.cue41Button, self.cue42Button, self.cue43Button, self.cue44Button,
                         self.cue45Button, self.cue46Button, self.cue47Button, self.cue48Button, self.cue49Button, self.cue50Button, self.cue51Button, self.cue52Button,
                         self.cue53Button, self.cue54Button, self.cue55Button, self.cue56Button, self.cue57Button, self.cue58Button, self.cue59Button, self.cue60Button,
                         self.cue61Button, self.cue62Button, self.cue63Button, self.cue64Button]
        x = 0
        for i in cueButtonList:
            if cue == x + 1:
                cueButtonList[x].background_color = 'red'
            else:
                cueButtonList[x].background_color = 'gray'
            x += 1

        superCueButtonList = [self.superCue1Button, self.superCue2Button, self.superCue3Button, self.superCue4Button,
                              self.superCue5Button, self.superCue6Button, self.superCue7Button, self.superCue8Button,
                              self.superCue9Button, self.superCue10Button, self.superCue11Button, self.superCue12Button,
                              self.superCue13Button, self.superCue14Button, self.superCue15Button, self.superCue16Button]
        
        x = 0
        for i in superCueButtonList:
            if sC == x:
                superCueButtonList[x].background_color = 'red'
            else:
                superCueButtonList[x].background_color = 'gray'
            x += 1
        
        programCueButtonList = [self.programCue1Button, self.programCue2Button, self.programCue3Button, self.programCue4Button,
                              self.programCue5Button, self.programCue6Button, self.programCue7Button, self.programCue8Button]
        
        x = 0
        for i in programCueButtonList:
            if pC == x:
                programCueButtonList[x].background_color = 'red'
            else:
                programCueButtonList[x].background_color = 'gray'
            x += 1
        
        if sM == 1:
            self.superModeButton.background_color = 'red'
            self.programModeButton.background_color = 'gray'
        if sM == 0:
            self.superModeButton.background_color = 'gray'
            self.programModeButton.background_color = 'red'
        
        res = isinstance(self.RGBinputRed.text, int)
        ges = isinstance(self.RGBinputGreen.text, int)
        bes = isinstance(self.RGBinputBlue.text, int)
        
        
        #self.ids.slider_label_red.text = str(self.red.text)
        if res is False:
            if self.RGBinputRed.text.isdigit() is True:
                self.ids.slider_red.value = int(self.RGBinputRed.text)
                if int(self.RGBinputRed.text) > 255:
                    self.ids.slider_red.value = 255
                if int(self.RGBinputRed.text) < 0:
                    self.ids.slider_red.value = 0
        if ges is False:
            if self.RGBinputGreen.text.isdigit() is True:
                self.ids.slider_green.value = int(self.RGBinputGreen.text)
                if int(self.RGBinputGreen.text) > 255:
                    self.ids.slider_green.value = 255
                if int(self.RGBinputGreen.text) < 0:
                    self.ids.slider_green.value = 0
        if bes is False:
            if self.RGBinputBlue.text.isdigit() is True:
                self.ids.slider_blue.value = int(self.RGBinputBlue.text)
                if int(self.RGBinputBlue.text) > 255:
                    self.ids.slider_blue.value = 255
                if int(self.RGBinputBlue.text) < 0:
                    self.ids.slider_blue.value = 0
        
        if self.RGBbrightness.text.isdigit() is True:
            self.ids.slider_brightness.value = int(self.RGBbrightness.text) / 100
            
        if self.RGBspeed.text.isdigit() is True:
            self.ids.slider_speed.value = int(self.RGBspeed.text) / 5
        
        if self.RGBbrightnessWeight.text.isdigit() is True and int(self.RGBbrightnessWeight.text) > 0:
            brightnessWeight = int(self.RGBbrightnessWeight.text)
        end = time.time()
        
        #print((end-start) + speed)
class MyApp(App):
    title = 'PiPixels'
    def build(self):
        return MyLayout()


# run Say Hello App Calss
if __name__ == "__main__":
    MyApp().run()

