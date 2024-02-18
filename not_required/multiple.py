import pywhatkit as kit
import time

def send_messages_to_multiple_users(phone_numbers, message, hour, minute):
    for phone_number in phone_numbers:
        kit.sendwhatmsg_instantly(phone_number, message, hour, minute)
        time.sleep(5)  
phone_numbers = ["+9967795512", "+7738706611", "+8779375502"]

message = "Hello from Shamna's WhatsApp Automation! This is a testing message for multiple users. Thank you for becoming part of my testing."


send_messages_to_multiple_users(phone_numbers, message, 19, 49)
