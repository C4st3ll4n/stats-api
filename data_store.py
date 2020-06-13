from uuid import uuid4, UUID

_in_memory_storage = dict()


def save_data(data):
    data_uuid = uuid4()
    _in_memory_storage[data_uuid] = data

    return data_uuid


def get_data(uuid):
    try:
        formated_uuid = UUID(uuid)

        try:
            result = _in_memory_storage[formated_uuid]
            return result
        except Exception:
            raise FileNotFoundError

    except ValueError:
        raise FileNotFoundError



#9126c973-a7f8-4133-b080-db777cb99207