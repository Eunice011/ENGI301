"""
--------------------------------------------------------------------------
Sound libray
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

Class for sound effects 
total of 5 functions for each element 
when called it choses a random sound within the right element and plays it

--------------------------------------------------------------------------
"""

import os 
import random

class Sound():

    def __init__(self):
        self.setup()
    #End init
    
    def setup(self):
        #nothing for now 
        pass
    #End setup
    
    def searth(self):
        r= random.randint(1,4)
        sound_file = "earth"+str(r)+".mp3"
        print(sound_file)
        os.system("{0} {1}/{2}".format("mplayer", "/var/lib/cloud9/ENGI301/project/Sound", sound_file))
    #End searth 
    
    def swater(self):
        # choose a random earth sound to play
        r = random.randint(1,4)
        sound_file = "water"+str(r)+".mp3"
        os.system("{0} {1}/{2}".format("mplayer", "/var/lib/cloud9/ENGI301/project/Sound", sound_file))
    #End searth 
    
    def swind(self):
        # choose a random earth sound to play
        r = random.randint(1,4)
        sound_file = "wind"+str(r)+".mp3"
        os.system("{0} {1}/{2}".format("mplayer", "/var/lib/cloud9/ENGI301/project/Sound", sound_file))
    #End searth 
    
    def sfire(self):
        # choose a random earth sound to play
        r = random.randint(1,4)
        sound_file = "fire"+str(r)+".mp3"
        os.system("{0} {1}/{2}".format("mplayer", "/var/lib/cloud9/ENGI301/project/Sound", sound_file))
    #End searth 
    
    def spink(self):
        # choose a random earth sound to play
        r = random.randint(1,4)
        sound_file = "pink"+str(r)+".mp3"
        os.system("{0} {1}/{2}".format("mplayer", "/var/lib/cloud9/ENGI301/project/Sound", sound_file))
    #End searth 
    
    def run(self):
        pass 


if __name__ == '__main__':
    
    print("Program Start")
    
    # Create instantiation of the lock
    sound = Sound()
    
    try:
        # Run the people counter
        sound.searth()
    
    except KeyboardInterrupt:
        # Clean up hardware when exiting
        pass
    
    print("Program Complete")
