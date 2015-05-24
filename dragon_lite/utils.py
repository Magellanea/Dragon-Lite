# -*- coding: utf-8 -*-
'''Helper utilities and decorators.'''
from flask import flash

def flash_errors(form, category="warning"):
    '''Flash all errors for a form.'''
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                    .format(getattr(form, field).label.text, error), category)


def flash_label_errors(form, category="warning"):
    '''Flash all errors for a form.'''
    for field, error in form.errors.items():
        flash("{0} - {1}"
              .format(field, error), category)
