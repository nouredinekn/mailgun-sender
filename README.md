
# Email Automation with Mailgun - sender 

## Overview

This project automates the process of sending personalized emails using the Mailgun API. The script reads email addresses from a file, selects random content from predefined text files and HTML templates, and sends out the emails. It tracks sent emails to avoid duplication and utilizes threading for efficient batch processing.

## Features

- **Mailgun Integration**: Seamless sending of emails via the Mailgun API.
- **Dynamic Content**: Randomly selects names, subjects, and HTML content for personalized emails.
- **Batch Processing**: Employs threading to send emails in batches for improved efficiency.
- **Sent Tracking**: Maintains a log of sent emails to prevent duplicates.
- **Customizable Email Content**: Easily modify sender names, subjects, and text snippets.

## Requirements

- Python 3.x
- Mailgun account with an API key
- `requests` library (install via `pip`)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nouredinekn/mailgun-sender.git
   cd mailgun-sender
   ```

2. **Install Required Dependencies**:
   ```bash
   pip install requests
   ```

3. **Setup Directories and Files**:
   Create the following directories and files in your project folder:
   - **letters/**: Place your HTML templates here (e.g., `email_template.html`).
   - **sender_names.txt**: A text file containing sender names for random selection (one name per line).
   - **subjects.txt**: A text file containing email subjects for random selection (one subject per line).
   - **txt/**: Create this folder and add three text files:
     - `##text1##.txt`
     - `##text2##.txt`
     - `##text3##.txt`
   Each file should contain lines of text snippets for dynamic email content.
   - **emailList.txt**: A text file containing a list of recipient email addresses (one email per line).
   - **SentSuccess.txt**: A text file to log successfully sent email addresses.

4. **Configuration**:
   Edit the script to include your Mailgun API key and domain:
   ```python
   api_key = "YOUR_MAILGUN_API_KEY"
   domain = "YOUR_DOMAIN"
   sender = "YOUR_SENDER_NAME <your-email@example.com>"
   ```

## Usage

1. **Run the Script**:
   Start the script to begin sending emails:
   ```bash
   python emailgun-sender.py
   ```


2. **Monitoring**:
   - The console will display logs for each email sent successfully or any errors encountered.
   - Check `SentSuccess.txt` for a record of sent email addresses.

## Contact

For any questions or support, feel free to reach out via Telegram: [@nouredinekn](https://t.me/nouredinekn).

