# m5atom matrix library

folder [/lib](/lib) contains the main library file [**matrix.py**](/lib/matrix.py) responsible for handling the embedded rbg led matrix in m5atom matrix.  In addition, there is the helper library [**digits.py**](/lib/digits.py) containing pixmap data for numbers.



Simple examples of using this library can be found in the example.py files

## Sample application

Simple thermometer application using the dallas DS18B20 temperature sensor.  The program displays the temperature in two-digit form.  Due to the size of the led matrix (5x5) I did not implement the display of negative temperatures and greater than 99. I meant to show how you can display two digits at once on such a small display.  In this program, the second digit overlaps the first one covering its part.  The file [**example5.py**](example5.py) shows how to display the common part of overlapping digits in a different color.

To simplify the sensor connection, I used three outputs located next to the ground in the connector.  I used one of the inputs on the connector as a sensor power supply pin

connection diagram:

![schema.jpg](schema.jpg)


showing 28 degrees

![termo.jpg](termo.jpg)
