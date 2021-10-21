# PRZYPOMNINIE DO KLAS
class House:
    doors: int
    color: str

    def __init__(self, doors: int, color: str) -> None:
        self.doors = doors
        self.color = color

    def change_color(self, new_color: str) -> None:
        if new_color == self.color:
            raise ValueError('Operacja niedozwolona')
        self.color == new_color

    def __str__(self) -> str:
        return 'liczba drzwi:{0}, kolor: {1}'.format(self.doors, self.color)

    def __len__(self) -> int:
        return 11

green_house: House = House(doors=20, color='green')
blue_house: House = House(doors=10, color='blue')
print(green_house.doors)
print(green_house.color)

print(green_house)
print(blue_house)

print(len(blue_house))



# ASSERT
def sum_(x: int, y: int) -> int:
    return x + y

assert sum_(2, 6) == 8
assert sum_(12, 16) == 28



