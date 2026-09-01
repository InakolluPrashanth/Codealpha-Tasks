import re
with open("email_extraction_practice.txt", "r") as file:
    text = file.read()
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

# Display the emails
print("Extracted Email Addresses:")

for email in emails:
    print(email)

with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("\nEmails saved to extracted_emails.txt")