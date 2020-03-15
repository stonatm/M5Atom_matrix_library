#m5atom matrix termometer example with ds18b20 sensor
#this example is only an idea, not a final code
#its simple example display only positive temperature
# from 0 to 99 degrees (two digits) only
#negative temperatures or greater than 99 can cause errors.

#sensor connect schema to atom
# 1 GND to GND
# 2 DQ to GPIO25
# 3 VCC to GPIO21
# connect 2.2 - 4.7 kohm resistor betwen DQ and VCC

import dallas
import matrix
import digits
import time

from machine import Pin

l = matrix.matrix
d = digits
t = dallas.ds18b20

#ds18b20 data pin
DS_PIN = 25
#main loop delay minimum 750ms for correct reads from sensor
LOOP_DELAY = 1000

#initialize matrix
l.init()
l.clear_all()

#set gpio 21 as power line for temperature sensor
power = Pin(21,Pin.OUT)
power.value(1)

#initialise temperature sensor
#and do first temperature measure
t.init(DS_PIN)
t.convert(DS_PIN)
#wait minimum 750ms betwen measure and read temperature
time.sleep_ms(750)

while 1:
  #read temperature from sensor
  temp_f = t.read(DS_PIN)
  temp = int(temp_f)
  d1 = int(temp/10)
  d2 = temp%10

  #debug line
  print(temp_f,temp,d1,d2)
  
  l.clear_all()
  l.show()
  #show left digit
  l.pixel_color(60)
  l.pixel_mask(d.digits_left[d1*25:])
  l.show()
  #show right digit
  l.pixel_color(120)
  l.pixel_mask(d.digits_right[d2*25:])
  l.show()
  
  #start measure temperature
  t.convert(DS_PIN)
  #wait minimum 750ms
  time.sleep_ms(LOOP_DELAY)
