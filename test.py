#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
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
        display.lcd_display_string("Greetings Human!", 1)  # Viết dòng văn bản lên dòng đầu tiên của màn hình
        display.lcd_display_string("Demo Pi Guy code", 2)  # Viết dòng văn bản lên dòng thứ hai của màn hình
        sleep(2)  # Chờ một khoảng thời gian để đọc tin nhắn
        display.lcd_display_string("I am a display!", 1)   # Làm mới dòng đầu tiên của màn hình với một thông điệp khác
        sleep(2)  # Chờ một khoảng thời gian để đọc tin nhắn
        display.lcd_clear()  # Xóa màn hình khỏi bất kỳ dữ liệu nào
        sleep(2)  # Chờ một khoảng thời gian để đọc tin nhắn
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")  # In ấn một thông báo chỉ định việc dọn dẹp
    display.lcd_clear()  # Xóa màn hình

