class character:
    def __init__(self, speed, damage, durability):
        self.speed = speed
        self.damage = damage
        self.durability = durability

    def double_speed(self):
        self.speed *= 2

ninja = character(90, 30, 30)

hulk = character(50, 90, 80)

print (f"The ninja's speed is {ninja.speed}")
print (f"The hulk's speed is {hulk.speed}")

ninja.double_speed()

print(f"The ninja's double speed is {ninja.speed}")
print(f"The hulk's double speed is {hulk.speed}")
        