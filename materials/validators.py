import re

from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pattern = r"^https?://(www\.)?youtube\.com/.*$"
        tmp_val = dict(value).get(self.field)
        print(tmp_val)
        if re.match(pattern, tmp_val):
            print("URL является допустимым URL youtube.com")
        else:
            raise ValidationError(
                "URL не является допустимым, так как не содержит youtube.com"
            )
