  
def pot(operation, num_rows = 6, num_columns = 6):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(operation(i, j), end = ' ')
        print()

pot(lambda x, y: x*y)
