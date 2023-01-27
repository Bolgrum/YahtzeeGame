def print_project_header(app_info, border="="*50, intro_message="Help Message Goes Here", ):
    """
    ------------------------------------------------------------------------------
    Function: print_project_header
    ------------------------------------------------------------------------------
    Description: This function prints to console the projects header that contains
    data about the project
    ------------------------------------------------------------------------------
    """
    # Prints the box containing information about the application
    print(border)    
    if type(app_info.get("author")) == list:
        print(
            "| App       : {:<9}|\n".format(app_info.get("name")) +
            "| Author(s) : {:<9}|\n".format(str(app_info.get("author")).strip("[]")) +
            "| Version   : {:<9}|\n".format(app_info.get("version")) +
            "| License   : {:<9}|".format(app_info.get("license"))
        )
    else:
        print(
            "| App       : {:<9}|\n".format(app_info.get("name")) +
            "| Author(s) : {:<9}|\n".format(app_info.get("author")) +
            "| Version   : {:<9}|\n".format(app_info.get("version")) +
            "| License   : {:<9}|".format(app_info.get("license"))
        )
    print(border)
    print(intro_message + '\n')
    
def print_rules():
    pass
