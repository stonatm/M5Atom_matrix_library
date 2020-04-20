
#Copyright (c) 2020 stonatm@gmail.com
#m5atom matrix
#neopixel 5x5 matrix library V2 with text scrolling
#HSV color model

from machine import Pin
import neopixel
import time
import math
import font

class matrix:

  # m5atom matrix hardware specific values
  LED_PIN = 27
  LED_WIDTH = 5
  LED_HEIGHT = 5
  LED_NUM = LED_WIDTH * LED_HEIGHT
  LED_BRIGHTNESS = 0.25 #max led brightness due to heating up to high temperature
  INSTA_DRAW = 0
  np = None

  #color in hsv color model color(h, s, v)
  #h = 0 - 360
  #s = 0 - 1.0
  #v = 0 - 1.0
  color = (0, 0, 1 * LED_BRIGHTNESS) #initial set color to white

  def init():
    matrix.np = neopixel.NeoPixel(Pin(matrix.LED_PIN), matrix.LED_NUM)

  def translate(value, inMin, inMax, outMin, outMax):
    return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin

  #convert color from hsv to rgb
  def hsv(h, s=1, v=1):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

  #set color used to draw function
  def pixel_color(h, s=1, v=1):
    matrix.color = (h, s, v * matrix.LED_BRIGHTNESS)

  def pixel_set(x, y):
    matrix.np[x + y * matrix.LED_HEIGHT] = matrix.hsv(*matrix.color)
    if matrix.INSTA_DRAW: matrix.show()

  def pixel_clear(x, y):
    matrix.np[x + y * matrix.LED_HEIGHT] = (0, 0, 0)
    if matrix.INSTA_DRAW: matrix.show()

  def pixel_blink(x, y, delay_ms=100 ):
    previous = matrix.np[x + y * matrix.LED_HEIGHT]
    matrix.np[x + y * matrix.LED_HEIGHT] = matrix.hsv(*matrix.color)
    matrix.np.write()
    time.sleep_ms( delay_ms )
    matrix.np[x + y * matrix.LED_HEIGHT] = previous
    matrix.np.write()

  def clear_all():
    matrix.np.fill((0,0,0))
    if matrix.INSTA_DRAW: matrix.show()

  def show():
    matrix.np.write()

  #write raw rgb value buffer to matrix
  def write_buffer(buf):
    size = matrix.LED_NUM
    if len(buf) < matrix.LED_NUM:
      size = len(buf)
    for pix in range (0, size):
      matrix.np[pix] = buf[pix]
    if matrix.INSTA_DRAW: matrix.show()

  def pixel_breathe(x, y, ms_in=50, ms_out=50):
    for i in range (0, 11, 1):
      val = math.pow(2, i) - 1
      matrix.np[x + y * matrix.LED_HEIGHT] = matrix.hsv(matrix.color[0], matrix.color[1], (matrix.LED_BRIGHTNESS * matrix.translate(val, 0, 1024, 0, 1)) )
      matrix.np.write()
      time.sleep_ms(ms_in)
    for i in range (10, -1, -1):
      val = math.pow(2, i) - 1
      matrix.np[x + y * matrix.LED_HEIGHT] = matrix.hsv(matrix.color[0], matrix.color[1], (matrix.LED_BRIGHTNESS * matrix.translate(val, 0, 1024, 0, 1)) )
      matrix.np.write()
      time.sleep_ms(ms_out)

  def pixel_mask(buf):
    size = matrix.LED_NUM
    if len(buf) < matrix.LED_NUM:
      size = len(buf)
    for pix in range (0, size):
      if buf[pix]:
        matrix.np[pix] = matrix.hsv(*matrix.color)
    if matrix.INSTA_DRAW: matrix.show()
  
  def _add(a,b):
    w_a = int(len(a)/5)
    w_b = int(len(b)/5)
    out = [0] *len(a)
    for i in range(len(a)):
      out[i] = a[i]
    for i in range(5):
      out[(i*w_a+i*w_b):(i*w_a+i*w_b)] = b[(i*w_b):((i+1)*w_b)]
    return out

  def _get_frame(buffer, offest):
    w_buf = int(len(buffer)/5)
    out = [0] *25
    for x in range (5):
      for y in range (5):
        out[x + y * 5] = buffer[(x+offest)+(y*w_buf)]
    return out

  def _create_pixmap(input):
    spacer = [0] *5
    empty = [0] *25
    text_buffer = [0] *25
    for i in range (len(input)):
      text_buffer = matrix._add(text_buffer, font.get_letter( ord( input[len(input)-1-i] ) ) )
      text_buffer = matrix._add(text_buffer, spacer) 
    text_buffer = matrix._add(text_buffer, empty)
    return text_buffer

  def text_scroll(text_to_scroll, delay=150):
    t_buf = matrix._create_pixmap(text_to_scroll)
    #scrolling pixmap on matrix
    for pos in range ( int(len(t_buf)/5) -5 +1 ):
      matrix.clear_all()
      matrix.pixel_mask(matrix._get_frame(t_buf, pos) )
      matrix.show()
      time.sleep_ms(delay)


