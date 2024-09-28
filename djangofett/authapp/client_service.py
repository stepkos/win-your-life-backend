from joblib.externals.cloudpickle import instance

from authapp.authentication_service import AuthenticationService
from authapp.client_serializer import ClientSerizalizer
from authapp.models import Client


class ClientService:
    def get_client_by_email(self, email):
        client = Client.objects.get(email=email)
        return ClientSerizalizer(client).data

    def register(self, data):
        client_serialized = ClientSerizalizer(data=data)
        client_serialized.is_valid(raise_exception=True)
        client_serialized.create(client_serialized.validated_data)

    def login(self, data):
        client_serialized = ClientSerizalizer(data=data)
        client_serialized.is_valid(raise_exception=True)

        return AuthenticationService.authenticate(client_serialized.instance.email, client_serialized.instance.password)







