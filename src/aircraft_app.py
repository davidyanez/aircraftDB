from controllers.aircraft_controller import filter_aircraft_by_field, filter_aircraft_array_field_contains, \
    populate_aircraft_db
from flask import Flask, Response, request, jsonify
from waitress import serve


app = Flask(__name__)

filter_aircraft_fields = ['Model', 'ATCT Weight Class', 'Tags']


@app.get('/filter_aircraft')
def filter_aircraft():
    """
    filter_aircraft GET endpoint
    with params  field and value
    Supports 'Model', 'ATCT Weight Class' and, 'Tags'

    :return:  Filtered items
    """
    args = request.args
    field = args.get('field')
    value = args.get('value')

    if field is None or value is None:
        return Response("field and value fields are required", status=400)

    response_obj = []
    if field in ['Model', 'ATCT Weight Class']:
        response_obj = filter_aircraft_by_field(field, value)
    elif field in ['Tags']:
        response_obj = filter_aircraft_array_field_contains(field, value)
    else:
        return Response(
            "Field not supported",
            status=400,
        )
    return jsonify(response_obj)


@app.get('/populate_db')
def populate_db():
    """
    Populate db endpoint:
    note:  used GET for simplicity to call it from the browser, but ideally should be POST
    :return: inserted items
    """
    return jsonify({'inserted': populate_aircraft_db()});

serve(app, port=8000)
