def file_n_lines(file_name: str, n: int) -> None:
        f = open(file_name, 'r')
        for i in range(n):
             print(f.readline(), end='')


file_n_lines('test.txt', 3)
