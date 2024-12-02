def read_file(file_name: str) -> list[list[int]]:
    with open(file_name, 'r') as file:
        return [list(map(int, line.split())) for line in file.readlines()]

def calculate_difference(l1: list[int], l2: list[int]) -> int:
    ans = 0
    for i, j in zip(l1, l2):
        ans += abs(i - j)
    return ans

def main() -> None:
    input_data = read_file("input.txt")
    l1 = []
    l2 = []
    for line in input_data:
        num1, num2 = line
        l1.append(num1)
        l2.append(num2)
    l1.sort()
    l2.sort()
    result = calculate_difference(l1, l2)
    print(result)

if __name__ == "__main__":
    main()
