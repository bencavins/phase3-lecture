class Car:
    def __init__(self, model):
        self.fuel = 100
        self.model = model
        self.engine = None
    
    def go(self):
        if self.engine.is_on:
            print('vroom')
            self.fuel -= 25
        else:
            print('engine is not running')
    
    def start(self):
        self.engine.is_on = True

class Engine:
    def __init__(self):
        self.cylinder_count = 8
        self.is_on = False
        self.car = None


if __name__ == '__main__':
    my_car = Car()
    my_engine = Engine()
    my_car.engine = my_engine
    my_engine.car = my_car

    my_car.start()
    print(my_car.engine.is_on)
    my_car.go()