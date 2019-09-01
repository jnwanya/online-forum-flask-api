import re

_email_regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"


def validate_email(email: str) -> bool:
    return re.search(_email_regex, email)
