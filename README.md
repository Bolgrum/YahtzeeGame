## INITIAL PULL FROM BRANCH PYTHON ON GITHUP
Make sure that you have in your settings.json file the following code.
```
{
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}"
      }
}
```
This code will tell the python interpreter to also look at pythonpath(project_root) for additional modules. This will allow you use the other modules within the project. For example, the following code becomes possible.
```
#..\tests\test_path.py

from yahtzee import output
```
However, if you do not set up settings.json the above code will give you the following error
```
ModuleNotFoundError: No module named 'yahtzee'.
```
