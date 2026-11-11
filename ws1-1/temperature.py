class Temperature:
    def __init__(self):
        self.celsius = 1.0

    def convert_to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def check_is_freezing(self):
        if (self.celsius <= 0):
            print("So god damn cold")
        else:
            print("My icecream is melting")

        return

    def check_weather(self):
        if (self.celsius <= 0):
            print("brrrr it's freezing")
        elif (self.celsius <= 10):
            print("Grab a jacket")
        elif (self.celsius <= 18):
            print("It's cool out")
        elif (self.celsius <= 25):
            print("Yeah, the sun <3")
        elif (self.celsius <= 35):
            print("Classic Australia")
        else:
            print("Heat wave time :(")

        return


if __name__ == "__main__":
    temperature = Temperature()

    for c in [1.0, -10.0, 25.0, 35.0]:

        temperature.celsius = c
        print(temperature.convert_to_fahrenheit())
        temperature.check_is_freezing()
        temperature.check_weather()

        print()
