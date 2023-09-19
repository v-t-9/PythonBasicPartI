# Write a Python program to concatenate N strings.

def concat_str(n):
   ac = ""
   i = 0

   while i < n:
      t = input("Enter a text: ")
      ac = ac + " " + t
      i = i + 1

   return ac.lstrip()

if __name__ == "__main__":
 n = int(input("Enter a number: "))
 print(concat_str(n))

 
