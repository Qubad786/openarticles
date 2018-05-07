from web.accounts.models import User


class CustomAuthenticationBackend(object):

    # noinspection PyMethodMayBeStatic
    def authenticate(self, unique_data, password):
        """
        Authenticates user if it already exists otherwise returns None.
        """
        try:
            user = User.objects.get(**unique_data)
            if not user.check_password(password):
                return None
        except User.DoesNotExist:
            return None

        return user

    # noinspection PyMethodMayBeStatic
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
