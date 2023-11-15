import re


def check_password(password):
    # 检查用户名是否合法
    if not re.match(r"^[a-zA-Z]\w{3,19}$", password):
        return False
    # 检查密码是否合法
    if not re.match(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{6,20}$", password):
        return False
    return True


username = input("请输入用户名：")
password = input("请输入密码：")

if check_password(password):
    print("密码合法")
else:
    print("密码不合法")
