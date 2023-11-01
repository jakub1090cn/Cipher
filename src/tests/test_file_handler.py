import pytest
import os
import json
from src.file_handler import FileHandler

@pytest.fixture
def setup_test_files():
    test_data = {
        "data": "common text"
    }
    with open('test_file.json', 'w') as f:
        json.dump(test_data, f)
    yield
    if os.path.exists('test_file.json'):
        os.remove('test_file.json')
    if os.path.exists('created_file.json'):
        os.remove('created_file.json')

def test_should_passed_when_read_data(setup_test_files):
    expected = {
        "data": "common text"
    }
    assert FileHandler.read_from_file('test_file.json') == expected

def test_should_passed_when_written(setup_test_files):
    data_to_write = "some new data"
    FileHandler.write_to_file('created_file.json', data_to_write)
    written_data = FileHandler.read_from_file('created_file.json')
    expected = {
        "data": "some new data"
    }
    assert written_data == expected

def test_should_passed_when_appended(setup_test_files):
    data_to_append = " and some appended text"
    FileHandler.append_to_file('test_file.json', data_to_append)
    appended_data = FileHandler.read_from_file('test_file.json')
    expected = {
        "data": "common text and some appended text"
    }
    assert appended_data == expected

def test_should_passed_when_file_is_cleared(setup_test_files):
    FileHandler.clear_file('test_file.json')
    cleared_data = FileHandler.read_from_file('test_file.json')
    expected = {"data": ""}
    assert cleared_data == expected
