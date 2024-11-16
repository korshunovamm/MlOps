from typing import List, Callable
import time
import numpy as np
from scipy.spatial.distance import chebyshev as scipy_chebyshev

import chebyshevDistance

def test_timings(func: Callable, *args):
    _ = func(*args)
    start_time = time.time()
    _ = func(*args)
    end_time = time.time()
    return round(end_time - start_time, 5)

def compare(vector_size: int) -> None:
    v1 = np.random.randint(1, vector_size, size=vector_size)
    v2 = np.random.randint(1, vector_size, size=vector_size)

    print(
        "Chebyshev Distance two vectors of {0} size: Pure C++ {1} seconds; Python scipy {2} seconds".format(
            vector_size, test_timings(chebyshevDistance.ChebyshevDistance.chebyshevDistance,
                                      v1, v2), test_timings(scipy_chebyshev, v1, v2)
        )
    )


if __name__ == "__main__":
    for vector_size in [100, 500, 800, 1000, 5000, 10000]:
        compare(vector_size)