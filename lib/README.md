# m5atom library files
Short &amp; simple micropython scripts for **M5atom Matrix**

## matrix.py
Simple library using m5atom builtin 5x5 addressable led  matrix

usage model:
- import library (once)
- initialize matrix (once)
- set drawing color
- draw/clear pixels/mask
- show changes you made on matrix

example:
```
#import library
import matrix
#create scr object
scr = matrix.matrix

#initialize matrix
scr.init()

#clear matrix
scr.clear_all()

#set active color
scr.pixel_color(120)
#set pixels with given color
scr.pixel_set(0,0)
scr.pixel_set(1,1)
scr.pixel_set(2,2)
scr.pixel_clear(1,1)
#show changes on matrix
scr.show()
```

list of library functions:


```
init()
```
Initialize led matrix. Run it once before using other functions from this library

parameters:

**none**


```
show()
```
Function show/draw to matrix changes made you by other drawing function

parameters:

**none**


```
pixel_color(h, s=1, v=1):
```
Set color who been used for the next drawing function, Color is set in HSV color model


parameters:

**h** - color number from color wheel (0 - 360)

**s** - optionally color saturation (0-1.0)

**v** - optionally color value (brightness of color) (0-1.0)

```
pixel_set(x, y):
```
Set given coordinates pixel to color 


parameters:

**x** - x coordinate (0-4)

**y** - y coordinate (0-4)

```
pixel_clear(x, y):
```
Clear given coordinates pixel


parameters:

**x** - x coordinate (0-4)

**y** - y coordinate (0-4)

```
pixel_blink(x, y, delay_ms=100 )
```
Blink given coordinates pixel. Preserve previous color of pixel after blink


parameters:

**x** - x coordinate (0-4)

**y** - y coordinate (0-4)

**delay_ms** - optionally blink time of pixel in miliseconds

```
pixel_breathe(x, y, ms_in=50, ms_out=50)
```
Breathe pixel effect at given coordinates pixel. This is blocking function using **time.sleep_ms()**. Total duration of efect is **11**×**ms_in + 11**×**ms_out**.


parameters:

**x** - x coordinate (0-4)

**y** - y coordinate (0-4)

**ms_in** - optionally breathe in effect step time in miliseconds

**ms_out** - optionally breathe out effect step time in miliseconds


```
pixel_mask(buf)
```
Seting pixels on matrix according to buffer containing pixmap. Function set only pixels on matrix with value greater on equal 1. Other pixels are not affected (preserve previous value). If length of **buf** is less than number of leds in matrix, the only partial leds in matrix will be set.

parameters:

**buf** - aray of pixels to set (0 - no change pixel, 1 or greater - set pixel )

example_buf = [
  0,0,0,0,0,
  0,1,0,1,0,
  0,0,0,0,0,
  1,0,0,0,1,
  0,1,1,1,0
  ]

```
write_buffer(buf)
```
Seting pixels color in RGB color. Function Function overwrite old color values. If length of **buf** is less than number of leds in matrix, the only partial leds in matrix will be set.

parameters:

**buf** - aray of rgb colors to set (red, green, blue )

example_buf = [
  (0,0,255),(0,0,255),(0,0,255),(0,0,255),(0,0,255),
  (0,0,255),(0,0,0),(0,0,0),(0,0,0),(0,0,255),
  (0,0,255),(0,0,),(255,255,255),(0,0,0),(0,0,255),
  (0,0,255),(0,0,0),(0,0,0),(0,0,0),(0,0,255),
  (0,0,255),(0,0,255),(0,0,255),(0,0,255),(0,0,255)
  ]

```
text_scroll(text_to_scroll, delay=150)
```
Display scrolling text on matrix display.

parameters:

**text_to_scroll** - text to scroll and display.

**delay** - optionally delay in ms between next frames of scrolling text, default is 150ms

## fonts.py
This is a helper library for function ```text_scroll()``` from **matrix.py** library. It contains pixmaps data for ascii characters codes from 32 to 127.

```
get_letter(asci)
```
Return pixmap data of character for given ascii code. Return pixmaps for ascii codes in range 32 to 127. If ascii code value is beyound of range 32-127 return empty pixmap.

parameters:

**asci** - number of character ascii code

## digits.py
This library contains three pixmaps array of digits from 0 to 9. Digits size: width = 3 pixel, weight = 5 pixel. 


```
digits_left = [ ...... ]
```
Contain pixmap of digits displayed on left side of matrix (column: 0,1,2)

```
digits_right = [ ...... ]
```
Contain pixmap of digits displayed on right side of matrix (column: 2,3,4)

```
digits_center = [ ...... ]
```
Contain pixmap digits displayed on center of matrix (column: 1,2,3)

```
get_digit(position, data)
```
Function return pixmap of given number of digit from given pixmap array.

parameters:

**position** - number of digit (from 0 to 9)

**data** - array of pixmaps which pixmap are returned. you can use **digits_left**, **digits_right**, **digits_center** or name of other array you are created.

