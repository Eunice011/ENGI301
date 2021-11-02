"""
--------------------------------------------------------------------------
LED Strip Light library
--------------------------------------------------------------------------
License:   
Copyright 2021 Eunice Aissi 

Based on Code from:  https://github.com/rpliu3/ENGI301/tree/master/Project_01/code
Copyright 2019 Rebecca Liu

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
Software API:

  * opc.client ensures that server is running so that LED string can be displayed
  
--------------------------------------------------------------------------
Background Information: 
 
   * Base code for LED functions came from the following repositories:
        https://markayoder.github.io/PRUCookbook/01case/case.html#_neopixels_5050_rgb_leds_with_integrated_drivers_ledscape
        https://markayoder.github.io/PRUCookbook/06io/io.html#io_uio
        https://github.com/Yona-Appletree/LEDscape.git
        https://github.com/zestyping/openpixelcontrol
when called starts an led display 
"""

import time
import opc

class LED():
    ADDRESS = None
    STR_LEN = None
    leds    = None
    client  = None
    def __init__(self,ADDRESS= 'localhost:7890', STR_LEN = 240, leds = [(255, 255, 255)]):
        self.ADDRESS = ADDRESS
        self.STR_LEN = STR_LEN
        self.leds    = leds * STR_LEN
        self.client  = opc.Client(ADDRESS)
        self.setup()
    #End init
    
    def setup(self):
        # Create a client object
        # Test if it can connect
        if self.client.can_connect():
            print ('connected to %s' % self.ADDRESS)
        else:
            # We could exit here, but instead let's just print a warning
            # and then keep trying to send pixels in case the server
            # appears later
            print ('WARNING: could not connect to %s' % self.ADDRESS)
            
        # Define Pixel String
        
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
        time.sleep(1)
    #End setup 
    def loff(self):
        time.sleep(0.1)
        for j in range(self.STR_LEN):
            self.leds[j] = (0,0,0)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    def lneutral(self):
        #print("N")
        time.sleep(0.1)
        for j in range(self.STR_LEN):
            self.leds[j] = (255,255,255)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    def learth(self):
        #print("e")
        time.sleep(0.1)
        #built green led array
        for j in range(self.STR_LEN):
            self.leds[j] = (11, 195, 14)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End earth 
    def lwater(self):
        #print("wa")
        time.sleep(0.1)
        #built green led array
        for j in range(self.STR_LEN):
            self.leds[j] = (15, 146, 216)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def 
    def lwind(self):
        #print("wi")
        time.sleep(0.1)
        #built green led array
        for j in range(self.STR_LEN):
            self.leds[j] = (244, 235, 42)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def 
    def lfire(self):
        #print("f")
        time.sleep(0.1)
        #built green led array
        for j in range(self.STR_LEN):
            self.leds[j] = (237, 36, 9)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def 
    def lpink(self):
        #print("p")
        time.sleep(0.1)
        #built green led array
        for j in range(self.STR_LEN):
            self.leds[j] = (250, 26, 151)
        if not self.client.put_pixels(self.leds, channel=0):
            print ('not connected')
    #End def 
        
        
if __name__ == '__main__':    
    led = LED()
    try:
        led.lpink()
        time.sleep(2)
        led.learth()
        time.sleep(2)
        led.lwater()
        time.sleep(2)
        led.lwind()
        time.sleep(2)
        led.lfire()
        
    except KeyboardInterrupt:
        pass

    print("Program Complete.")        
