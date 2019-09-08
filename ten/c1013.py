import re
s = "ABC296D99977"
s = "11ABC296D99977"

# def findall(pattern, string, flags=0)
r = re.findall('\d', s)
print(r)
# def match(pattern, string, flags=0):
r1 = re.match('\d', s)
print(r1, r1.group(), r1.span())
# def search(pattern, string, flags=0):
r2 = re.search("\d", s)
print(r2, r2.group(), r2.span())