
from pyfirmata import Arduino,util,OUTPUT,INPUT
from morse.Morse_Decoder import Morse_Decoder,MORSE_ENCODING
from time import time
from typing import List

#This is a new comment

COM_PORT = 'COM3'





def main():
    dec = Morse_Decoder(print,time())
    board = Arduino(COM_PORT)
    it = util.Iterator(board)
    ldr_pin = board.get_pin('a:0:i')
    it.start()
 
    while(ldr_pin.read() is None):
        pass
    print("Ready")
    
    while True:
        
        val = ldr_pin.read()

        #buttone reads
        #thermistor reads etc.
        if(val is not None):
            #print(val,dec.state)
            if(dec.get_signal(val > 0.5,time())):
                break
            









if __name__ == "__main__":
    main()


