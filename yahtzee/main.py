# Std lib
import sys

# Custom libs
import yahtzee

# Run main program
if __name__ == "__main__":    
    if len(sys.argv) > 1:
        # Used for command line entry ex. python main.py <arg>
        if sys.argv[1].lower() == 'gui':
            yahtzee.run_gui()
            
        if sys.argv[1].lower() == "console":
            yahtzee.run_console()