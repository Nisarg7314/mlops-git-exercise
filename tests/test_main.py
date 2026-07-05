import io
import sys
import unittest

from mlops_github.main import main


class TestMain(unittest.TestCase):
    def test_main_prints_message(self):
        captured = io.StringIO()
        sys_stdout = sys.stdout
        try:
            sys.stdout = captured
            main()
        finally:
            sys.stdout = sys_stdout

        self.assertIn("Hello from mlops_github!", captured.getvalue())


if __name__ == "__main__":
    unittest.main()
