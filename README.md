# BulkEmail Generation

BulkEmail Generation is a Python-based script designed to send personalized bulk emails using Gmail's/Web Mail SMTP server. It uses a CSV file to load user details (names and emails), generates an HTML email message, and sends the email to all users in the list.

## Folder Structure

```
BulkEmail Generation/
│
├── Users.csv
├── script.py
├── MailContents(html).html
└── icons/ 
```

### File Descriptions

1. **Users.csv**: This file contains the names and email addresses of the users. It must have two columns: 
   - `Name`: The name of the recipient.
   - `Email`: The email address of the recipient.

2. **script.py**: The Python script responsible for sending emails to all users listed in the CSV file. Before running the script, ensure to:
   - Replace the SMTP server, sender's email, and sender's password with your Gmail details.
   - Ensure that Gmail allows sending emails through less secure apps.
   - Insert the content from the `MailContents(html).html` file into the script.

3. **MailContents(html).html**: This file contains the HTML structure and styling for the email. You should add the contents of this file to the `script.py` where indicated to format the email properly.

4. **icons/**: This folder is where your email's icons or other related assets are stored.

---

## Setup and Usage

### 1. Requirements

You need to have the following libraries installed in your Python environment:

```bash
pip install pandas
```

The script uses `pandas` for handling CSV data and `smtplib` for sending emails.

### 2. Instructions

1. **Prepare Users.csv**: Create or update the `Users.csv` file with two columns: `Name` and `Email`.

   Example `Users.csv` format:

   | Name    | Email              |
   |---------|--------------------|
   | John   | johndoe@example.com |
   | Toby   | toby@example.com    |

2. **Update script.py**: In the `script.py` file:
   - Replace the `SENDER_EMAIL` and `SENDER_PASSWORD` with your Gmail address and password.
   - Make sure to replace placeholders with your specific details, such as email subject, email content, etc.
   - Add the contents of the `MailContents(html).html` file where the HTML content of the email message is defined in `script.py`.

3. **Run the Script**: Execute the script to send emails to all the users listed in `Users.csv`.

   ```bash
   python script.py
   ```

### 3. SMTP Configuration in script.py

Before running the script, make sure to configure the following:

- **SMTP_SERVER**: The SMTP server for Gmail is `smtp.gmail.com`.
- **SMTP_PORT**: The SMTP port for Gmail is `587`.
- **SENDER_EMAIL**: Your Gmail address.
- **SENDER_PASSWORD**: Your Gmail password (ensure you have allowed access for less secure apps).

```python
# Example SMTP setup
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_password'
```

You can replace these with your Gmail credentials.

### 4. Personalizing Email Content

The email content in the script is dynamically generated using the user's name and your custom message from the `MailContents(html).html` file. Make sure to copy the HTML content from `MailContents(html).html` and replace the `html` section in `script.py`.

---


