#simple ds1820 ds18b20 module
#reads only one sensor per pin

from machine import Pin
import _onewire

class ds1820:

  #configure pin to onewire transmission
  def init(pin):
    Pin(pin, Pin.OPEN_DRAIN, Pin.PULL_UP)

  #send convert command to sensor
  def convert(pin):
    _onewire.reset(Pin(pin))
    _onewire.writebyte(Pin(pin), 0xcc) #skip rom
    _onewire.writebyte(Pin(pin), 0x44) #convert

  #send read temperature command to sensor
  def read(pin):
    _onewire.reset(Pin(pin))
    _onewire.writebyte(Pin(pin), 0xcc) #skip rom
    _onewire.writebyte(Pin(pin), 0xbe) #read scratchpad

    tlo = _onewire.readbyte(Pin(pin))
    thi = _onewire.readbyte(Pin(pin))
    _onewire.reset(Pin(pin))

    #convert raw values to human eye readable
    temp = tlo + thi * 256
    if temp > 32767:
      temp = temp - 65536
    temp = temp * 0.5
    return(temp)

class ds18b20:
  
  #configure pin to onewire transmission
  def init(pin):
    Pin(pin, Pin.OPEN_DRAIN, Pin.PULL_UP)
  
  #send convert command to sensor
  def convert(pin):
    _onewire.reset(Pin(pin))
    _onewire.writebyte(Pin(pin), 0xcc) #skip rom
    _onewire.writebyte(Pin(pin), 0x44) #convert
  
  #send read temperature command to sensor
  def read(pin):
    _onewire.reset(Pin(pin))
    _onewire.writebyte(Pin(pin), 0xcc) #skip rom
    _onewire.writebyte(Pin(pin), 0xbe) #read scratchpad
    #read raw temperature
    tlo = _onewire.readbyte(Pin(pin))
    thi = _onewire.readbyte(Pin(pin))
    _onewire.reset(Pin(pin))
    #convert raw values to human eye readable
    temp = tlo + thi * 256
    if temp > 32767:
      temp = temp - 65536
    temp = temp * 0.0625
    return(temp)

