# from flask_restful import Resource
# from flask import request, Response
# from flasgger import swag_from
# import json
# from to_xml_fun import to_xml
#
# class ReportResource(Resource):
#     def __init__(self, **kwargs):
#         self.report_generator = kwargs['report_generator']
#
#     @swag_from('./docs/report_resource.yml')
#     def get(self):
#         format_type = request.args.get('format', 'json')
#         order = request.args.get('order', 'asc')
#         print(f"Received request for ReportResource with format: {format_type}, order: {order}")
#
#         report_data = self.report_generator.get_report_data(order)
#         if format_type == 'xml':
#             xml_data = to_xml(report_data)
#             return Response(xml_data, mimetype='application/xml')
#         return report_data
#
# class DriversResource(Resource):
#     def __init__(self, **kwargs):
#         self.report_generator = kwargs['report_generator']
#
#     @swag_from('./docs/drivers_resource.yml')
#     def get(self):
#
#         format_type = request.args.get('format', 'json')
#         print(f"Received request for ReportResource with format: {format_type}")
#
#         drivers_data = self.report_generator.get_all_drivers()
#         if format_type == 'xml':
#             xml_data = to_xml(drivers_data)
#             return Response(xml_data, mimetype='application/xml')
#         return drivers_data
#
# class DriverInfoResource(Resource):
#     def __init__(self, **kwargs):
#         self.report_generator = kwargs['report_generator']
#
#     @swag_from('./docs/driver_info_resource.yml')
#     def get(self, driver_id):
#         format_type = request.args.get('format', 'json')
#         print(f"Received request for ReportResource with format: {format_type}")
#
#         driver_info = self.report_generator.get_driver_info(driver_id)
#         if format_type == 'xml':
#             xml_data = to_xml(driver_info)
#             return Response(xml_data, mimetype='application/xml')
#         return driver_info

from flask_restful import Resource
from flasgger import swag_from
from response_decorator import response_format

class ReportResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    @response_format
    @swag_from('./docs/report_resource.yml')
    def get(self):
        order = request.args.get('order', 'asc')
        return self.report_generator.get_report_data(order)

class DriversResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    @response_format
    @swag_from('./docs/drivers_resource.yml')
    def get(self):
        return self.report_generator.get_all_drivers()

class DriverInfoResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    @response_format
    @swag_from('./docs/driver_info_resource.yml')
    def get(self, driver_id):
        return self.report_generator.get_driver_info(driver_id)