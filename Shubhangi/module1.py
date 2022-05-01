class M01:
    def __init__(self, colour, tank_cap, mileage, model_type, engine_type, seats, gear_box, backup_camera):
       self.colour = colour
       self.tank_cap = tank_cap
       self.mileage = mileage
       self.model_type = model_type
       self.engine_type = engine_type
       self.seats = seats
       self.gear_box = gear_box
       self.backup_camera = backup_camera
    def __str__(self):
        return f'Colour : {self.colour}\nTank Capacity: {self.tank_cap}\nMileage: {self.mileage}\nModel Type: {self.model_type}\nEngine_Type: {self.engine_type}\nSeats: {self.seats}\nGear Box: {self.gear_box}\nBackup_Camera: {self.backup_camera}'

car1 = M01('Red',45,18.5,'Manual','Gasoline',7,'6-Speed','Yes')


class M02(M01):
    def __init__(self, colour, tank_cap, mileage, model_type, engine_type, seats, gear_box, backup_camera):
       super().__init__(self, colour, tank_cap, mileage, model_type, engine_type, seats, gear_box, backup_camera)
car2 = M01('White', 40, 17.5, 'Automatic', 'Gasoline', 4, '6-Speed', 'Yes')

class M03(M01):
    def __init__(self, colour, tank_cap, mileage, model_type, engine_type, seats, gear_box, backup_camera):
       super().__init__(self, colour, tank_cap, mileage, model_type, engine_type, seats, gear_box, backup_camera)
car3 = M01('Silver', 35, 16.5, 'Automatic', 'Electric', 4, '6-Speed', 'Yes')

class M04(M01):
    def __init__(self, colour, tank_cap, mileage, model_type, engine_type, seats, gear_box, backup_camera):
       super().__init__(self, colour, tank_cap, mileage, model_type, engine_type, seats, gear_box, backup_camera)
car4 = M01('Silver', 45, 19.5, 'Automatic', 'Gasoline and Electric', 7, '6-Speed', 'Yes')

Model_Name = input("Enter model name: ")
if Model_Name == 'M01':
       print(car1)
elif Model_Name == 'M02':
       print(car2)
elif Model_Name == 'M03':
       print(car3)
elif Model_Name == 'M04':
     print(car4)
else:
    print("Wrong input ")




