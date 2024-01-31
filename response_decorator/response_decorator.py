from flask import request, Response
from to_xml_fun import to_xml
from functools import wraps


def response_format(func):

    # use of wraps decorator is necessary to make sure that attributes to
    # match those of the original function for swagger to work correctly
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        format_type = request.args.get('format', 'json')

        if format_type == 'xml':
            xml_data = to_xml(data)
            return Response(xml_data, mimetype='application/xml')
        else:
            return data

    return wrapper
