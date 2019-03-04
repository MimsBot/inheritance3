class System:

    def __init__(self):
        self.bodies = []

    def add(self, new_body):
        if new_body not in self.bodies:
            self.bodies.append(new_body)
        else:
            print("The body {} is already in the list.".format(new_body.name))
            return self.bodies

    def total_mass(self):
        current_mass = 0

        for num, body in enumerate(self.bodies):
            current_mass += body.mass
            return current_mass


class Body(System):

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


class Planet(Body):

    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year


class Star(Body):

    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type


class Moon(Body):

    def __init__(self, name, mass, month, planet):
        super().__init__(name, mass)
        self.month = month
        self.planet = planet


earth = Planet("earth", 12000, 20, 365)
neptune = Planet("neptune", 13999, 30, 1200)
sun = Star("sun", 150000, "G-type")
earth_moon = Moon("moon", 1500, 23, "earth")

solar_system = System()
solar_system.add(earth)
solar_system.add(neptune)
solar_system.add(sun)
print(solar_system)
print(solar_system.add(earth_moon))
print(solar_system.add(earth_moon))
print(solar_system.total_mass())
