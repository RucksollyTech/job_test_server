import pytest
from my_web_socket.server import compute_sum_numbers
# Here we test our compute_sum_numbers
@pytest.mark.asyncio
async def test_compute_sum_numbers():
    assert await compute_sum_numbers(1, 2) == 3
    assert await compute_sum_numbers(10, 5) == 15
    assert await compute_sum_numbers(-5, 5) == 0
    assert await compute_sum_numbers(3.5, 2.5) == 6.0
