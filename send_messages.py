import pandas as pd
from telethon import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact
from telethon.errors import PhoneNumberInvalidError, UserNotMutualContactError
from config import Config

# Initialize the Telegram client
client = TelegramClient(Config.PHONE, Config.API_ID, Config.API_HASH)

# Load the Excel file
file_path = './list_of_people.xlsx'
df = pd.read_excel(file_path)

# Define the asynchronous function to send a personalized message
async def send_message(name, phone_number):
    message_body = f"""
    Hi {name}, Your message here
    """

    try:
        # Create a contact object
        contact = InputPhoneContact(client_id=0, phone=f"+{phone_number}", first_name=name.split()[0], last_name=" ".join(name.split()[1:]))
        # Import the contact
        result = await client(ImportContactsRequest([contact]))
        # Get the user entity
        if result.users:
            user = result.users[0]
            # Send the message to the user entity
            await client.send_message(user.id, message_body)
            print(f"Message sent to {name} (+{phone_number})")
        else:
            print(f"Failed to find user for phone number: +{phone_number}")

    except PhoneNumberInvalidError:
        print(f"Invalid phone number: +{phone_number}({name})")
    except UserNotMutualContactError:
        print(f"User is not a mutual contact: +{phone_number}({name})")
    except Exception as e:
        print(f"An error occurred for the user  +{phone_number}({name}): {str(e)}")

# Define the main asynchronous function to iterate over the DataFrame and send messages
async def main():
    await client.start()
    for _, row in df.iterrows():
        name = f"{row['First Name']} {row['Last Name']}"
        phone_number = row['Phone Number']
        await send_message(name, phone_number)

# Run the main function inside the event loop of the Telegram client
with client:
    client.loop.run_until_complete(main())