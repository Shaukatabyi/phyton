def input_data():
    pass

def print_data(file_number = None):
    
    if file_number is None or file_number == 1:
        print('1 файл:')
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            data_first = file.readlines()
            data_first_second = []
            j = 0
            num = 1
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_second.extend([f"\n{num}.\n", ''.join(data_first[j:i]).strip(), '\n'])
                    j = i
                    num += 1
            data_first = data_first_second
            print(''.join(data_first))
    
    if file_number is None or file_number == 2:
        print('2 файл:\n')
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            data_second = list(file.readlines())
            num = 1
            for i in data_second:
                if i != '\n':
                    i = i.strip()
                    print(f'{num}. {i}')
                    num += 1       
       


def put_data():
    pass

def delete_data():
    pass