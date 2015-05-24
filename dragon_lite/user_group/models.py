# -*- coding: utf-8 -*-
from dragon_lite.database import db
from dragon_lite.database import CRUDMixin

group_user = db.Table('group_user',
 db.Column('group_id', db.Integer, db.ForeignKey('user_groups.id')),
 db.Column('user_id', db.Integer, db.ForeignKey('users.id')))


class UserGroup(CRUDMixin, db.Model):
    __tablename__ = 'user_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', secondary=group_user, backref='user_groups')

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)
        self.errors = []

    def __repr__(self):
        return '<UserGroup({name})>'.format(name=self.name)
