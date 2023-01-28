import sys
import unittest
from yahtzee import output

def print_pythonpath():
    for path in sys.path:
        print(path)

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