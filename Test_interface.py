from microbit import *
import radio
import time

radio.on()
radio.config(group=1)
menuOpen = False
resetOption = False
count = 0
amountOfMilk = 0

display.show(Image.HEART)

while True:
      
    if button_a.is_pressed() and resetOption == False:
        display.clear()
        count = 1
        display.show(count)
        menuOpen = True

    while menuOpen == True:
        if button_a.is_pressed():
            display.clear()
            count -= 1
            display.show(count)
            sleep(500)
            print(count)
                
        elif button_b.is_pressed():
            display.clear()
            count += 1
            display.show(count)
            sleep(500)
            print(count)
    
        elif pin_logo.is_touched():
            start_time = time.ticks_ms()
            while pin_logo.is_touched():
                if time.ticks_ms() >= 2000:
                    display.clear()
                    amountOfMilk += count
                    break
            sleep(1000)
            display.scroll("Value :")
            display.scroll(amountOfMilk)
            menuOpen = False
            break

    if button_b.is_pressed() and menuOpen == False:
        display.scroll("Reset?")
        resetOption = True
        
    while resetOption == True:
        if button_a.is_pressed():
            display.clear()
            display.scroll("Cancelled")
            resetOption = False
            break
                
        elif button_b.is_pressed():
            display.clear()
            amountOfMilk = 0
            display.scroll("Count reset")
            resetOption = False
            break