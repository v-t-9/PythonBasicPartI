#Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
# Original sequence: 01010101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False
# Original sequence: 000111000111
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# True
# Original sequence: 00011100011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False


def sequence_zeroes_followed_by_ones(s): 
    l = []
    for i in s:
        if i == "0":
            l.append(i)
        else:
            l.pop()
    if l == []:
        return True
    else:
        return False

if __name__ == "__main__":

    s1 = "01010101"
    s2 = "00"
    s3 = "000111000111"
    s4 = "00011100011"
    print(sequence_zeroes_followed_by_ones(s1))
    print(sequence_zeroes_followed_by_ones(s2))
    print(sequence_zeroes_followed_by_ones(s3))
    print(sequence_zeroes_followed_by_ones(s4))

