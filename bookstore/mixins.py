class AuthContextMixin:
    def get_auth_context(self, context):
        context['is_auth'] = self.request.user.is_authenticated

        return context
