import re

pattern = r"\d{8}"
string = "身份证号为19990711"
match = re.search(pattern, string)
if match:
    print(match.group())
else:
    print("未匹配到身份证号")
