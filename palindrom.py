x= input('enter something to chech the Palindrome :\n')
print("your input: ",x)

print("inverse input :",x[::-1])
if x==x[::-1]:
    print("its Palindrome")
else:
    print("no its not Palindrome")