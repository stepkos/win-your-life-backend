from rest_framework.exceptions import APIException


class BadCredentialsException(APIException):
    status_code = 401
    default_detail = "Bad credentials"
    default_code = "bad_credentials"
