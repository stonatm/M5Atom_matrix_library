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

#setings digits colors
color1 = 0 #color of left digit
color2 = 210 #color of right digit
color3 = 300 #color of common pixels of digits

number = 0
while 1:
  d1 = int(number / 10)
  d2 = number % 10
  d_l = d.get_digit(d1, d.digits_left)
  d_r = d.get_digit(d2, d.digits_right)
  #create empty pixmap of common pixel
  d_com = [0] * 25
  #find common pixels of left and right digits and create new pixmap
  for pix in range (0, 25):
    if ((d_l[pix] + d_r[pix]) == 2):
      d_com[pix] = 1
    else:
      d_com[pix] = 0
  #show digits
  s.clear_all()
  s.pixel_color(color1)
  s.pixel_mask(d_l)
  s.pixel_color(color2)
  s.pixel_mask(d_r)
  s.pixel_color(color3)
  s.pixel_mask(d_com)
  s.show()
  time.sleep_ms(500)
  number = number +1
  if number > 99:
    number = 0

