import argparse

import requests
from flask import json
from loguru import logger


def send(data):
    response = requests.post("http://localhost:5000/data", json={"data": json.loads(data)})
    print(response.json())
    data = response.json()["data"]
    return data


def retrieve(uuid):
    response = requests.get(f"http://localhost:5000/data/{uuid}")
    return response.json()


def request_operation(uuid, operation):
    response = requests.get(f"http://localhost:5000/data/{uuid}/{operation}")
    return response.json()


def main():
    #    uuid = send([1, 2, 3, 4])
    #    retrieve(uuid)
    parser = argparse.ArgumentParser(description="Test our API")
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--get", action="store_true")
    parser.add_argument("--calc", action="store_true")
    parser.add_argument("--data", dest="data", type=str)
    parser.add_argument("--uuid", dest="uuid", type=str)
    parser.add_argument("--op", dest="op", type=str)

    args = parser.parse_args()

    if args.send and args.data:
        logger.info(f"sending data {args.data}")

        response = send(args.data)

        logger.info(f"Response {response}")

    elif args.get and args.uuid:
        logger.info(f"getting data with uuid:{args.uuid}")

        response = retrieve(args.data)

        logger.info(f"Response {response}")

    elif args.calc and args.uuid and args.op:
        logger.info(f"perform op: {args.op}with uuid:{args.uuid}")

        response = request_operation(args.uuid, args.op)

        logger.info(f"Response {response}")
    else:
        logger.info(f"No action")


if __name__ == "__main__":
    main()
