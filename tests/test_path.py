import os
import sys
import unittest
from yahtzee import output

def print_project_path_info():
    print("In module products __package__, __name__ ==", __package__, __name__)
    print_pythonpath()

def print_pythonpath():
    for path in sys.path:
        print(path)

class TestPaths(unittest.TestCase):
    def test_paths(self):
        pass

# Test Script
project_paths: dict = output.set_project_paths()
print("=" * 100)
print("test_path.py test script")
print("=" * 100)
print("Project Files Paths:")
print("Project Root Path   :", project_paths.get("project_root"))
print("Project Source Path :", project_paths.get("project_sub"))
print()

print("Project PYTHONPATH:")
print_pythonpath()
print("=" * 100)