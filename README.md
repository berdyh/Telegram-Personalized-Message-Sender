# Telegram Personalized Message Sender

This repository contains a Python script that sends personalized Telegram messages to users using their phone numbers. The script reads names and phone numbers from an Excel file (`list_of_people.xlsx`) and sends each person a customized invitation message.

## Features

- Reads recipient data from an Excel file
- Sends personalized messages to recipients via Telegram
- Supports Markdown formatting for messages

## Prerequisites

- Python 3.x
- A Telegram account
- Telegram API credentials (API ID and API hash)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/berdyh/Telegram-Personalized-Message-Sender.git
    cd telegram-message-sender
    ```

2. Install the required Python packages:

    ```sh
    pip install pandas telethon openpyxl
    ```

3. Create a Telegram application to get your API ID and API hash. You can do this at [my.telegram.org](https://my.telegram.org).

## Configuration

1. Rename the `config_example.py` file to `config.py`:

    ```sh
    mv config_example.py config.py
    ```

2. Open the `config.py` file and update it with your Telegram API credentials and your phone number:

    ```python
    class Config:
        API_ID = 'your_api_id'
        API_HASH = 'your_api_hash'
        PHONE = 'your_telegram_phone_number'
    ```

## Preparing the Excel File

The script reads recipient data from `list_of_people.xlsx`. Ensure the file has the following columns:

- First Name
- Last Name
- Phone Number

Example:

| First Name | Last Name | Phone Number |
|------------|-----------|--------------|
| John       | Doe       | 1234567890   |
| Jane       | Smith     | 9876543210   |

## Running the Script

To run the script and send messages:

```sh
python send_messages.py
```
<small>(built with the assistance of ChatGPT)</small>