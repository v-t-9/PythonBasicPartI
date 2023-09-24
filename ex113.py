# Write a Python program that inputs a number and generates an error message if it is not a number.
  
if __name__ == "__main__":
    try: 
        num = int(input("Enter a number: "))
        print(f"The number is {num}")
    except ValueError:
        print( "You haven't entered a number.")
        