class Human:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지 마라")

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))

    def sentinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("아름", 25, "여자")
areum.who()

del(areum)