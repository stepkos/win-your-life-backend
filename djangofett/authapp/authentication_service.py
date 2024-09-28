from rest_framework_simplejwt.tokens import RefreshToken

from authapp.exceptions import BadCredentialsException
from authapp.models import Client


class AuthenticationService:
    def authenticate(self, email, password):
        client = Client.objects.get(email=email)

        if client.password == password:
            refresh = RefreshToken.for_user(client)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            raise BadCredentialsException
