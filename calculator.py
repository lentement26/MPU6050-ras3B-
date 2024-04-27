import math
from machine import Pin
import utime
import I2C_LCD_driver

a=0
matrix_char=[]

led_onboard =Pin(25,Pin.OUT)

lcd = I2C_LCD_driver.lcd()

#### KEY_PAD0 ####
matrix_keys = [['1', '2', '3', '+'],
               ['4', '5', '6', '-'],
               ['7', '8', '9', 'x'],
               ['AC', '0', '=', ':']]
               

row_pins = [2,3,4,5]
col_pins = [6,7,8,9]

for i in range(0,4):
    row_pins[i] = Pin(row_pins[i], Pin.OUT)
    row_pins[i].value(1)
for i in range(0,4):
    col_pins[i]=Pin(col_pins[i], Pin.IN, Pin.PULL_DOWN)
    col_pins[i].value(0)

####KEY_PAD1###########
    
matrix_keys1 = ['.', 'CHS', '%', 'SQRT']

Button_1 = Pin(10, Pin.IN, Pin.PULL_UP)

Button_2 = Pin(11, Pin.IN, Pin.PULL_UP)

Button_3 = Pin(12, Pin.IN, Pin.PULL_UP)

Button_4 = Pin(13, Pin.IN, Pin.PULL_UP)

######KEY_PAD2############
matrix_keys2 = ['MC', 'MR', 'M-', 'M+']

Button_1s = Pin(21, Pin.IN, Pin.PULL_UP)

Button_2s = Pin(20, Pin.IN, Pin.PULL_UP)

Button_3s = Pin(19, Pin.IN, Pin.PULL_UP)

Button_4s = Pin(18, Pin.IN, Pin.PULL_UP)

######## CE ###############
CE_key=['CE']
Button_5 = Pin(16,Pin.IN, Pin.PULL_UP)
   
print("Please enter a key from the keypad")

def calculator(matrix_char): #lay matrix_char lam bien 
    size=len(matrix_char)    # lay do dai cua matrix_char
    func=''					 # thuat toan 
    result=0				 # ket qua tinh toan
    result1=0				 # so dang truoc thuat toan
    result2=0				 # so dang sau thuat toan 
    number_before_char=[]	 # chuoi ki tu truoc thuat toan
    number_after_char=[]     # chuoi ki tu sau thuat toan 

    if '+' in matrix_char or '-' in matrix_char or 'x' in matrix_char or ':' in matrix_char :  # kiem tra xem trong matrix_char co thuat toan hay khong  
        for i in range(size):   # chay i de tim ra vi tri cua thuat toan
            if matrix_char[i] == '+' or matrix_char[i] == '-' or  matrix_char[i] == 'x' or matrix_char[i] == ':' :  # tim duoc vi tri thuat toan 
                func=matrix_char[i]  # gan func la thuat toan +, -, x hoac :
                for j in range(i):   
                    number_before_char.append(matrix_char[j])  # them cac ki tu truoc thuat toan vao 1 mang la number_before_char
                for k in range(i+1,size):
                    number_after_char.append(matrix_char[k])   # them cac ki tu sau thuat toan vao 1 mang la number_before_char
        

###############################################################
        
        if '%' in number_before_char :
            number_before_char = number_before_char[:-1]
            result1 = float(''.join(number_before_char)) 
            result1 = result1/100
            print(result1)
            print("Da xoa %")
            number_before_char.append('%')
            
            if '%' in number_after_char :
                number_after_char = number_after_char[:-1]
                result2 = float(''.join(number_after_char))
                result2 = result2/100
                number_after_char.append('%')
               
            if 'SQRT' in number_after_char :
                number_after_char = number_after_char[1:]
                result2 = float(''.join(number_after_char)) 
                result2 = math.sqrt(result2)
                number_after_char.insert(0,'SQRT')
                
            if  'SQRT' not in number_after_char and '%' not in number_after_char :
                result2 = float(''.join(number_after_char))
        
        if 'SQRT' in number_before_char :
            number_before_char = number_before_char[1:]
            result1 = float(''.join(number_before_char)) 
            result1 = math.sqrt(result1)
            number_before_char.insert(0,'SQRT')
            
            if '%' in number_after_char :
                number_after_char = number_after_char[:-1]
                result2 = float(''.join(number_after_char))
                result2 = result2/100
                number_after_char.append('%')
               
            if 'SQRT' in number_after_char :
                number_after_char = number_after_char[1:]
                result2 = float(''.join(number_after_char)) 
                result2 = math.sqrt(result2)
                number_after_char.insert(0,'SQRT')
                
            if  'SQRT' not in number_after_char and '%' not in number_after_char :
                result2 = float(''.join(number_after_char))
        
        if '%' not in number_before_char and 'SQRT' not in number_before_char :
            result1 = float(''.join(number_before_char))
            print('')
            print('Neu xoa % di')
            print(result1)
            if '%' in number_after_char :
                number_after_char = number_after_char[:-1]
                result2 = float(''.join(number_after_char))
                result2 = result2/100
                number_after_char.append('%')
               
            if 'SQRT' in number_after_char :
                number_after_char = number_after_char[1:]
                result2 = float(''.join(number_after_char)) 
                result2 = math.sqrt(result2)
                number_after_char.insert(0,'SQRT')
                
            if  'SQRT' not in number_after_char and '%' not in number_after_char :
                result2 = float(''.join(number_after_char))
            
            
        if func=='+':
            result= result1+result2
        if func=='-':
            result= result1-result2 
        if func=='x':
            result= result1*result2
        if func==':':
            result= result1/result2
    
        
