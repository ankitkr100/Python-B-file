#import string
##
#new_str = str1.translate(str.maketrans('', '', string.punctuation))
#print("New string is:", new_str)

import re
str1 = "/*Jon is @developer & musician"
print("original string is :", str1)

#replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is :", res)



