from flask_restful import Resource
from flask import request, Response
from flasgger import swag_from
import json
from to_xml_fun import to_xml

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
