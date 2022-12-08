import re

with open('assets/potential_contacts.txt') as f:
    potential_contacts = f.read()

# telephone number search with regex
phone_numbers = []
phone_numbers.extend(re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',
                                potential_contacts))

# search and prevent duplicates
duplicates = list(set(phone_numbers))
duplicates.sort()

telephone_number = ''
for num in duplicates:
    telephone_number += num + ', '

# write new documents
with open('assets/phone_numbers.txt', 'w') as file:
    phone_numbers_only = file.write(telephone_number)

# email addresses search with regex
emails = []
emails.extend(re.findall('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', potential_contacts))

# search and prevent duplicates
email_duplicates = list(set(emails))
email_duplicates.sort()

email_address = ''
for mail in email_duplicates:
    email_address += mail + ', '

# write email document
with open('assets/emails.txt', 'w') as file:
    emails_only = file.write(email_address)
