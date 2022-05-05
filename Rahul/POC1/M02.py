#THIS IS FOR AUTOMATIC & GASOLINE CARS
class Auto_Gasoline:
    colour=None
    tank_cap=None
    sun_roof=True

    def details(self, *args):
        print("You have entered below features : \n Colour :", self.colour, "\nTank Capacity : ", self.tank_cap,
              "\n Its Sunroof :", self.sun_roof)
