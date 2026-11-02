import unittest

import numpy as np

from task import Task


class TestTask(unittest.TestCase):
    def test_work(self):
        task = Task(identifier=1, size=10)
        task.work()

        # Check that Ax = B
        np.testing.assert_allclose(
            task.a @ task.x,
            task.b,
            rtol=1e-5,
            atol=1e-8,
        )


if __name__ == "__main__":
    unittest.main()
