from src.manager import Manager
import pytest
import os
import json


class TestManager:
    @pytest.mark.parametrize("rot_type, result", [("rot13", 13), ("rot47", 47)])
    def test_should_passed_when_return_13_or_47(self, rot_type, result):
        assert Manager.rot_type2rot(rot_type) == result

    def test_should_passed_when_buffer_cleared(self):
        manager = Manager()
        manager.buffer.add_text("common string")
        manager.clear_buffer()
        assert manager.buffer.data == []
