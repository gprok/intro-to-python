
class Car:
    def __init__(self, pl, col):
        self.plate = pl
        self.color = col

    def __str__(self):
        return self.plate + ", color: " + self.color


a = Car("AA111", "red")

b = Car("BB909", "yellow")


print(a)
print(b)

