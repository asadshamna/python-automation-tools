import tkinter as tk
from tkinter import ttk, filedialog
import pywhatkit as kit
import threading

def send_message():
    phone_number = "+" + phone_numbers_entry.get()
    message = message_entry.get()
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())

    if image_path_var.get():
        send_single_message_with_image(phone_number, message, hour, minute, image_path_var.get())
    else:
        send_single_message(phone_number, message, hour, minute)

def send_single_message(phone_number, message, hour, minute):
    kit.sendwhatmsg_instantly(phone_number, message, hour, minute)

def send_single_message_with_image(phone_number, message, hour, minute, image_path):
    kit.sendwhatmsg(phone_number, message, int(hour), int(minute), image_path)

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    image_path_var.set(file_path)

root = tk.Tk()
root.title("WhatsApp Message Scheduler")

phone_numbers_label = ttk.Label(root, text="Phone Number:")
phone_numbers_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
phone_numbers_entry = ttk.Entry(root, width=30)
phone_numbers_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

message_label = ttk.Label(root, text="Message:")
message_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
message_entry = ttk.Entry(root, width=30)
message_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

hour_label = ttk.Label(root, text="Hour (24-hour format):")
hour_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
hour_entry = ttk.Entry(root, width=5)
hour_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

minute_label = ttk.Label(root, text="Minute:")
minute_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
minute_entry = ttk.Entry(root, width=5)
minute_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

image_path_var = tk.StringVar()

browse_button = ttk.Button(root, text="Browse Image", command=browse_image)
browse_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

send_button = ttk.Button(root, text="Send Message", command=lambda: threading.Thread(target=send_message).start())
send_button.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()
