import lcd2  # Importing the LiquidCrystal_I2C module
from time import sleep  # Importing the sleep function from the time module

lcd = lcd2.lcd()  # Initializing the LCD object
lcd.clear()  # Clearing the LCD screen
lcd.display("Testing....", 1, 0)  # Displaying "Testing...." on the first line of the LCD
sleep(1)  # Waiting for 1 second
lcd.clear()  # Clearing the LCD screen

# Loop to display '*' moving from left to right on the LCD screen
for j in range(1, 3):  # Loop for the LCD lines
    for i in range(16):  # Loop for LCD columns
        lcd.display("*", j, i)  # Displaying '*' at the current position on the LCD
        sleep(0.1)  # Waiting for 0.1 seconds between each '*' display
lcd.clear()  # Clearing the LCD screen

# Infinite loop to continuously display user input on the LCD
while True:
    try:
        lcd.display("Enter String you", 1, 0)  # Displaying a message prompting the user to enter a string
        lcd.display("want to display", 2, 0)  # Displaying another message on the second line
        sleep(1)  # Waiting for 1 second
        user_input = input("Enter String You Want to Display")  # Taking user input
        lcd.display(user_input, 1, 0)  # Displaying the user input on the first line of the LCD
        sleep(2)  # Waiting for 2 seconds
        lcd.clear()  # Clearing the LCD screen
    except KeyboardInterrupt:  # Handling KeyboardInterrupt to exit the loop when Ctrl+C is pressed
        break  # Exiting the loop
