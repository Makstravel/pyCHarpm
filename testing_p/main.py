def find_lines_len_more_6(file_name:str) -> int:
    with open(file_name, 'r') as f:
        s= [i for i in f.read().splitlines()]
        x= 0
        for i in s:
            if len(i) >6:
                x+=1
        return x





