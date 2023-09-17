

class Dog:
    MIN_AGE = 0
    @classmethod
    def validate_age(cls, age):
        if not isinstance(age, int):
            return False
        if not age >= 0:
            return False
        return True

    def __init__(self, age:int) -> None:
        ''' ## возраст целое положительное число'''
        self.age = 0
        if self.validate_age(age=age):
            self.age=age

    def __str__(self) -> str:
        return f"{self.age}"


print(Dog('2'))