#  Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

def here_document(s):
    return s

if __name__ == "__main__":
    s = """ a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example """
    print(here_document(s))