####################################################################################
    else:
        if 'SQRT' in matrix_char:
            matrix_char =matrix_char[1:]
            result = float(''.join(matrix_char)) 
            result = math.sqrt(result)
            matrix_char.append('SQRT')
            
        if '%' in matrix_char :
            matrix_char = matrix_char[:-1]
            result = float(''.join(matrix_char))
            result = result/100
            matrix_char.append('%')
            
        if 'SQRT' not in matrix_char and '%' not in matrix_char : 
            result= float(''.join(matrix_char))
    
    
    return result
    
def get_key():
############KEY_PAD0###############
    global matrix_char 
    global a
    for row in range(4):
        for col in range(4):
            row_pins[row].high()
            if col_pins[col].value() == 1:
                key_press = matrix_keys[row][col]
                print("You have pressed:", matrix_keys[row][col])
                if key_press != '=' and key_press != 'AC' and key_press != 'MR':
                    matrix_char.append(key_press)
                    led_onboard.value(1)
                    chuoi_matrix=''.join(matrix_char)
                    lcd.lcd_display_string('                  ',1)
                    lcd.lcd_display_string(chuoi_matrix,1)
                    utime.sleep(0.3)
                    led_onboard.value(0)
                    utime.sleep(0.3)
                
                    
                else:
                    if key_press == '=':
                        
                        led_onboard.value(1)
                        utime.sleep(0.3)
                        led_onboard.value(0)
                        a=calculator(matrix_char)
                        print(a)
                        matrix_char.append('=')
                        chuoi_matrix=''.join(matrix_char)
                        lcd.lcd_display_string(chuoi_matrix,1)
                        lcd.lcd_display_string(str(a),2)
                        matrix_char.clear()
                        matrix_char.append(str(a))
                        print('Ket qua',a)
                    
                    if key_press == 'AC':
                        led_onboard.value(1)
                        utime.sleep(0.3)
                        led_onboard.value(0)
                        lcd.lcd_display_string('                  ',1)
                        lcd.lcd_display_string('                  ',2)
                        #matrix_char.clear()
                        #matrix_char.append(str(a))
                
        row_pins[row].low()
        
#################### PAD 1 ##################
    if Button_1.value() == 0:                           #### Nut "."
        print("You have pressed:", matrix_keys1[0])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        matrix_char.append('.')
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string(chuoi_matrix,1)
        utime.sleep(0.3)
        
    if Button_2.value() == 0:                     		### Nut CHS ####
        print("You have pressed:", matrix_keys1[1])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        a=calculator(matrix_char)
        a=-a
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string(chuoi_matrix,1)
        lcd.lcd_display_string(str(a),2)
        matrix_char.clear()
        matrix_char.append(str(a))
        utime.sleep(0.3)
    
    if Button_3.value() == 0:                           ### Nut % ###
        print("You have pressed:", matrix_keys1[2])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        matrix_char.append('%')
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string(chuoi_matrix,1)
        utime.sleep(0.3)
        
    if Button_4.value() == 0:                           ### Nut SQRT ####
        print("You have pressed:", matrix_keys1[3])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        matrix_char.append('SQRT')
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string(chuoi_matrix,1)
        utime.sleep(0.3)

####### KEY_PAD 2 ##################
    if Button_1s.value() == 0:                           #### Nut "MC"
        print("You have pressed:", matrix_keys2[0])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        led_onboard.value(1)
            
        lcd.lcd_display_string('                  ',1)
        lcd.lcd_display_string('                  ',2)
        matrix_char.clear()
        a=0
        utime.sleep(0.3)
        

    if Button_2s.value() == 0:                           ### Nut MR ####
        print("You have pressed:", matrix_keys2[1])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        matrix_char.append(str(a))
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string(chuoi_matrix,1)    
    
    if Button_3s.value() == 0:                           ### Nut M- ###
        print("You have pressed:", matrix_keys2[2])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        matrix_char.append('-')
        matrix_char.append(str(a))
        a=calculator(matrix_char)
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string(chuoi_matrix,1)
        lcd.lcd_display_string(str(a),2)
        matrix_char.clear()
        matrix_char.append(str(a))
        print('Ket qua',a)
        utime.sleep(0.3)
        
        
    if Button_4s.value() == 0:                           ### Nut M+ ####
        print("You have pressed:", matrix_keys2[3])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)
        matrix_char.append('+')
        matrix_char.append(str(a))
        a=calculator(matrix_char)
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string(chuoi_matrix,1)
        lcd.lcd_display_string(str(a),2)
        matrix_char.clear()
        matrix_char.append(str(a))
        print('Ket qua',a)
        utime.sleep(0.3)
#################### CE ############
    if Button_5.value() == 0 :
        print("You have pressed:", CE_key[0])
        led_onboard.value(1)
        utime.sleep(0.3)
        led_onboard.value(0)

        matrix_char = matrix_char[:-1]
        chuoi_matrix=''.join(matrix_char)
        lcd.lcd_display_string('                     ',1)  
        lcd.lcd_display_string(chuoi_matrix,1)  
      
while True:
    get_key()
    
