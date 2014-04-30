import re

# match = re.search(pat, str)

str = "alice_-_b@google.com"

match = re.search(r'([\w.-]+)@([\w.-]+)', str)

if match:
    print('Match found: ', match.group())
    print('Match found: ', match.group(1))
    print('Match found: ', match.group(2))
else:
    print('No match')

#findall
## Suppose we have a text with many email addresses
str1 = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str1) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print('Each Email : ', email)
    
    
#findall With Files
# Open file
f = open('regex.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'Python', f.read())
for string in strings:
    # do something with each found email string
    print('Each String : ', string)
    

# Case Insensitive Search using compile
str = "Mother Teresa"
print("\n Input Str : ", str);
keyword = re.compile(r"mother ", re.IGNORECASE)  #Case Insensitive Search
if (keyword.search(str)):
    print("Matched Str");
else:
    print("NOT Matched Str");


#re.search('hello', 'hello world').group() 
#vs
#re.match('hello', 'hello world').group()
#vs
#re.compile('hello').match('hello world').group()


# Case Insensitive Search
str = "Mother Teresa"
print("\n Input Str : ", str);
match = re.search(r"mother ", str, re.IGNORECASE)  #Case Insensitive Search

if (match):
    print("Matched Str :", match.group());
else:
    print("NOT Matched Str");    
    
    
"""    
if match:
    print('Match found: ', match.group())
else:
    print('No match')
"""

