import pywhatkit as kit
import pandas as pd
import time
from datetime import datetime
import os

# Path to contacts file and message templates
contacts_file = 'contacts.csv'
templates_file = 'templates.csv'
scheduled_messages_file = 'scheduled_messages.csv'

# Load contacts
def load_contacts(file_path):
    df = pd.read_csv(file_path)
    # Remove duplicates
    df.drop_duplicates(subset='PhoneNumber', inplace=True)
    return df

# Load templates
def load_templates(file_path):
    df = pd.read_csv(file_path)
    return df

# Send a WhatsApp message
def send_whatsapp_message(phone_number, message, media_path=None):
    if media_path:
        kit.sendwhatmsg_to_group(phone_number, message, media_path)
    else:
        kit.sendwhatmsg(phone_number, message, time_hour=datetime.now().hour, time_min=datetime.now().minute + 1)

# Schedule a WhatsApp message
def schedule_message(phone_number, message, scheduled_time, media_path=None):
    current_time = datetime.now()
    wait_time = (scheduled_time - current_time).total_seconds()
    if wait_time > 0:
        time.sleep(wait_time)
    send_whatsapp_message(phone_number, message, media_path)

# Read scheduled messages and execute
def execute_scheduled_messages():
    df = pd.read_csv(scheduled_messages_file)
    for index, row in df.iterrows():
        phone_number = row['PhoneNumber']
        message = row['Message']
        scheduled_time = datetime.strptime(row['ScheduledTime'], '%Y-%m-%d %H:%M:%S')
        media_path = row.get('MediaPath')
        schedule_message(phone_number, message, scheduled_time, media_path)

# Example usage
if __name__ == "__main__":
    contacts = load_contacts(contacts_file)
    templates = load_templates(templates_file)

    # Example of sending a message
    for index, row in contacts.iterrows():
        phone_number = row['PhoneNumber']
        name = row['Name']
        # Personalize message using template
        for _, template in templates.iterrows():
            message = template['Message'].replace("{name}", name)
            send_whatsapp_message(phone_number, message)

    # Execute scheduled messages
    execute_scheduled_messages()
