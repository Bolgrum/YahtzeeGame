from . import errors

# FUNCTIONS DEFINITIONS
def user(input_prompt="<Input Command:>", input_range_tup=(1,150), valid_chars=None):
    # Try to input into console based on the class specifications
    try:
        console_input = input(input_prompt)

        if len(console_input) < input_range_tup[0]:
            raise errors.MinLengthError
        
        if len(console_input) > input_range_tup[1]:
            raise errors.MaxLengthError
        
        if valid_chars is not None:
            if not check_valid_chars(console_input):
                raise errors.CharacterNotValid

        taken_input = console_input

        return taken_input

    # Exception that is raised when input exceeds the maximum length
    except errors.MinLengthError:
        print(errors.MINIMUM_LENGTH_ERROR)
        return user(input_prompt, input_range_tup, valid_chars)

    # Exception that is raised when input exceeds the maximum length
    except errors.MaxLengthError:
        print(errors.MAXIMUM_LENGTH_ERROR)
        return user(input_prompt, input_range_tup, valid_chars)

    # Exception that is raised when input is not in the valid range of characters
    except errors.CharacterNotValid: 
        print(errors.INPUT_ENTRY_ERROR)
        return user(input_prompt, input_range_tup, valid_chars)

def check_valid_chars(input_string, valid_chars):
    valid_input = True

    # Loops through the length of the inputValue checking each character
    for index in range(len(input_string)):
        if input_string[index] not in valid_chars:
            valid_input = False
            break
        index += 1

    return valid_input