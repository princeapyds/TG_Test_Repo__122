#Main Program
import M01
import M02
import M03
import M04
import re
class MainClass:
    def __init__(self):
        try:
            no_of_entry = int(input('Enter how many entries :'))
            for i in range(0,no_of_entry):
                variant = int(input("Please let us know what is the car variant\n press 1. Manual or press 2 for Automatic: "))
                if variant == 1:
                    print("Ok! so it's Manual with Gasoline")
                    self.colour = (input('Enter colour :'))
                    self.tank_cap = float(input('Enter tank capacity : '))
                    self.sun_roof = input('Is sun_roof available, please enter YES or NO :')
                    M01.Man_Gasoline.details(self, self.colour, self.tank_cap, self.sun_roof)
                elif variant == 2:
                    print("Ok! so it's Automatic \n")
                    module = input("Please let us know the fuel type \n Gas , Electric or Gas  & 1Electric \n")
                    if module == 'Gas' or module == 'gas':
                        print("Ok! so it's Gas with Gasoline")
                        self.colour = str(input('Enter colour :'))
                        self.tank_cap = float(input('Enter tank capacity : '))
                        self.sun_roof = input('Is sun_rooof available, please enter YES or NO :')
                        M02.Auto_Gasoline.details(self, self.colour, self.tank_cap, self.sun_roof)
                    elif module == 'Electric' or module == 'electric':
                        print("Ok! so it's Electric with Gasoline")
                        self.colour = str(input('Enter colour :'))
                        self.battery_cap = float(input('Enter tank capacity : '))
                        self.sun_roof = input('Is sun_rooof available, please enter YES or NO :')
                        M03.Auto_Electric.details(self, self.colour, self.battery_cap, self.sun_roof)
                    else:
                        print("Ok! so it's Gas & Electric")
                        self.colour = str(input('Enter colour :'))
                        self.tank_cap = float(input('Enter tank capacity : '))
                        self.battery_cap = float(input('Enter Battery Capacity :'))
                        self.sun_roof = input('Is sun_rooof available, please enter YES or NO :')
                        M04.Auto_Ele_Gas.details(self, self.colour, self.tank_cap, self.battery_cap, self.sun_roof)
                else:
                    print('Please provide valid input')


        except:
                print('please provide valid input')
                MainClass.__init__(self)


obj = MainClass()
