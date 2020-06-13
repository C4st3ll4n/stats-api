import pytest
import requests
from loguru import logger


class TestAPI:

    @pytest.fixture(scope="class")
    def url(self):
        port = "5000"
        host = "localhost"
        return f"http://{host}:{port}/data"

    @pytest.fixture(scope="class")
    def data(self):
        return [1, 2, 3, 4]

    @pytest.fixture(scope="class")
    def uuid(self, url, data):
        test_data = data
        response = requests.post(url=url, json={"data": test_data})
        return response.json()["data"]

    def test_save_data_sucess(self, url, uuid):
        assert uuid is not None

    def test_get_sucess(self, uuid, url, data):
        response = requests.get(url=f"{url}/{uuid}")

        assert response.ok
        assert response.json()["data"] == data

    def test_calc_mean(self, url, uuid):
        response = requests.get(url=f"{url}/{uuid}/mean")
        #   logger.info(f"Response: {response.json()}")
        assert response.ok
        assert response.json()["data"] == pytest.approx(2.5)

    def test_calc_min(self, url, uuid):
        response = requests.get(url=f"{url}/{uuid}/min")
        #   logger.info(f"Response: {response.json()}")
        assert response.ok
        assert response.json()["data"] == 1

    def test_calc_max(self, url, uuid):
        response = requests.get(url=f"{url}/{uuid}/max")
        #   logger.info(f"Response: {response.json()}")
        assert response.ok
        assert response.json()["data"] == 4

    @pytest.mark.parametrize("operation, expected",
                             [("mean", 2.5), ("max", 4), ("min", 1)])
    def test_parametrized(self, url, uuid, operation, expected):
        response = requests.get(url=f"{url}/{uuid}/{operation}")
        #   logger.info(f"Response: {response.json()}")
        assert response.ok
        assert response.json()["data"] == pytest.approx(expected)
