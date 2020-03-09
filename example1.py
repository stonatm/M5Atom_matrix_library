import matrix
import urandom
import time


#assign randint function to r
r = urandom.randint

#create matrix class object
s = matrix.matrix

#initialize matrix
s.init()
#clear matrix
s.clear_all()
#show changes
s.show()

while 1:
  #set random activr color
  s.pixel_color( r(0,360) )
  #blink pixel at random position
  #pixel_blink change pixels immediately
  #you dont need use s.show() function
  s.pixel_blink( r(0,4), r(0,4), 10 )
  #wait some time
  time.sleep_ms(10)
