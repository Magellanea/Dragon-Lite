class ValidationError(ValueError):
    """
    Raised when a validator fails to validate its input.
    """
    def __init__(self, message='', *args, **kwargs):
        ValueError.__init__(self, message, *args, **kwargs)


class WhiteList(object):
    """
    Validates the existence of value among known vals.
    :param vals:
        The set of vals for which the value should be a part of
    :param message:
        Error message to raise in case of a validation error.
    """
    def __init__(self, vals, message=None):
        assert type(vals) is list, 'Vals must be a list'
        self.vals = vals
        self.message = message

    def __call__(self, form, field):
        b = field.data and field.data in self.vals
        if not b:
            message = self.message
            if message is None:
                message = 'value should be one of:%s' % str(self.vals)
            raise ValidationError(message)
