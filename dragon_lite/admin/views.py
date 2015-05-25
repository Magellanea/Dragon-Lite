from flask.ext.login import current_user
from flask.ext.admin.contrib.sqla import ModelView


class AdminView(ModelView):
    # TODO : Clean that mess
    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, static_folder=None, menu_class_name=None, menu_icon_type=None, menu_icon_value=None, columns=None):
        if columns is not None:
            self.column_list = columns
        super(AdminView, self).__init__(model, session, name=name, category=category, endpoint=endpoint, url=url, static_folder=static_folder, menu_class_name=menu_icon_type, menu_icon_type=menu_icon_type, menu_icon_value=menu_icon_value)

    def is_accessible(self):
        return current_user.is_authenticated()
