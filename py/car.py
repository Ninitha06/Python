class Car(object):
    def __init__(self, name, model, color, company, speedLimit):
        self.name = name
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def accelerate(self):
        print("Accelerating the car")

    def gearChanged(self, gearType):
        print("Gear changed to " + gearType)
    


car1 = Car("Celerio", "C870", "red", "MAruthi", 90)
car1.accelerate()
car1.start()
car1.gearChanged("fast")
print(car1.name)