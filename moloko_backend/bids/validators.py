import phonenumbers
from django.core.exceptions import ValidationError
from phonenumbers import NumberParseException


class ValidatePhoneMixin:
    def clean_contact_phone(self):
        contact_phone = self.cleaned_data.get("contact_phone")
        self.validate_phone(contact_phone)
        return contact_phone

    def validate_phone(self, value):  # type: ignore
        try:
            phone = phonenumbers.parse(value, "RU")
        except NumberParseException:
            raise ValidationError(
                "%(value)s является неверным телефоном", params={"value": value}
            )
        phone = phonenumbers.is_valid_number(phone)
        if not phone:
            raise ValidationError(
                "%(value)s является неверным телефоном", params={"value": value}
            )


