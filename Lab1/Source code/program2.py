str1 = []
with open("file1.txt", "r") as f:
  for line in f:
    str1.append(line.strip().lower())

s1=list(str1[0].split(" "))

print(s1)
str2 = []
with open("file2.txt", "r") as f:
  for line in f:
    str2.append(line.strip())

s2=list(str2[0].split(" "))
new_str= " "

print(s2)

print("\nThe final output is:\n ")
for i in s1:
    for j in s2:
        if i == j:
            ind = s1.index(i)
            s1[ind] = ""

print(' '.join(s1))