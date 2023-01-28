## INITIAL PULL FROM GITHUB ON BRANCH PYTHON
Make sure that you have in your settings.json file the following code.
```
{
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}"
      }
}
```
this code will set the root pythonpath path as your root folder for the project. This will allow you use the other modules within the project, for example.
if you are in ../tests the following code is possible with the above setup.
```
#..\tests\test_path.py

from yahtzee import output
```
However, if you do not set up settings.json the above code will give you the following error
```
ModuleNotFoundError: No module named 'yahtzee'.
```
