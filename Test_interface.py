# Imports go at the top
from microbit import *
import radio

radio.on()
radio.config(group=23)
menuOpen = False
wasTouched = False
count = 0

display.show(Image.HEART)

while True:
    if button_a.is_pressed():
        count = 0
        display.show(count)
        menuOpen = True

        while menuOpen == True:
            if button_a.is_pressed():
                display.clear()
                count -= 1
                display.show(count)
                sleep(1000)
                print(count)
            elif button_b.is_pressed():
                display.clear()
                count += 1
                display.show(count)
                sleep(1000)
                print(count)
            elif pin_logo.is_touched():
                start_time = running_time()
                while pin_logo.is_touched():
                    if running_time() - start_time >= 2000:
                        display.clear()
                        break
                    sleep(1000)
                    break
                
        
            
                
            
            
                
        
        
        
        
    
