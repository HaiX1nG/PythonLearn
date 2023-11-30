class Phones:
    def call(self):
        print("使用手机打电话")


class iPhone(Phones):
    def call(self):
        print("使用iPhone打电话")


class APhone(Phones):
    def call(self):
        print("使用Android手机打电话")


class Person:
    def use_phone_call(self, phone):
        phone.call()


phone1 = iPhone()
phone2 = APhone()

person = Person()

person.use_phone_call(phone1)
person.use_phone_call(phone2)
