import re

def redact_phone(text: str): 
    
    phones = re.findall(r'\+84\d+|\d{10}', text)

    result = text
    for phone in phones:
        result = result.replace(phone, '[REDACTED]')
    
    return result


print(redact_phone("Call 0123456789 or +84912345678"))
