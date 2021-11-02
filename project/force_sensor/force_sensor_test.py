"""
--------------------------------------------------------------------------
Touch sensor test Library
--------------------------------------------------------------------------
License:   
Copyright 2021 Eunice Aissi 

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
Purpose:

    The purpose of this code is to test the force sensor in order
    for me to learn how to use it.
--------------------------------------------------------------------------

"""

import Adafruit_BBIO.ADC as ADC 
import time


class Force():
    # Define variables 
    analog_in1  = None
    
    def __init__(self, analog_in1="P1_19"):
        #Initialize Variables 
        self.analog_in1 = analog_in1
        
        self._setup()
        
    # End def 
    
    def _setup(self):
        #Set up hardware components 
        ADC.setup()
        
    #End def
    
    def show_force_value(self): 
        # prints the analog value of the force sensor 
        value = ADC.read_raw(self.analog_in1)
        value = int(value)
        return value
    #End def 
    
    def run(self):
        #run program 
        #get force sensor value 
        value = self.show_force_value()
        return value 
    #End def 
    
    
if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the Sword
    sword = Force()

    try:
        # run show_analog_value
        while True:
            (val) = sword.run()
            print(val)
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        pass
        