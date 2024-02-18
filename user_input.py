import pywhatkit as kit
import time

def send_messages_to_multiple_users(phone_numbers, message, hour, minute):
    for phone_number in phone_numbers:
        kit.sendwhatmsg_instantly(phone_number, message, hour, minute)
        time.sleep(5)  
phone_numbers_input = input("Enter phone numbers (comma-separated) and add a (+) before each phone number: ").split(',')
message = input("Enter the message you want to send: ")
hour = int(input("Enter the hour (24-hour format): "))
minute = int(input("Enter the minute: "))
phone_numbers = [number.strip() for number in phone_numbers_input]
send_messages_to_multiple_users(phone_numbers, message, hour, minute)
