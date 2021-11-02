"""
--------------------------------------------------------------------------
Cosplay Sword Main Code
--------------------------------------------------------------------------
License:   
Copyright 2021 Eunice Aissi 

Based on library from

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Purpose: The purpose of this project is to create an LED sword that can be used 
as part of a costplay outfit. The sword has 6 modes, four elemental modes, one 
neutral mode, and one pink mode. In each swrod mode different LED displays and
sound effects are emitted to match with the mode. For example, water mode will 
turn the sword blue with water flowing sound effects whenever the sword is moved.
Lastly the sword has two main modes for how the user interacts with it: 
Chosen mode - The Effects only appear while the handle is gripped
Muggle mode - The effects remain regardless the handle being gripped
Sensors: Force Sensor, accelerometer, button
Actuators: Servo, LED strip lights, speakers 
--------------------------------------------------------------------------

Functions:
    - On start up the sword is white to indicate neutral mode
--------------------------------------------------------------------------
"""

import os
import time
import random 
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import sound as SOUND
import LED as LED
import threading
#import sound class
#import LED class 

#Constants 
SG90_FREQ   = 50 #50                  # 20ms period (50Hz)
SG90_POL    = 0                   # Rising Edge polarity
SG90_OFF    = 0                   # 0ms pulse -- Servo is inactive
SG90_RIGHT  = 5 #5                  # 1ms pulse (5% duty cycle)  -- All the way right
SG90_LEFT   = 10 #10                 # 2ms pulse (10% duty cycle) -- All the way Left
# Global variables 

