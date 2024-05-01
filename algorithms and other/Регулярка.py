import re

def find_matches(pattern, text):
    matches = re.findall(pattern, text)
    return matches

text = "Hello, my email is user@example.com and my phone number is 123-456-7890"
pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern_phone = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

email_matches = find_matches(pattern_email, text)
phone_matches = find_matches(pattern_phone, text)

print("Email addresses found:", email_matches)
print("Phone numbers found:", phone_matches)
