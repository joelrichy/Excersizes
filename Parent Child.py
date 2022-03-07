class Staff:
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job

    class Management:
        def __init__(self, car):
            self.car = car

    class Clerical:
        def __init__(self, typing_speed):
            self.typing_speed = typing_speed

    class Factory:
        def __init__(self): []