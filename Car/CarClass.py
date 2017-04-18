class Car(object):

    def __init__(self, *args): #taking arguments provided

      #check if name and model are passed, else set as defualts
      if len(args) >= 2:
        self.name = args[0]
        self.model = args[1]
      else:
        self.name = 'General'
        self.model = 'GM'
        

      if self.name == 'Porshe' or self.name == 'Koenigsegg': 
        self.num_of_doors = 2
      else:
        self.num_of_doors = 4

      #check if cartypr is passed, else set as saloon
      if len(args) >= 3:
        self.car_type = args[2]
      else:
        self.car_type = 'saloon'

      #set number of wheels
      if self.car_type == 'saloon':
        self.num_of_wheels = 4
      else:
        self.num_of_wheels = 8

      self.speed = 0

    #set car type to sallon
    def is_saloon(self):
      return self.car_type == 'saloon'

    #set speed when car drives
    def drive(self, speed):
        if self.car_type == 'saloon':
            self.speed = speed * (1000 / 3)
        else:
            self.speed = speed * 11
        return self