class Sword(): 
    servo      = None # Servo
    analog_in1 = None # Force sensor 
    analog_inx = None # Accelerometer x
    analog_iny = None # Acceleromenter y
    analog_inz = None # Accelerometer z
    button     = None # Button
    timing     = None # timing duration intervals 
    wings      = None # boolean that monitors the wings status False = closed
    accel_sen  = None # accelerometer sensitivity factor
    accel_max  = None # max accelerometer output value should always = 12285
    force_sen  = None # force sensor sensitivity 
    force_max  = None # force 
    sound      = None # sound class 
    #function   = None
    #stand in LEDS
    neutral    = None
    earth      = None
    wind       = None
    water      = None 
    fire       = None 
    #pink = White + red 
    
    def __init__(self, servo="P1_36", analog_in1="P1_19", analog_inx="P1_21", 
                        analog_iny="P1_23", analog_inz="P1_25", button="P1_2",
                        timing=2.0, neutral="P2_10",earth="P2_17", wind="P2_6",
                        water="P2_4", fire="P2_2", wings=False, accel_sen = 2,
                        accel_max = 12285, force_sen=1, force_max=4095, accel_sen2=10,
                        ):
        self.servo = servo
        self.analog_in1 = analog_in1
        self.analog_inx = analog_inx
        self.analog_iny = analog_iny
        self.analog_inz = analog_inz
        self.button     = button
        self.timing     = timing
        self.wings      = wings 
        self.accel_sen  = accel_sen
        self.accel_max  = accel_max
        self.force_sen  = force_sen
        self.force_max  = force_max
        self.sound      = SOUND.Sound()
        self.led        = LED.LED()
        self.neutral    = neutral
        self.earth      = earth
        self.water      = water
        self.wind       = wind
        self.fire       = fire
        
        #run setup function on initiation 
        #threading.Thread.__init__(self)
        self.setup()
    #End def
    
    def setup(self): # white led on and wings closed 
        ADC.setup() # setup force sensors and accelerometers analog inputs 
        PWM.start(self.servo, SG90_OFF, SG90_FREQ, SG90_POL) # servo set up
        PWM.set_duty_cycle(self.servo, SG90_OFF)
        GPIO.setup(self.button, GPIO.IN) # setup button pin 
        GPIO.setup(self.neutral, GPIO.OUT) # Temps LEDS
        GPIO.setup(self.earth, GPIO.OUT)
        GPIO.setup(self.wind, GPIO.OUT)
        GPIO.setup(self.water, GPIO.OUT)
        GPIO.setup(self.fire, GPIO.OUT)
        #for full code make all the leds white 
        GPIO.output(self.neutral, GPIO.HIGH)
        GPIO.output(self.earth, GPIO.LOW)
        GPIO.output(self.wind, GPIO.LOW)
        GPIO.output(self.water, GPIO.LOW)
        GPIO.output(self.fire, GPIO.LOW)
        self.led.lneutral()
    #End def
    def close(self):
        # close the wings 
        PWM.set_duty_cycle(self.servo, SG90_LEFT)
        time.sleep(1)
        PWM.set_duty_cycle(self.servo,SG90_OFF)
        # check later
    #End def
    
    def openw(self):
        # open the wings 
        PWM.set_duty_cycle(self.servo, SG90_RIGHT)
        time.sleep(1)
        PWM.set_duty_cycle(self.servo,SG90_OFF)
        # check later 
    #End def
    
    def accel_analog(self,direction):
        # outputs the analog value of the accelerometer in the specified direction 
        if direction == "x":
            value = ADC.read_raw(self.analog_inx)
        elif direction == "y":
            value = ADC.read_raw(self.analog_iny)
        elif direction == "z":
            value = ADC.read_raw(self.analog_inz)
        elif direction == "m":
            value = ADC.read_raw(self.analog_inx)+ADC.read_raw(self.analog_iny)+ADC.read_raw(self.analog_inz)
        else:
            raise ValueError("Please choose a valid direction for the show_analog function input, valid directions: x,y,z,m")
        # End if 
        
        value = int(value)//self.accel_sen
        return value 
    #End def 
    
    def force_analog(self):
        value = ADC.read_raw(self.analog_in1)
        value = int(value)//self.force_sen
        return value
    #End def 
    
    def button_press(self, function=None):
        """Button press
               - Optional function to execute while waiting for the button to be pressed
                 - Returns the last value of the function when the button was pressed
               - Waits for a full button press
               - Returns the time the button was pressed as tuple
        """
        button_press_time            = 0.0                 # Time button was pressed (in seconds)
        ret_val                      = None                # Optional return value for provided function

        # Optinally execute function pointer that is provided
        #   - This is so that function is run at least once in case of a quick button press
        if function is not None:
            ret_val = function()
        # Wait for button press
        while(GPIO.input(self.button) == 1):
            # Optinally execute function pointer that is provided
            if function is not None:
                ret_val = function()

            # Sleep for a short period of time to reduce CPU load
            time.sleep(0.1)

        # Record time
        button_press_time = time.time()

        # Wait for button release
        while(GPIO.input(self.button) == 0):
            # Sleep for a short period of time to reduce CPU load
            time.sleep(0.1)

        # Compute button press time
        button_press_time = time.time() - button_press_time

        # Return button press time and optionally ret_val
        if function is not None:
            return (button_press_time, ret_val)
        else:
            return (button_press_time)

    # End def
    
    def Neutral(self):
        # Neutral mode, all leds are white and the wings are closed 
        #set all leds to white / temp set white led on and everythign else off 
        GPIO.output(self.neutral, GPIO.HIGH)
        GPIO.output(self.earth, GPIO.LOW)
        GPIO.output(self.wind, GPIO.LOW)
        GPIO.output(self.water, GPIO.LOW)
        GPIO.output(self.fire, GPIO.LOW)
        self.led.lneutral()
        #check if the wings are open using the boolean
        # if they are open close wings, else do nothing 
        if self.wings == True :
            self.close()
            self.wings = False
        else:
            pass
    #End def 
    
    def Earth(self):
        # start earth led display sequence 
        # if the sword is swung output a random sound effect 
        # if the button is pressed at anytime exit the program 
        #temp code 
        GPIO.output(self.neutral, GPIO.LOW)
        GPIO.output(self.earth, GPIO.HIGH)
        GPIO.output(self.wind, GPIO.LOW)
        GPIO.output(self.water, GPIO.LOW)
        GPIO.output(self.fire, GPIO.LOW)
        self.led.learth()
        time.sleep(0.1)
        # while the accelerometer is moving
        while True:
            if (self.accel_analog("m") == self.accel_max//self.accel_sen):
                #print("still")
                # Temp code - while the sword is not moving turn off the other leds 
                GPIO.output(self.neutral, GPIO.LOW)
                GPIO.output(self.earth, GPIO.HIGH)
                GPIO.output(self.wind, GPIO.LOW)
                GPIO.output(self.water, GPIO.LOW)
                GPIO.output(self.fire, GPIO.LOW)
                self.led.learth()
            if (self.accel_analog("m") != self.accel_max//self.accel_sen):
                # print(self.accel_analog("m"))
                # output a sound 
                # keep led display going 
                # for temporary code turn on all leds
                
                GPIO.output(self.neutral, GPIO.HIGH)
                GPIO.output(self.earth, GPIO.HIGH)
                GPIO.output(self.wind, GPIO.HIGH)
                GPIO.output(self.water, GPIO.HIGH)
                GPIO.output(self.fire, GPIO.HIGH)
                self.led.learth()
                self.sound.searth()
                
                
            if GPIO.input(self.button) == 0:
                break
                
        print("Exiting Earth")        
    #End def
    
    def Wind(self):
        # start earth led display sequence 
        # if the sword is swung output a random sound effect 
        #temp code 
        GPIO.output(self.neutral, GPIO.LOW)
        GPIO.output(self.earth, GPIO.LOW)
        GPIO.output(self.wind, GPIO.HIGH)
        GPIO.output(self.water, GPIO.LOW)
        GPIO.output(self.fire, GPIO.LOW)
        self.led.lwind()
        time.sleep(0.1)
        # while the accelerometer is moving
        while True:
            if (self.accel_analog("m") == self.accel_max//self.accel_sen):
                #print("still")
                # Temp code - while the sword is not moving turn off the other leds 
                GPIO.output(self.neutral, GPIO.LOW)
                GPIO.output(self.earth, GPIO.LOW)
                GPIO.output(self.wind, GPIO.HIGH)
                GPIO.output(self.water, GPIO.LOW)
                GPIO.output(self.fire, GPIO.LOW)
                self.led.lwind()
            if (self.accel_analog("m") != self.accel_max//self.accel_sen):
                # print(self.accel_analog("m"))
                # output a sound 
                # keep led display going 
                # for temporary code turn on all leds
                
                GPIO.output(self.neutral, GPIO.HIGH)
                GPIO.output(self.earth, GPIO.HIGH)
                GPIO.output(self.wind, GPIO.HIGH)
                GPIO.output(self.water, GPIO.HIGH)
                GPIO.output(self.fire, GPIO.HIGH)
                self.led.lwind()
                self.sound.swind()
                
            if GPIO.input(self.button) == 0:
                break
        print("Exiting Wind")
    #End def
    
    def Water(self):
        # start earth led display sequence 
        # if the sword is swung output a random sound effect 
        #temp code 
        GPIO.output(self.neutral, GPIO.LOW)
        GPIO.output(self.earth, GPIO.LOW)
        GPIO.output(self.wind, GPIO.LOW)
        GPIO.output(self.water, GPIO.HIGH)
        GPIO.output(self.fire, GPIO.LOW)
        self.led.lwater()
        time.sleep(0.1)
        # while the accelerometer is moving
        while True:
            if (self.accel_analog("m") == self.accel_max//self.accel_sen):
                #print("still")
                # Temp code - while the sword is not moving turn off the other leds 
                GPIO.output(self.neutral, GPIO.LOW)
                GPIO.output(self.earth, GPIO.LOW)
                GPIO.output(self.wind, GPIO.LOW)
                GPIO.output(self.water, GPIO.HIGH)
                GPIO.output(self.fire, GPIO.LOW)
                self.led.lwater()
            if (self.accel_analog("m") != self.accel_max//self.accel_sen):
                # print(self.accel_analog("m"))
                # output a sound 
                # keep led display going 
                # for temporary code turn on all leds
                
                GPIO.output(self.neutral, GPIO.HIGH)
                GPIO.output(self.earth, GPIO.HIGH)
                GPIO.output(self.wind, GPIO.HIGH)
                GPIO.output(self.water, GPIO.HIGH)
                GPIO.output(self.fire, GPIO.HIGH)
                self.led.lwater()
                self.sound.swater()
                
            if GPIO.input(self.button) == 0:
                break
        print("Exiting Water")
    #End def
    
    def Fire(self):
        # start earth led display sequence 
        # if the sword is swung output a random sound effect 
        #temp code 
        GPIO.output(self.neutral, GPIO.LOW)
        GPIO.output(self.earth, GPIO.LOW)
        GPIO.output(self.wind, GPIO.LOW)
        GPIO.output(self.water, GPIO.LOW)
        GPIO.output(self.fire, GPIO.HIGH)
        self.led.lfire()
        time.sleep(0.1)
        # while the accelerometer is moving
        while True:
            if (self.accel_analog("m") == self.accel_max//self.accel_sen):
                #print("still")
                # Temp code - while the sword is not moving turn off the other leds 
                GPIO.output(self.neutral, GPIO.LOW)
                GPIO.output(self.earth, GPIO.LOW)
                GPIO.output(self.wind, GPIO.LOW)
                GPIO.output(self.water, GPIO.LOW)
                GPIO.output(self.fire, GPIO.HIGH)
                self.led.lfire()
            if (self.accel_analog("m") != self.accel_max//self.accel_sen):
                # print(self.accel_analog("m"))
                # output a sound 
                # keep led display going 
                # for temporary code turn on all leds
                
                GPIO.output(self.neutral, GPIO.HIGH)
                GPIO.output(self.earth, GPIO.HIGH)
                GPIO.output(self.wind, GPIO.HIGH)
                GPIO.output(self.water, GPIO.HIGH)
                GPIO.output(self.fire, GPIO.HIGH)
                self.led.lfire()
                self.sound.sfire()
                
            if GPIO.input(self.button) == 0:
                break
        print("Exiting Fire")
    #End def
    
    def Pink(self):
        # start earth led display sequence 
        # if the sword is swung output a random sound effect 
        # if button is pressed >4s turn off sound effects no way to do this right now 
        # if buttoon pressed >4s again turn on sound effects 
        #temp code 
        GPIO.output(self.neutral, GPIO.HIGH)
        GPIO.output(self.earth, GPIO.LOW)
        GPIO.output(self.wind, GPIO.LOW)
        GPIO.output(self.water, GPIO.LOW)
        GPIO.output(self.fire, GPIO.HIGH)
        self.led.lpink()
        time.sleep(0.1)
        # while the accelerometer is moving
        while True:
            if (self.accel_analog("m") == self.accel_max//self.accel_sen):
                #print("still")
                # Temp code - while the sword is not moving turn off the other leds 
                GPIO.output(self.neutral, GPIO.HIGH)
                GPIO.output(self.earth, GPIO.LOW)
                GPIO.output(self.wind, GPIO.LOW)
                GPIO.output(self.water, GPIO.LOW)
                GPIO.output(self.fire, GPIO.HIGH)
                self.led.lpink()
            if (self.accel_analog("m") != self.accel_max//self.accel_sen):
                # print(self.accel_analog("m"))
                # output a sound 
                # keep led display going 
                # for temporary code turn on all leds
                
                GPIO.output(self.neutral, GPIO.HIGH)
                GPIO.output(self.earth, GPIO.HIGH)
                GPIO.output(self.wind, GPIO.HIGH)
                GPIO.output(self.water, GPIO.HIGH)
                GPIO.output(self.fire, GPIO.HIGH)
                self.led.lpink()
                self.sound.spink()
                
            if GPIO.input(self.button) == 0:
                break
        print("Exiting Pink")
    #End def
    
    def cleanup(self):
        # Clean up GPIOs
        GPIO.output(self.neutral, GPIO.LOW)
        GPIO.output(self.earth, GPIO.LOW)
        GPIO.output(self.wind, GPIO.LOW)
        GPIO.output(self.water, GPIO.LOW)
        GPIO.output(self.fire, GPIO.LOW)
        self.led.loff()

        # Clean up GPIOs
        GPIO.cleanup()

        # Stop servo
        PWM.stop(self.servo)
        PWM.cleanup()
    #End def 
    # runs of the element functions depending on their assigned number
    def rand(self,r):
        if r == 1:
            self.Earth()
        if r == 2:
            self.Water()
        if r == 3:
            self.Wind()
        if r == 4:
            self.Fire()
        if r == 5:
            self.Pink()
        #End ifs 
    #End def 
    
    def run(self):
        i = -1
        while True:
            # main script which controls user interaction 
            # signal flow (muggle vs chosen in main script)
            # check if the touch sensor is touched
            if self.force_analog() != self.force_max//self.force_sen:
                # if the touch sensor is touched open wings and assign a random element
                if self.wings == False: #if the wings are closed
                    # open wings 
                    self.openw()
                    self.wings=True # set wing status to open 
                    time.sleep(2)
                #End if 
                for j in range(1):
                    # assign a random element 
                    r = random.randint(1,5)
                    r = int(r)
                    #print(r)
                    # when this is called the chosen element fucntion runs until
                    # a button press
                    self.rand(r)
                    #print("exit 2") 
                    #when the button is pressed wait 1 second 
                    time.sleep(1)
                #End for 
                
            #if the button is clicked again cycle through element options 
            
            if GPIO.input(self.button) == 0:
                time.sleep(0.2)
                #print("button")
                #time.sleep(0.1)
                if i == 5:
                    i=-1
                #End if
                i = i+1
                self.rand(i) 
            #End if 
            #End while
        #End if 
                
            
            
            
            
            
        
         
        # check if the button is clicked
        # if the button is clicked cycle through the element choices led change colors
        # according the mode 
        # click for more than 2 seconds to choose a mode 
        # move sword makes sound effects 
        # if button is pressed at anytime you can change modes 
    
    #End def 
  
  
if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the sword
    # runs setup and initiation functions 
    # turns on white led and closes flower if it is open 
    sword = Sword()
    # chose muggle or chosen mode 
    
    # run program 
    """elements = (sword.Neutral(),sword.Earth(),sword.Water(),sword.Wind(),sword.Fire(),sword.Pink())
    i=1"""

    try:

        # Run the program
        """sword.Neutral()
        time.sleep(5)
        sword.Earth()
        time.sleep(2)
        sword.Water()
        time.sleep(2)
        sword.Wind()
        time.sleep(2)
        sword.Fire()
        time.sleep(2)
        sword.Pink()
        time.sleep(2)"""
        """elements[i]
        time.sleep(1)"""
        sword.run()
        time.sleep(1)

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        sword.cleanup()

    print("Program Complete")

    
    
    
                
                
                
            
        
        
        
        
    
    
    
        
             
        
    