def create_file_with_numbers(n):
    file = open('range_'+str(n)+'.txt', 'w')
    for i in range(1, n+1):
        file.write(str(i)+'\n')
    file.close()


create_file_with_numbers(5)


