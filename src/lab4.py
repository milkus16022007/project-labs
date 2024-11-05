class TourPackage:
    num_people = 1
    tour_type = "Standard"

    def __init__(self, country="", duration=0, price=0.0):
        self.__country = country 
        self.__duration = duration  
        self.__price = price  

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"TourPackage(country={self.__country}, duration={self.__duration} days, price={self.__price} EUR)"

    def __repr__(self):
        return f"TourPackage({self.__country!r}, {self.__duration!r}, {self.__price!r})"

    def __del__(self):
        print(f"TourPackage for {self.__country} is being deleted")

def main():
    package1 = TourPackage("Italy", 7, 1500)
    package2 = TourPackage("Spain", 10, 2000)
    package3 = TourPackage("Greece", 5, 1200)

    print(package1)
    print(package2)
    print(package3)

    print("Country of package1:", package1.get_country())
    print("Duration of package2:", package2.get_duration())
    print("Price of package3:", package3.get_price())

if __name__ == "__main__":
    main()


