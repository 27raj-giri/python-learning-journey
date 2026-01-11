# Create a Time class with hours, minutes, seconds. Add a method to display time in HH:MM:SS format.

class Time:
    def __init__(self, hours, minutes, seconds):
        self.h = hours
        self.m = minutes
        self.s = seconds

    def show_time(self):
        print(f"{self.h}:{self.m}:{self.s}")

t = Time(11, 33, 27)
t.show_time()