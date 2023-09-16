import sys
# Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
def command_line_arguments():
    return f"Total arguments {len(sys.argv)}\nName of the script {sys.argv[0]}\nArguments {str(sys.argv)}"
if __name__ == "__main__":
    print(command_line_arguments())