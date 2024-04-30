#include <Wire.h>
#include <Servo.h>
#include <LiquidCrystal_I2C.h>
#include <MPU6050.h>

Servo servo;
MPU6050 mpu;

// Địa chỉ I2C của mô-đun LCD của bạn
int lcdAddress = 0x27; // Thay đổi địa chỉ này cho phù hợp với mô-đun LCD của bạn (thường là 0x27 hoặc 0x3F)

// Khởi tạo thư viện LiquidCrystal_I2C với địa chỉ LCD và số cột và hàng
LiquidCrystal_I2C lcd(lcdAddress, 16, 2);

void setup() {
  Serial.begin(115200); // Giao tiếp Arduino với máy tính 115200bits mỗi giây
  servo.attach(3);
  Wire.begin();
  mpu.initialize();
  mpu.setFullScaleAccelRange(MPU6050_ACCEL_FS_8);
  mpu.setFullScaleGyroRange(MPU6050_GYRO_FS_500);
  
  lcd.init();
  lcd.backlight(); // Bật đèn nền
  lcd.setCursor(0, 0);
  lcd.print("Goc nghieng: ");
  lcd.setCursor(3, 1);
  lcd.print("xOz= ");
}

void loop() {
  // Đọc giá trị gia tốc từ cảm biến
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);
  int value = ay;
  value = map(value, -5000, 5000, 180, 0); // Điều chỉnh phạm vi giá trị tùy thuộc vào cụm cảm biến MPU6050
  servo.write(value);
  char valueString[6]; // Định dạng chuỗi có thể chứa tối đa 5 chữ số và ký tự kết thúc chuỗi ('\0')
  sprintf(valueString, "%-3d", value); // Định dạng giá trị với chiều dài là 3, căn trái
  
  lcd.setCursor(8, 1); // Đặt con trỏ tới vị trí giá trị trục Y
  lcd.print(valueString);
  //Serial.println(X);
  Serial.println(value);
  //Serial.println(Z);
  delay(15);
}

