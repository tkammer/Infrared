class IRException(Exception):
    def __init__(self, message):
        self.message = message


class IRKeyNotFoundException(IRException):
    def __init__(self, key, dic):
        super(self.__class__, self).__init__(
            'Key "%s" not found in %s' % (key, dic))


class IRFileNotFoundException(IRException):
    def __init__(self, file_path, msg=None):
        pre_msg = msg if msg else 'No such file or directory: '
        super(self.__class__, self).__init__(pre_msg + file_path)


class IRExtraVarsException(IRException):
    def __init__(self, extra_var):
        super(self.__class__, self).__init__(
            '"%s" - extra-var argument must be a path to a setting file or '
            'in "key=value" form' % extra_var)


class IRMissingAncestorException(IRException):
    def __init__(self, key):
        super(self.__class__, self).__init__(
            'Please provide all ancestors of "--%s"' % key.replace("_", "-"))


class IRUndefinedEnvironmentVariableExcption(IRException):
    def __init__(self, env_var):
        super(self.__class__, self).__init__(
            'Environment variable "%s" is not defined' % env_var)


class IRPlaybookFailedException(IRException):
    def __init__(self, playbook, message=''):
        msg = 'Playbook "%s" failed!' % playbook
        if message:
            msg += ' ' + message
        super(self.__class__, self).__init__(msg)


class IRYAMLConstructorError(IRException):
    def __init__(self, mark_obj, where):
        self.message = mark_obj.problem
        pm = mark_obj.problem_mark
        self.message += ' in:\n  "{where}", line {line_no}, column ' \
                        '{column_no}'.format(where=where,
                                             line_no=pm.line + 1,
                                             column_no=pm.column + 1)


class IRPlaceholderException(IRException):
    def __init__(self, trace_message):
        self.message = 'Mandatory value is missing.\n' + trace_message


class IRNotImplemented(IRException):
    pass


class IRUnknownApplicationException(IRException):
    """
    This exceptions is raised when unknown application is
     started by user.
    """
    def __init__(self, app_name):
        self.app_name = app_name
        super(IRUnknownApplicationException, self).__init__(
            "Application is unknown: '{}'".format(app_name))


class IRConfigurationException(IRException):
    """
    General exception for any kind of configuration issues.
    """
    pass


class IRInfiniteLookupException(IRException):
    def __init__(self, value):
        message = "Lookup circular reference detected for: {}".format(value)
        super(IRInfiniteLookupException, self).__init__(message)
