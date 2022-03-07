class Bus:
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        bus_list.append(self)



# main routine
bus_list = []

b1 = Bus("2010", "Y", "Greg")
b2 = Bus("2011", "P", "Joel")
b3 = Bus("2012", "X", "Jack")

for bus in bus_list:
    print(f"Bus number is {bus.number}, route is {bus.route} and the driver is {bus.driver}")
    f(bus)