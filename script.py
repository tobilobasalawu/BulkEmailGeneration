import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd

# Load your list of users (CSV or Excel file with columns like 'Name' and 'Email')
users = pd.read_csv(r'C:\Users\oluwa\Documents\BulkEmailGeneration\Users.csv')

# Email server (Outlook example)
SMTP_SERVER = 'smtp.gmail.com'  # For Gmail
SMTP_PORT = 587
SENDER_EMAIL = 'tobisal.dev@gmail.com'  # Update with your Gmail address
SENDER_PASSWORD = 'ouma pmxo ghfr yjwm'  # Update with your Gmail password

# Create server connection
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

# Loop through users and send emails
for index, user in users.iterrows():
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = 'Happy People Care <tobisal.dev@gmail.com>'
    msg['To'] = user['Email']
    msg['Subject'] = "We're Here to Support You - Happy People Care"

    
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
            <p>I hope this message finds you well, especially during this busy time of the year!</p>
            <p>I wanted to remind you that Happy People Care is here to support you with all your staffing needs, whether temporary or permanent. We understand how critical it is to have the right team in place, particularly during high-demand periods, and we are ready to assist. We offer competitive rates to suit your budget and have got your back even when you need a last-minute cover for urgent staffing needs.</p>
            <p>We offer a range of services designed to meet your unique requirements, including:</p>
            <ul>
                <li>Well-trained Care Assistants and Support Workers</li>
                <li>Qualified RGNs, RMNs, and Other Specialist Nurses</li>
            </ul>
            <p>We understand you may have a preferred agency or perhaps haven't used an agency before, but we encourage you to try Happy People Care—we promise to wow you! Please don't hesitate to reach out if there's anything we can do to assist. We look forward to collaborating with you and providing the high-quality staffing support you expect.</p>
            <div class="footer">
                <p style="font-size: 14px; color: #B54826;">Kind Regards,<br><br>Happy People Care</p>
                <div class="footer-sec">
                    <div class="icon-section-mid">
                        <img src="https://ci3.googleusercontent.com/meips/ADKq_NZMUY0OEeTPq-e4LU5laTbaObRbLfNryU9Diyix7C7Ftb3MIUbPbUXe_mmXKwnaSjcPvfkEhVJBtWOmWx5xp8xVOJzCD0F-pDrCYJqeWzBg6UL9oHanb-48hig4RwT7Fz4LKH2UJOWlzB0tek67Kg=s0-d-e1-ft#https://signatures-cam.300media.co.uk/wp-content/uploads/2024/01/Happy-People-Care-01.png" alt="Company Logo"><br>
                    </div>
                    <div class='sec-pace'>
                        <div class="icon-section">
                            <p><b>Office</b>: 01217512426<br><b>Mobile</b>: 07423377255, 07570528707</p>
                            
                        </div>
                        <div class="icon-section">
                            <a href="mailto:info@happypeoplecare.co.uk">info@happypeoplecare.co.uk</a>
                        </div>
                        <div class="icon-section">
                            <a href="https://happypeoplecare.co.uk/">www.happypeoplecare.co.uk</a>
                        </div>
                        <div class="icon-section">
                            <p>Fort Dunlop, Fort Parkway, Birmingham,<br>West Midlands, B24 9FE</p>
                        </div>
                    </div>
                </div>
            </div>
            <div style="background-color: #B54826; font-weight: bold; height: 40px;">
                <p style="color: white; font-size:12px; padding-top: 10px; padding-left: 8px;">Quality Staffing and Compassionate Care</p>
            </div>
            <p style="font-size: 10px; max-width: 550px;">This e-mail is only for the above addressee(s). It may contain confidential or privileged information. If you are not an addressee you must not copy, distribute, disclose or use any of the information in it or any attachments. If you have received it in error please notify the sender and delete it immediately. Registered Name: Happy People Care Limited, Registration Number: 15340377</p>
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
