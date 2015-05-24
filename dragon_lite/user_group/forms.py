from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

from dragon_lite.user_group.models import UserGroup


class UserGroupForm(Form):
    name = TextField('Name', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(UserGroupForm, self).__init__(*args, **kwargs)
        self.user_group = None

    def validate(self):
        initial_validation = super(UserGroupForm, self).validate()
        if not initial_validation:
            return False
        self.user_group = UserGroup.query.\
                    filter_by(name=self.name.data).first()
        if self.user_group:
            self.errors['Name'] = 'UserGroup exists'
            return False
        else:
            return True
