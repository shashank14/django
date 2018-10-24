from django.core.exceptions import ValidationError


def validate_author_email(value):
    if '@'in value:
        return value
    else:
        raise ValidationError('Invalid email format')
