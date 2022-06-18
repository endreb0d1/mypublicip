from requests import get
import smtplib
import time

new_ip = get('https://api.ipify.org').content.decode('utf8')
old_ip = new_ip

while True:
    try:
        new_ip = get('https://api.ipify.org').content.decode('utf8')
    
        # send email if IP has changed
        if new_ip != old_ip:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("sender_email_id@gmail.com", "sender_email_id_password")
            sender = "sender_email_id@gmail.com"
            receiver = "receiver_email_id@gmail.com"
            subject = "Your public IP has changed"
            text = f"Current IP:\n\n{new_ip}"
            message = f"Subject: {subject}\n\n{text}"
            s.sendmail(sender, receiver, message)
            s.quit()
        
            # set IP
            old_ip = new_ip

    except:
        pass
        
    # check every 2 minutes
    time.sleep(120)
