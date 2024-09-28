from joblib.externals.cloudpickle import instance

from modules.auth.authentication_service import AuthenticationService
from modules.auth.client_serializer import ClientSerizalizer
from modules.auth.models import Client


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







