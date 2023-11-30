class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"用户信息摘要：{self.first_name}{self.last_name}，年龄：{self.age}，所在地：{self.location}")

    def greet_user(self):
        print(f"欢迎您，{self.first_name}{self.last_name}！")


user1 = User("张", "三", 25, "北京")
user2 = User("李", "四", 30, "上海")
user3 = User("王", "五", 28, "广州")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
