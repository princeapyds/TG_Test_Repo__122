#THIS IS FOR AUTOMATIC & ELECTRI CARS
class Auto_Electric:
    colour=None
    battery_cap=None
    sun_roof=True

    def details(self, *args):
        print("You have entered below features : \n Colour :", self.colour, "\nTank Capacity : ", self.battery_cap,
              "\n Its Sunroof :", self.sun_roof)


