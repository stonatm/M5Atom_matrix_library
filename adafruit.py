#M5Atom matrix scroll text example using matrix.py library
#Reads data from adafruit.io using REST API.
#Feed from adafruit.io who you want to read without APIKEY
#must be set as PUBLIC in feed settings.
#That mean that anyone can read it, but cannot write to it.

import urequests
import matrix
import time
import json
import urandom

import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
#REPLACE YOUR ACCES POINT CREDENTIALS BELOW
sta_if.connect("YOUR_ACCES_POINT_NAME", "AP_PASSWORD")

def read(delay=100):
  #creating aliasses
  r = urandom.randint
  m = matrix.matrix
  
  #init matrix
  m.init()
  m.clear_all()
  
  #setting adafruit.io access data
  USER_NAME = 'robalstona'
  FEED_NAME = 'feed02'
  #access to adafruit.io feed via REST API
  #read humidity value from feed
  response = urequests.get('https://io.adafruit.com/api/v2/' + USER_NAME + '/feeds/' + FEED_NAME)
  #decode json response from adafruit.io
  output = json.loads((response.text))
  #reads a needed field from response
  feed_value = output['last_value']
  #set random color of text
  m.pixel_color( r(0,360) )
  text = 'humidity = ' + feed_value + ' %rh'
  #print value
  print(text)
  #scroll values on matrix
  m.text_scroll(text, delay)

  #setting adafruit.io access data
  USER_NAME = 'robalstona'
  FEED_NAME = 'feed01'
  #access to adafruit.io feed via REST API
  #read temperature value from feed
  response = urequests.get('https://io.adafruit.com/api/v2/' + USER_NAME + '/feeds/' + FEED_NAME)
  #decode json response from adafruit.io
  output = json.loads((response.text))
  #reads a needed field from response
  feed_value = output['last_value']
  #set random color of text
  m.pixel_color( r(0,360) )
  #create celsius symbol character
  celsius = chr(176)
  text = 'temperature = ' + feed_value + ' ' + celsius + 'C'
  #print value
  print(text)
  #scroll values on matrix
  m.text_scroll(text, delay)
