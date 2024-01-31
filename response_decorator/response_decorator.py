from flask import request, Response
from to_xml_fun import to_xml
from functools import wraps

def response_format(func):
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