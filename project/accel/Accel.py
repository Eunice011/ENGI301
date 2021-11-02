"""
--------------------------------------------------------------------------
Accelerometer Test
--------------------------------------------------------------------------
License:   
Copyright 2021 Eunice 

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

Purpose: 
    
    Establish paramerters needed to use the accelerometer 

--------------------------------------------------------------------------
"""

import Adafruit_BBIO.ADC as ADC 
import time 

class Accel():
    analog_inx = None
    analog_iny = None
    analog_inz = None
    
    def __init__(self, analog_inx = "P1_21", analog_iny = "P1_23", analog_inz = "P1_25"):
        
        self.analog_inx = analog_inx
        self.analog_iny = analog_iny
        self.analog_inz = analog_inz
        
        self.setup()
        
    #End def
    
    def setup(self):
        ADC.setup()
    #End def
    
    def show_analog(self,direction):
        # outputs the analog value of the accelerometer in the specified direction 
        if direction == "x":
            value = ADC.read_raw(self.analog_inx)
        elif direction == "y":
            value = ADC.read_raw(self.analog_iny)
        elif direction == "z":
            value = ADC.read_raw(self.analog_inz)
        else:
            raise ValueError("Please choose a valid direction for the show_analog function input, valid directions: x,y,z")
        # End if 
        
        value = int(value)
        return value 
    #End def 
    
    def run(self):
        # output all three directional analog values 
        valuex = self.show_analog("x")
        valuey = self.show_analog("y")
        valuez = self.show_analog("z")
        value = [valuex, valuey, valuez]
        return value
    #End def
    
if __name__ == '__main__': 
    print("Program Start")
    accel = Accel()
    try:
        # run show_analog_value
        while True:
            (val) = accel.run()
            mean = (val[0]+val[1]+val[2])
            print (mean)
            time.sleep(0.01)
        #End for note mean = 12285 when nothing is moving

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        pass

        
        
    