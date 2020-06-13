from flask import Flask, request, jsonify
from loguru import logger

import data_store
import operation

app = Flask(__name__)


@app.route("/data", methods=["POST"])
def save_data():
    logger.info(f"Savinda data..")

    content = request.get_json()

    uuid = data_store.save_data(content["data"])

    logger.info(f"Data saved with UUID {uuid} !")

    return jsonify({"status": "success", "message": "data saved", "data": uuid})


@app.route("/data/<uuid>", methods=["GET"])
def retrive_data(uuid):
    logger.info(f"Retrieving data associated with {uuid}...")

    try:
        data = data_store.get_data(uuid)
        logger.warning(f"Data associated with uuid: {uuid} was sucessfuly found !")
    except KeyError:
        logger.warning(f"Cannot retrive data with this uuid: {uuid}")
        return jsonify({"status": "fail", "message": "UUID not found", "data": []})

    return jsonify({"status": "sucess", "message": "UUID was found", "data": data})


class NoSuchOperationError(Exception):
    pass


@app.route('/data/<uuid>/<operation>', methods=["GET"])
def process_operation(uuid, operation):
    logger.info(f"Processing operation: {operation}, on uuid:{uuid}")

    try:
        data = data_store.get_data(uuid)

        operation_func = get_operation(operation)

        result = operation_func(data)

    except KeyError:

        logger.warning(f"Cannot retrive data with this uuid: {uuid}")
        return jsonify({"status": "fail", "message": "UUID not found", "data": []})

    except NoSuchOperationError:

        logger.warning(f"Cannot perform operation {operation}")
        return jsonify({"status": "fail", "message": "Operation does not exists", "data": []})

    logger.info(f"Operation: {operation} performed with sucess, on uuid:{uuid}")
    return jsonify({"status": "sucess", "message": "UUID was found", "data": result})


def get_operation(operation_name):
    if operation_name == "min":
        return operation.op_min
    elif operation_name == "mean":
        return operation.op_mean
    elif operation_name == "max":
        return operation.op_max
    else:
        raise NoSuchOperationError


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
