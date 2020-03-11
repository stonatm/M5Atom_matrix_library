import matrix
import digits
import urandom
import time


#assign randint function to r
r = urandom.randint

#create matrix class object
s = matrix.matrix

#create digits class object
d = digits

#initialize led matrix
s.init()
#clear led matrix
s.clear_all()
#show changes
s.show()

color = 0
while 1:
  #set random active color
  s.pixel_color( color )
  
  #write pixmap of random digit to pic variable
  pic = d.get_digit( r(0,9), d.digits_center )
  #pic = d.get_digit( r(0,9), d.digits_left )
  #pic = d.get_digit( r(0,9), d.digits_right )
  #write pixmap to led matrix
  s.clear_all()
  s.pixel_mask( pic )
  #show changes
  s.show()
  #wait some time
  time.sleep_ms(1000)
  color = color + 5

