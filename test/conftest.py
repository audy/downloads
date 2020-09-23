import pytest
import os


@pytest.fixture
def run_in_tmp_path(tmp_path):
    """Run test in a temporary directory"""
    os.chdir(tmp_path)
    yield
