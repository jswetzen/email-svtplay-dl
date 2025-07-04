import unittest
import subprocess
import os

class TestParseMailUrl(unittest.TestCase):
    def run_script(self, input_file):
        script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'parsemailurl.py'))
        with open(input_file, 'rb') as f:
            result = subprocess.run(['python3', script], stdin=f, capture_output=True, text=True)
        return result.stdout.strip()

    def run_example(self, n=1):
        output = self.run_script(os.path.join(os.path.dirname(__file__), f'input{n}.txt'))
        with open(os.path.join(os.path.dirname(__file__), f'output{n}.txt')) as f:
            expected = f.read().strip()
        self.assertEqual(output, expected)

    def test_example_1(self):
        self.run_example(1)

    def test_example_2(self):
        self.run_example(2)

    def test_example_3(self):
        self.run_example(3)

if __name__ == '__main__':
    unittest.main()
