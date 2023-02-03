class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if Clock.__check_time(tm) == True:
            self.__time = tm

    @classmethod
    def get_time(self):
        Clock.__time = self.time


    @classmethod
    def __check_time(self, tm):
        self.tm = tm
        if type(self.tm) in int and self.tm >=0 and self.tm < 100_000:
            return True




clock = Clock(4530)
clock.set_time(500)
print(clock.get_time())