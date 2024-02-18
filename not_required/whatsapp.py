import pywhatkit as kit

phone_number = "+8779375502"
message = "Hello from Python WhatsApp Automation! This is a testing message for individual person."

kit.sendwhatmsg_instantly(phone_number, message, 19, 59)