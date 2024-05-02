
import drivers  # Nhập mô-đun drivers
from time import sleep  # Nhập hàm sleep từ mô-đun time

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")  # In ấn một thông báo chỉ định việc ghi vào màn hình
        display.lcd_display_string("G", 1)  # Viết dòng văn bản lên dòng đầu tiên của màn hình
        display.lcd_display_string("D", 2)  # Viết dòng văn bản lên dòng thứ hai của màn hình
        sleep(2)  # Chờ một khoảng thời gian để đọc tin nhắn
        display.lcd_display_string("I", 1)   # Làm mới dòng đầu tiên của màn hình với một thông điệp khác
        sleep(2)  # Chờ một khoảng thời gian để đọc tin nhắn
        display.lcd_clear()  # Xóa màn hình khỏi bất kỳ dữ liệu nào
        sleep(2)  # Chờ một khoảng thời gian để đọc tin nhắn
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Clean!")  # In ấn một thông báo chỉ định việc dọn dẹp
    display.lcd_clear()  # Xóa màn hình

