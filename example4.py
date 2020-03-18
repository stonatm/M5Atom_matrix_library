import matrix
import urandom
import time

#assign randint function to r
r = urandom.randint

#create matrix class object
s = matrix.matrix

#initialize led matrix
s.init()
#clear led matrix
s.clear_all()
#show changes
s.show()

#smile pixmaps
smile0 = [
  0,0,0,0,0,
  0,1,0,1,0,
  0,0,0,0,0,
  1,0,0,0,1,
  0,1,1,1,0
  ]
  
smile1 = [
  0,0,0,0,0,
  0,1,0,1,0,
  0,0,0,0,0,
  1,1,1,1,1,
  0,0,0,0,0
  ]

smile2 = [
  0,0,0,0,0,
  0,1,0,1,0,
  0,0,0,0,0,
  0,1,1,1,0,
  1,0,0,0,1
  ]

while 1:
  #set random active color
  s.pixel_color( r(0,360) )
  #write smile pixmap to led matrix and show changes
  s.clear_all()
  s.pixel_mask( smile0 )
  s.show()
  time.sleep_ms(1000)
  s.clear_all()
  s.pixel_mask( smile1 )
  s.show()
  time.sleep_ms(1000)
  s.clear_all()
  s.pixel_mask( smile2 )
  s.show()
  time.sleep_ms(1000)


