
#1. search in a string and find the first non-repeated characters in that string

str = input("enter the input:")
str=str.lower()
new_str = str.replace(' ', '')
print(new_str)
s=list(new_str)
s1=s
print(s)

print("the non- repeated terms are:")
for i in new_str:

    count = 0
    for j in new_str:

        if i == j:
            count+=1
    if count == 1:
        print(i)