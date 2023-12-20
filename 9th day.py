#methods in strings
# strings are immutable
a="Khasim basha"
print(len(a))
print(a.upper())
print(a.lower())
# string methods will make changes in the stringitself
print(a.rstrip("!"))
print(a.replace("Khasim","John"))
# print(a.split(" "))
print(a.split("!"))
blogheading="introduction to Js"
# capitalize is used for only making the first alphabet as capital one
print(blogheading.capitalize())
str1="Welcometoconsole"
print(len(str1))
print(len(str1.center(50)))
print(str1)
print(a.count("Khasim basha"))
print(str1.endswith("!!!"))
print(str1.find("to"))
#index and find are similar but index throws the error by detecting an exception
print(str1.index("to"))
print(str1.isalnum())
print(str1.isupper())
print(str1.islower())
print(str1.isprintable())
print(str1.istitle())
print(str1.swapcase())