class Clock:
    def __init__(self, tm):
        self.__time = 0
        self.set_time(tm)

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


    @classmethod
    def __check_time(cls, tm):
        return type(tm) == int and 0 <= tm < 100_000



clock = Clock(4530)
clock.set_time(15)
print(clock.get_time())  #15
clock.set_time(100000)
clock.set_time(-1)
clock.set_time('2')
clock.set_time(0.1)
print(clock.get_time())  #15