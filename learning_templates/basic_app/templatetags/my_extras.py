from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string.
    :param value: the string to be cutted
    :param arg: the cuts that need to be applied on value parameter
    :return: string without the values in "arg"
    """

    return value.replace(arg, '')


# register.filter('cut', cut)
