import jwt


class JwtService:
    def generate_jwt(self, user_id):
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    def decode_jwt(self, token):
        return jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])