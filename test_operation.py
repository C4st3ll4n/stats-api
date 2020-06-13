import loguru
import pytest

import operation


@pytest.mark.parametrize("data", [[1, 2, 3], [3, 2, 1]])
@pytest.mark.parametrize("expected_mean", [2])
def test_mean_sucess(data, expected_mean):
    assert operation.op_mean(data) == pytest.approx(expected_mean)


@pytest.mark.parametrize("data", [[1, 2, 3], [3, 2, 1]])
@pytest.mark.parametrize("expected_max", [3])
def test_max_sucess(data, expected_max):
    loguru.logger.info(f"data:{data}====result:{expected_max}")
    assert operation.op_max(data) == expected_max


@pytest.mark.parametrize("data", [[1, 2, 3], [1, 2, 3, 4], [3, 2, 1]])
@pytest.mark.parametrize("expected_min", [1])
def test_min_sucess(data, expected_min):
    assert operation.op_min(data) == expected_min
