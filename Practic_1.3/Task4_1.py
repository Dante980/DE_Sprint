from fileinput import close
from inspect import stack
str_ = input()

while(True):
    temp = str_ 
    str_ = str_.replace("{"+"}", "")
    str_ = str_.replace("[]", "")
    str_ = str_.replace("()", "")
    if str_ == "":
        print(True)
        break
    if temp == str_:
        print(False)
        break