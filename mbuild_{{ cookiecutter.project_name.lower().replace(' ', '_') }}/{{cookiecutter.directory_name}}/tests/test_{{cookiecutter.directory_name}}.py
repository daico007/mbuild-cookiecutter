"""
Unit and regression test for the {{cookiecutter.directory_name}} package.
"""

# Import package, test suite, and other packages as needed
import {{cookiecutter.directory_name}}
import pytest
import sys
import mbuild as mb

def test_{{cookiecutter.directory_name}}_imported():
    """ Sample test, will always pass so long as import statement worked """
    assert "{{cookiecutter.directory_name}}" in sys.modules

def test_import():
    """ Test that mBuild recipe import works """
    assert "{{cookiecutter.first_plugin_name}}" in vars(mb.recipes).keys()
