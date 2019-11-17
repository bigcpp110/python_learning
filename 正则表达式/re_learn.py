import re

a="-你好"
res=re.match("\w",a)#首字母
res=re.search("\b",a)

import re
s = " ever !mm"
print(re.findall(r'\b', s))