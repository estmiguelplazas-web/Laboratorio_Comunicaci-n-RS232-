1 import machine
2 import utime
3 from machine import Pin , UART
4
5 led = machine . Pin ("LED ", machine . Pin . OUT )
6 uart = UART (0 , baudrate =9600 , bits =8 , parity =0 , tx = Pin (0) , rx = Pin (1) )
7
8 while True :
9 led . on ()
10 uart . write ("U")
11 utime . sleep (1)
12 led . off ()
13 utime . sleep (1)
