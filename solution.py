def read_input_file():
    with open("input.txt", "r") as file:
        read_content = file.readlines()
    result = []
    for stroke in read_content:
        stroke = stroke.split(',')
        result.append([int(x) for x in stroke])
    return result

def solve_task(input_list):
    i = 0
    length = len(input_list)
    while i < length - 1:
        max_element = [0, 0]
        for j in range(input_list[i], 0, -1):
            if i + j < length and input_list[i + j] > max_element[0] or i + j == length - 1:
                max_element = [input_list[i + j], i + j]
        if max_element[1] == 0:
            return False
        else:
            i = max_element[1]
    return True

if __name__ == '__main__':
    input_data = read_input_file()
    for input_list in input_data:
        print(f"{input_list} - {solve_task(input_list)}")
