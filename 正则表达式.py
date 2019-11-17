import re
#
# string1=" 5569"
# string2="4569"
# pattern="(?<!4)56(?=9)"
# ret=re.findall(pattern,string2)
# print(ret)
#
# s = "ip='230.192.168.78',version='1.0.0'"
# res=re.search(r"ip='(?P<ip>\d+\.\d+\.\d+\.\d+).*", s)
# print(res.group('ip'))#通过命名分组引用分组
#
# print(re.search(r'(?P<name>go)\s+(?P=name)\s+(?P=name)', 'go go go').group('name'))
# print(re.search(r'(go)\s+\1\s+\1', 'go go go').group())
#
# s = 'abc.xyz'
# print(re.sub(r'(.*)\.(.*)', r'\2.\1', s))
#
# s1='''char *a="hello world"; char b='c'; /* this is comment */ int c=1; /* t
# his is multiline comment */'''
#
# print(re.findall( r'(?<=/\*).+?(?=\*/)' , s1 ,re.M|re.S))

# pattern="indestr(?=y|ies)"
# print(re.match(pattern,"indestries"))

s="123<div>antzone"
reg="(?!>)<[^>]+>\w+"
print(re.match(reg,s))