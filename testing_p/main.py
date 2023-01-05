def print_from(n: int) -> None:
        if n>1:
                print_from(n-1)
        print(n)


print_from(5)