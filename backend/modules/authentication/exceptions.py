from rest_framework.exceptions import APIException


class BadCredentialsException(APIException):
    status_code = 401
    default_detail = "Bad credentials"
    default_code = "bad_credentials"

class ActivationTokenExpiredException(APIException):
    status_code = 401
    default_detail = "Activation token expired"
    default_code = "activation_token_expired"
