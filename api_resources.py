from flask_restful import Resource
from flask import request, Response
import json
import xml.etree.ElementTree as ET

def to_xml(data):
    if isinstance(data, list):
        root = ET.Element('data')
        for item in data:
            element = ET.SubElement(root, 'item')
            for key, value in item.items():
                child = ET.SubElement(element, key)
                child.text = str(value)
    else:
        root = ET.Element('driver')
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
    return ET.tostring(root, encoding='utf-8', method='xml')

class ReportResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    def get(self):
        format_type = request.args.get('format', 'json')
        order = request.args.get('order', 'asc')
        print(f"Received request for ReportResource with format: {format_type}, order: {order}")

        report_data = self.report_generator.get_report_data(order)
        if format_type == 'xml':
            xml_data = to_xml(report_data)
            return Response(xml_data, mimetype='application/xml')
        return report_data

class DriversResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    def get(self):
        format_type = request.args.get('format', 'json')
        print(f"Received request for ReportResource with format: {format_type}")

        drivers_data = self.report_generator.get_all_drivers()
        if format_type == 'xml':
            xml_data = to_xml(drivers_data)
            return Response(xml_data, mimetype='application/xml')
        return drivers_data

class DriverInfoResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    def get(self, driver_id):
        format_type = request.args.get('format', 'json')
        print(f"Received request for ReportResource with format: {format_type}")

        driver_info = self.report_generator.get_driver_info(driver_id)
        if format_type == 'xml':
            xml_data = to_xml(driver_info)
            return Response(xml_data, mimetype='application/xml')
        return driver_info