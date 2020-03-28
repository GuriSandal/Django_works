import re

ab = "this is ppppppy the python example"

#rs = re.findall("py",ab)

rs = re.search("python", ab)

print(rs.span())
print(rs.string)
print(rs.group())


result = re.finditer("py", ab)
for i in result:
    print(i.span())
    
    
