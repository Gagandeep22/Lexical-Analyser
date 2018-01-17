
# coding: utf-8

# In[3]:

from sys import exit

print("Lexical Analyzer - List the tokens")

fileName = input("Enter the name of the file: ")
try:
    codeFile = open(fileName,"r")
    numFile = open("num.txt","r")
    operatorFile = open("operator.txt","r")
    keywordFile = open("keyword.txt","r")
    specialCharFile = open("specialchar.txt","r")
except:
    print("Error in one of the files, either file not present or incorrect file name!!")
    exit(0)

numbers = [num.strip() for num in numFile]
operators = [op.strip() for op in operatorFile]
keywords = [keyword.strip() for keyword in keywordFile]
specialChars = [chars.strip() for chars in specialCharFile]

alpha = False
number = False
value = ''

tokens = {'variables': [], 'special': [], 'operator': [], 'keyword': [], 'numbers': []}

for line in codeFile:
    for character in line:
        if character != '\n':
            if character.isdigit():
                value += character
                if not alpha:
                    number = True
            elif character in operators or character in specialChars or character == ' ':
                if character in operators:
                    if character not in tokens['operator']:
                        tokens['operator'].append(character)
                elif character in specialChars:
                    if character not in tokens['special']:
                        tokens['special'].append(character)
                if number:
                    if value not in tokens['numbers']:
                        tokens['numbers'].append(value)
                elif alpha:
                    if value in keywords:
                        if value not in tokens['keyword']:
                            tokens['keyword'].append(value)
                    else:
                        if value not in tokens['variables']:
                            tokens['variables'].append(value)
                alpha = False
                number = False
                value = ''
            else:
                value += character
                num = False
                alpha = True
                  
print("\nThe Tokens in the given C file are: \n")
for types in tokens:
    print(types)
    for val in tokens[types]:
        print("\t"+val)
    print("\n")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



