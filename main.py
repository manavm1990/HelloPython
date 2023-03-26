from car import Car

if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed? ").upper()
        if action not in "ABOS" or not action:
            print("I don't know how to do that")
            continue
        if action == 'A':
            print(my_car.accelerate())
        elif action == 'B':
            print(my_car.brake())
        elif action == 'O':
            print("The car has driven {}km".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {}km/h".format(my_car.get_average_speed()))
        print(my_car.step())
