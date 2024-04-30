# Khai báo thư viện
import RPi.GPIO as GPIO
import smbus
from time import sleep
import drivers
display = drivers.Lcd()
# Thiết lập các chân GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Đặt chân của động cơ servo là chân đầu ra
GPIO.setup(4, GPIO.OUT)

pwm = GPIO.PWM(4, 50)
pwm.start(0)

# Một số thanh ghi MPU6050 và địa chỉ của chúng
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47

bus = smbus.SMBus(4)
Device_Address = 0x68  # Địa chỉ thiết bị MPU6050

def angle(Góc):
    duty = Góc / 18 + 2
    GPIO.output(4, True)
    pwm.ChangeDutyCycle(duty)
    #     sleep(1)
    GPIO.output(4, False)
    #     pwm.ChangeDutyCycle(0)

def setAngle():
    angle(90)

def MPU_Init():
    
    # Ghi vào thanh ghi tỷ lệ mẫu
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    # Ghi vào thanh ghi quản lý nguồn
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    # Ghi vào thanh ghi cấu hình
    bus.write_byte_data(Device_Address, CONFIG, 0)

    # Ghi vào thanh ghi cấu hình girosco
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    # Ghi vào thanh ghi cho phép ngắt
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    # Giá trị của Accelero và Gyro là 16 bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr + 1)
    
    # Ghép nối giá trị cao và giá trị thấp
    value = ((high << 8) | low)
        
    # Để lấy giá trị dấu từ mpu6050
    if(value > 32768):
        value = value - 65536
    return value

MPU_Init()

while True:
    # Đọc giá trị thô của Accelerometer
    acc_x = read_raw_data(ACCEL_XOUT)
    acc_y = read_raw_data(ACCEL_YOUT)
    acc_z = read_raw_data(ACCEL_ZOUT)

    # Đọc giá trị thô của Gyroscope
    gyro_x = read_raw_data(GYRO_XOUT)
    gyro_y = read_raw_data(GYRO_YOUT)
    gyro_z = read_raw_data(GYRO_ZOUT)

    Ax = acc_x / 16384.0
    Ay = acc_y / 16384.0 
    Az = acc_z / 16384.0

    Gx = gyro_x / 131.0
    Gy = gyro_y / 131.0
    Gz = gyro_z / 131.0

    # Bỏ chú thích dòng dưới đây để xem các giá trị của Accelerometer và Gyroscope
    #print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
       
    in_min = 1
    in_max = -1
    out_min = 0
    out_max = 180
    
    setAngle()  # Sử dụng hàm này để đặt điểm của động cơ servo
    
    # Chuyển đổi các giá trị trục Y của Accelerometer từ 0 đến 180   
    value = (Ay - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    value = int(value)
    print(value)
    display.lcd_display_string("hi", 1)
    if value >= 0 and value <= 180:
        # Ghi các giá trị này vào động cơ servo
        angle(value)  # Xoay động cơ servo sử dụng các giá trị cảm biến
        sleep(0.08)
