import re
from datetime import datetime
from app.utils.exception import ShapeShyftException

def is_valid_phone_number(phone_number: str) -> bool:
    # Define a regular expression pattern for E.164 format phone numbers
    pattern = r"^\+\d{1,15}$"
    return re.match(pattern, phone_number) is not None


def is_valid_email(email: str) -> bool:
    # Define a regular expression pattern for email validation
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    return re.match(pattern, email) is not None


def is_valid_time_format(time_string):
    try:
        datetime.strptime(time_string,"%I:%M%p")
        return True
    except ValueError:
        raise ShapeShyftException("E1025",400)
