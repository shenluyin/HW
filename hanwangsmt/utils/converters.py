from django.urls import converters
# 转换器

class UsernameConverter:
    regex='[a-zA-Z0-9_-]{5,20}'

    def to_python(self,value):
        return value