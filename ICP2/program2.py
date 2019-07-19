"""Write a python program to count number of words and characters in a file and the print the output."""


file_name = "prasad.txt"
chars = words = lines = 0
with open(file_name, 'r') as in_file:
    for line in in_file:
        lines += 1
        words += len(line.split())
        chars += len(line)
        print("num of words: ", words)
        print("num of characters:", chars)














"""

string=input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)
"""
