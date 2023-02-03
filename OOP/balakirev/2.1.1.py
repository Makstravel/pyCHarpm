class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):

    def get_time(self):

    def __check_time(self, tm):
        self.tm = tm
        if type(self.tm) in int and self.tm >=0 and self.tm < 100_000:
            return True




clock = Clock(4530)