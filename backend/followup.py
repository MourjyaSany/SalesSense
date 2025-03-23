import time

def send_followup(lead_email):
    print(f"Sending follow-up email to {lead_email}...")

if __name__ == '__main__':
    leads = ["user1@example.com", "user2@example.com"]
    for email in leads:
        send_followup(email)
        time.sleep(2)
