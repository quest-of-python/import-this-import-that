import subprocess
import unittest


class ImportThisImportThatAppTest(unittest.TestCase):
    def test_correct_algorithms(self):
        for algo in (
            "foo",
            "bar",
            "baz",
            "foobar",
            "barbaz",
        ):
            with self.subTest():
                res = subprocess.run(["python", "main.py", algo], capture_output=True)

                self.assertEqual(res.returncode, 0)
                self.assertEqual(
                    f"Running {algo} algorithm.", res.stdout.decode("utf-8").strip()
                )

    def test_bad_algorithm(self):
        res = subprocess.run(["python", "main.py", "aaa"], capture_output=True)

        self.assertEqual(res.returncode, 1)
        self.assertEqual(res.stdout.decode().strip(), "Algorithm aaa not supported.")


if __name__ == "__main__":
    unittest.main()
