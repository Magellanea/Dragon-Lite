from flask.ext.login import current_user
from flask.ext.admin.contrib.sqla import ModelView


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated()
