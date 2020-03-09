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
  #set random active color
  s.pixel_color( r(0,360) )
  #breathe pixel at random position
  #pixel_breathe change pixels immediately
  #you dont need use s.show() function
  s.pixel_breathe( r(0,4), r(0,4) )
  #wait some time
  time.sleep_ms(10)
