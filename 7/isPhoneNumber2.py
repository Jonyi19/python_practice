import re

def is_phone_number(text):
    phone_str = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phone_str.search(text)
    return mo.group()

message = '明日415-555-1011に電話してください。オフィスは415-555-9999です。'
print(is_phone_number(message))