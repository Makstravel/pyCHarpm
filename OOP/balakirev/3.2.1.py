import random


class RandomPassword:

    def __init__(self, psw_chrs: str, min_pass: int, max_pass: int):
        self.psw_chrs = psw_chrs
        self.min_pass = min_pass
        self.max_pass = max_pass

    def __call__(self, *args, **kwargs):
        length = random.randint(self.min_pass, self.max_pass)
        return ''.join(random.choices(self.psw_chrs, k=length))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd(), rnd(), rnd()]

print(lst_pass)
