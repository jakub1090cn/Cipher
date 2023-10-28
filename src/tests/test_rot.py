import pytest
from src.rot import Rot


def test_should_return_encrypted_text():
    assert Rot.encrypt_text('a', 13) == 'n'
    assert Rot.encrypt_text('a', 47) == 'v'


def test_should_return_decrypted_text():
    assert Rot.encrypt_text('a', 13) == 'n'
    assert Rot.encrypt_text('a', 47) == 'v'
