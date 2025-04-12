class Engine:
    def getRPM(self):
        return 3000 # valor por defecto del motor
    
class Vehicle:
    def __init__(self, name, speed, engine):
        self._name = name
        self._speed = speed
        self._engine = engine
    
    def getName(self):
        return self._name # metodo protegido
    
    def getEngineRPM(self):
        return self._engine.getRPM()
    
    def getMaxSpeed(self):
        return self._speed

# Esta clase se encargará de imprimir los datos
class VehiclePrinter:
    def __init__(self, vehicle):
        self._vehicle = vehicle
    
    def printInfo(self):
        print(
            "Vehicle: {}, Max Speed: {}, RPM: {}".format(
                self._vehicle.getName(),
                self._vehicle.getMaxSpeed(),
                self._vehicle.getEngineRPM(),
            ))

class VehiclePersistance:
    def __init__(self, vehicle, db):
        self._vehicle = vehicle
        self._persistance = db
        print("Hey, storing data!", self._persistance)

if __name__ == "__main__":
    engine = Engine()
    vehicle = Vehicle(name = "Car", engine = engine, speed = 200)
    peristance = VehiclePersistance(vehicle, db = "Firebase")
    printer = VehiclePrinter(vehicle = vehicle)
    printer.printInfo()