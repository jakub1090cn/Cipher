import pytest
from src.manager import Manager


class TestRotType2Rot:

    @pytest.mark.parametrize('rot_type', ['rot13', 'rot47'])
    def test_should_return_13_or_47(self, rot_type):
        assert Manager.rot_type2rot(rot_type) == 13 or 47


class TestClearBuffer:
    def test_clear_buffer_should_return_0(self):
        manager = Manager()
        manager.buffer.add_text("Test data")
        manager.clear_buffer()
        assert len(manager.buffer.data) == 0

class TestSaveToFile:
    @pytest.mark.parametrize('file_name', ["test_file", "example"])
    def test_should_return_true_if_file_exists(self, file_name, tmp_path):
        manager = Manager()
        file_name = tmp_path / file_name
        manager.buffer.add_text("Test data")
        manager.save_to_file(file_name)
        assert file_name.exists()