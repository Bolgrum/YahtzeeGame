# CONSTANTS
INPUT_ENTRY_ERROR    = "Invalid Input\n"
MINIMUM_LENGTH_ERROR = "Input does not meet the minimum length\n"
MAXIMUM_LENGTH_ERROR = "Input exceeds the maximum length\n"

# CLASSES
class Error(Exception):
    pass

class MinLengthError(Error):
    pass

class MaxLengthError(Error):
    pass

class CharacterNotValid(Error):
    pass