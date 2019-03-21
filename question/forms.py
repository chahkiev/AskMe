from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

text_validator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Text should contain letters")

tags_validator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Tags should contain letters")

password_validator = RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                                   "Password should contain minimum 8 characters, at least 1 letter and 1 number")
