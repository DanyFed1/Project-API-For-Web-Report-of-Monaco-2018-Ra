from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api
import reporting_gen as rpg
from api_resources import ReportResource, DriversResource, DriverInfoResource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)


# Configure Flasgger e
swagger = Swagger(app)

# Initialize the report generator object based on logic defined in reporting_gen.py
processor = rpg.Q1Processor('./files')
report_generator = rpg.Q1ReportGenerator(processor)

# API endpoints with versioning
api.add_resource(ReportResource, '/api/v1/report/', resource_class_kwargs={'report_generator': report_generator})
api.add_resource(DriversResource, '/api/v1/drivers/', resource_class_kwargs={'report_generator': report_generator})
api.add_resource(DriverInfoResource, '/api/v1/drivers/<driver_id>/', resource_class_kwargs={'report_generator': report_generator})


#Web Interface endpoits
@app.route('/')
def index():
    return redirect(url_for('report'))

@app.route('/report/')
def report():
    order = request.args.get('order', 'asc')
    report_data = report_generator.get_report_data(order)
    return render_template('report.html', drivers=report_data, order=order)


@app.route('/report/drivers/')
def drivers():
    order = request.args.get('order', 'asc')
    report_data = report_generator.get_all_drivers()
    return render_template('drivers.html', drivers=report_data, order=order)


@app.route('/report/drivers/<driver_id>')
def driver_info(driver_id):
    info = report_generator.get_driver_info(driver_id)
    if not info:
        info = {'name': 'Not Found', 'team': 'N/A', 'lap_time': 'N/A'}
    return render_template(
        'driver_info.html',
        driver_info=info,
        driver_id=driver_id)


if __name__ == '__main__':
    app.run(debug=True)
