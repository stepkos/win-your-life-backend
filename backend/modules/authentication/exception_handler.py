from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    try:
        exception_class = exc.__class__.__name__
        print(exception_class)
        handlers = {
            "BadCredentialsException": _handler_bad_credentials,
            "ValidationError": _handler_validation_error,
            "IntegrityError": _handler_validation_error,
            'InvalidToken': _handler_permission_denied,
            'ActivationTokenExpiredException': _handler_token_expired,
            # Add more handlers as needed
        }
        res = exception_handler(exc, context)

        if exception_class in handlers:
            # calling hanlder based on the custom
            message, status_code = handlers[exception_class](exc, context, res)
        else:
            # if there is no hanlder is presnet
            message = str(exc)
            status_code = HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data={"error": message}, status=status_code)
    except Exception as e:
        return Response(
            data={"error": "Internal server error"},
            status=HTTP_500_INTERNAL_SERVER_ERROR,
        )


def _handler_validation_error(exc, context, res):
    return "Invalid data", 400


def _handler_integrity_error(exc, context, res):
    return "Integrity error", 400


def _handler_bad_credentials(exc, context, res):
    return exc.detail, 400


def _handler_permission_denied(exc, context, res):
    return 'Invalid or expired token', 401

def _handler_token_expired(exc, context, res):
    return exc.detail, 401
