import pytest
from src.buffer import Buffer
from src.text import Text
from unittest.mock import mock_open, patch

def test_add_text():
    buffer = Buffer()
    text = Text("example text", "rot13", "Encrypted")
    buffer.add_text(text)
    assert buffer.data == [text]

def test_save_to_file():
    buffer = Buffer()
    text = Text("example text", "rot13", "Encrypted")
    buffer.add_text(text)
    with patch("builtins.open", mock_open()) as mocked_file:
        buffer.save_to_file("test_file.txt")
        mocked_file.assert_called_once_with("test_file.txt", "w")
        mocked_file().write.assert_called_once_with(f"{text}\n")

def test_load_from_file():
    buffer = Buffer()
    file_content = "example text\nanother example\n"
    with patch("builtins.open", mock_open(read_data=file_content)):
        buffer.load_from_file("test_file.txt")
        assert buffer.data == ["example text", "another example"]

def test_convert_data_to_list_of_dicts():
    buffer = Buffer()
    text1 = Text("example text", "rot13", "Encrypted")
    text2 = Text("another example", "rot13", "Encrypted")
    buffer.add_text(text1)
    buffer.add_text(text2)
    result = buffer.convert_data_to_list_of_dicts()
    expected = [{"text": "example text", "rot_type": "rot13", "status": "Encrypted"},
                {"text": "another example", "rot_type": "rot13", "status": "Encrypted"}]
    assert result == expected

def test_clear_buffer():
    buffer = Buffer()
    text = Text("example text", "rot13", "Encrypted")
    buffer.add_text(text)
    buffer.clear_buffer()
    assert buffer.data == []
