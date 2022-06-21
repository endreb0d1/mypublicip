from requests import get
import smtplib
import time

new_ip = get('https://api.ipify.org').content.decode('utf8')
current_ip = new_ip

while True:
    try:
        new_ip = get('https://api.ipify.org').content.decode('utf8')
    
        # send email if IP has changed
        if new_ip != current_ip and len(new_ip) < 16:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("sender_email_id@gmail.com", "sender_email_password")
            sender = "sender_email_id@gmail.com"
            receiver = "receiver_email_id@gmail.com"
            subject = "Your public IP has changed"
            text = f"Current IP:\n\n{new_ip}"
            message = f"Subject: {subject}\n\n{text}"
            s.sendmail(sender, receiver, message)
            s.quit()
        
            # set current IP
            current_ip = new_ip

    except:
        pass
        
    # check every 10 minutes
    time.sleep(600)
