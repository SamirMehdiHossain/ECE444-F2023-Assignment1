import utils
utilsObject = utils.Utils


print(utilsObject.reversed(1234))
print(utilsObject.reversed(12.34))
print(utilsObject.reversed("string"))

print(utilsObject.reversed(4985586))
print(utilsObject.reversed(4985.586))
print(utilsObject.reversed("hello"))

print(utilsObject.formatter(1234))
print(utilsObject.formatter(12.34))
print(utilsObject.formatter("string"))

print(utilsObject.formatter(4985586))
print(utilsObject.formatter(4985.586))
print(utilsObject.formatter("hello"))
