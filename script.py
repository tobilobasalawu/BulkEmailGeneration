import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd

# Load your list of users (CSV or Excel file with columns like 'Name' and 'Email')
users = pd.read_csv(r'Users.csv')

# Email server (Outlook example)
SMTP_SERVER = 'smtp.gmail.com'  # For Gmail
SMTP_PORT = 587
SENDER_EMAIL = 'username@gmail.com'  # Update with your Gmail address
SENDER_PASSWORD = 'password'  # Update with your Gmail password

# Create server connection
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

# Loop through users and send emails
for index, user in users.iterrows():
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = 'CompanyName <username@gmail.com>'
    msg['To'] = user['Email']
    msg['Subject'] = "Subject"

    
    # Personalize the body
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                overflow: hidden;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                color: #555;
                line-height: 1.5;
            }}
            img {{
                max-width: 100%;
                height: auto;
                border-radius: 8px;
            }}
            .footer {{
                margin-top: 20px;
                padding: 10px;
                border-top: 1px solid #ccc;
            }}
            .footer p {{
                margin: 5px 0;
                color: #333;
            }}
            .contact-section {{
                font-size: 13px;
                text-decoration: underline;
            }}
            .contact-section p {{
                color: #666666;
            }}
            .contact-section a {{
                text-decoration: none;
                color: #666666;
            }}
            .footer-sec {{
                display: flex;
                align-items: center; /* Align items vertically */
                flex-wrap: wrap;
            }}
            .icon-section {{
                display: flex;
                align-items: center;
                margin: 5px;
            }}
            .icon section a{{
                font-size: 10px;
                padding-bottom: 5px;
            }}
            .icon section p{{
                font-size: 10px;
            }}
            .icon-section img {{
                width: 18px;
                padding-right: 10px;
                padding-top: 5px;
            }}
            .icon-section-mid img {{
                width: 120px;
                margin-top: 10px; 
            }}
            @media (max-width: 600px) {{
                .container {{
                    padding: 10px;
                }}
                .footer-sec {{
                    flex-direction: column;
                    align-items: flex-start;
                }}
                .icon section a{{
                    font-size: 10px;
                    padding-bottom: 5px;
                }}
                .icon section p{{
                    font-size: 10px;
                }}
                .footer-sec p {{
                    font-size: 12px; /* Reduce font size for smaller screens */
                }}
                .icon-section img {{
                    width: 15px;
                    padding-right: 10px;
                    padding-top: 5px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <p>Dear {user['Name']},</p>
            <p>Welcome to the Platform!</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            <div class="footer">
                <p style="font-size: 14px; color: #B54826;">Kind Regards,<br><br>Company Name</p>
                <div class="footer-sec">
                    <div class="icon-section-mid">
                        <img src="" alt="Company Logo"><br>
                    </div>
                    <div class='sec-pace'>
                        <div class="icon-section">
                            <p><b>Phone Numbers</b>: 123456789</p>
                            
                        </div>
                        <div class="icon-section">
                            <a href="mailto:username@gmail.com">username@gmail.com</a>
                        </div>
                        <div class="icon-section">
                            <a href="https://companywebsite.com">www.companywebsite.com</a>
                        </div>
                        <div class="icon-section">
                            <p>London, United Kingdom<br>Location, Address</p>
                        </div>
                    </div>
                </div>
            </div>
            <div style="background-color: #B54826; font-weight: bold; height: 40px;">
                <p style="color: white; font-size:12px; padding-top: 10px; padding-left: 8px;">Thank for choosing us</p>
            </div>
            <p style="font-size: 10px; max-width: 550px;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
    </body>
    </html>
    """

    # Attach HTML content
    msg.attach(MIMEText(html, 'html'))

    # Send the email
    server.sendmail(SENDER_EMAIL, user['Email'], msg.as_string())

# Close the server
server.quit()
