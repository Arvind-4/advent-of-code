def abs_value(a: int) -> int:
    return abs(a)

def all_decreasing(input_list: list[int]) -> bool:
    for i in range(1, len(input_list)):
        if input_list[i] > input_list[i - 1]:
            return False
    return True

def all_increasing(input_list: list[int]) -> bool:
    for i in range(1, len(input_list)):
        if input_list[i] < input_list[i - 1]:
            return False
    return True

def max_diff(input_list: list[int], max_diff_value: int) -> bool:
    for i in range(1, len(input_list)):
        if abs_value(input_list[i] - input_list[i - 1]) > max_diff_value:
            return False
    return True

def min_diff(input_list: list[int], min_diff_value: int) -> bool:
    for i in range(1, len(input_list)):
        if abs_value(input_list[i] - input_list[i - 1]) < min_diff_value:
            return False
    return True

def read_file(file_name: str) -> list[list[int]]:
    with open(file_name, 'r') as file:
        return [list(map(int, line.split())) for line in file.readlines()]


def validate(data: list[int]) -> bool:
    desc = all_decreasing(data)
    incr = all_increasing(data)
    max_ = max_diff(data, 3)
    min_ = min_diff(data, 1)
    return (desc or incr) and max_ and min_

def main() -> None:
    input_data = read_file("input.txt")
    count = 0
    for data in input_data:
        if validate(data):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
