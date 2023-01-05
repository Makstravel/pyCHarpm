def print_from(n: int) -> None:
        if n>1:
                print_from(n-3)
        print(n)


print_from(5)