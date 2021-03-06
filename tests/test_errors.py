from pyxl.codec.transform import pyxl_transform_string
from pyxl.codec.tokenizer import PyxlParseError
from pyxl.codec.parser import ParseError

import os

error_cases_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'error_cases')

def _expect_failure(file_name):
    path = os.path.join(error_cases_path, file_name)
    try:
        with open(path, 'r') as f:
            print(pyxl_transform_string(f.read()))
        assert False, "successfully decoded file %r" % file_name
    except (PyxlParseError, ParseError):
        pass

def test_error_cases():
    cases = os.listdir(error_cases_path)
    for file_name in cases:
        if file_name.endswith(".txt"):
            _expect_failure(file_name)
