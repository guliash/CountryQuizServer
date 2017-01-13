from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_password_length(value):
    if len(value) < 6:
        raise ValidationError(_('passowrd must have more than 5 symbols'),
                              params = {'value': value}, code = 'invalid')
