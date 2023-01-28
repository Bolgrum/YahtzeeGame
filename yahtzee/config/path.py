import os

def set_project_paths() -> dict:
    # file paths
    project_root = os.path.dirname(os.path.dirname(__file__))
    sub_folder   = os.path.join(project_root, 'yahtzee')    
    
    project_paths = {
        "project_root" : project_root,
        "project_sub" : sub_folder,
    }
    return project_paths

def print_project_paths(paths: dict):
    for path in paths:
        print(paths[path])