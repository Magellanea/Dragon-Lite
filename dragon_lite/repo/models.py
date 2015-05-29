# -*- coding: utf-8 -*-
from sqlalchemy.orm import validates
from dragon_lite.database import db
from dragon_lite.database import CRUDMixin
from dragon_lite.user_group import UserGroup


class Repo(CRUDMixin, db.Model):
    __tablename__ = 'repos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # All arguments must have a default value, otherwise
    # flask will throw an exception

    def __init__(self, name="", **kwargs):
        db.Model.__init__(self, name=name, **kwargs)
        self.errors = []

    def __repr__(self):
        return '<Repo({name})>'.format(name=self.name)


class Permission(CRUDMixin, db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer, db.ForeignKey('repos.id'), nullable=False)
    user_group_id = db.Column(db.Integer, db.ForeignKey('user_groups.id'), nullable=False)
    permission = db.Column(db.String(80),  nullable=False)
    repo = db.relationship(Repo)
    user_group = db.relationship(UserGroup)

    @validates('permission')
    def validate_permission(self, key, val):
        if val not in ['RW+', 'RW-']:
            raise ValueError('Permission value not recognized')
        return val
