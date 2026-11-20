import re

text = "Contact us at student@gmail.com or admin@yahoo.com"

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)