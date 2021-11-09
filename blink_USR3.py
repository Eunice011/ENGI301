"""
--------------------------------------------------------------------------
Python Code to Blink the USER 3 LED at 5Hz
--------------------------------------------------------------------------
License:   
Copyright 2021 Eunice Aissi 

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Code that will 
  - continously blink the USR3 LED on a pockebeagle Black board 
  - Repeats

Note:
  - The LED starts blinking as soon as the code is started 
  - LED does not stop blinking
  - Frequency = 5Hz 

Error conditions:
  - Can't contact LED --> prints 'Failed' and exists code 

--------------------------------------------------------------------------
"""
# import the adafruit gpio library sicne I want to control a gpio pin 
import Adafruit_BBIO.GPIO as GPIO
#import the time library to allow me to measure time 
import time
#set up the user 3 led as an output pin
GPIO.setup("USR3", GPIO.OUT)
#the while statement ensures that the led keeps blinking 
while True:
    try: # try to blink the led
        GPIO.output("USR3",GPIO.HIGH) # turn on the led
        time.sleep(0.1)# wait 0.1 seconds since the frequency is 5 full on/off cycles per second 
        GPIO.output("USR3", GPIO.LOW) # after 0.1 seconds turn off the led 
        time.sleep(0.1)# wait for 0.1 seconds
        #repeat
    except:# if something goes wrong 
        print("Failed") # print "failed"
        break # and break out of the while loop to stop the program


