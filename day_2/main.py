def store_list(list1: list):
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            numbers = list(map(int, line.strip().split()))
            if is_increasing_or_decreasing(numbers) and has_valid_difference(numbers): 
                list1.append(line.strip())
            elif is_valid_with_one_removal(numbers):
                list1.append(line.strip())
            
def is_increasing_or_decreasing(numbers: list) -> bool:
    increasing = all(x < y for x, y in zip(numbers, numbers[1:]))
    decreasing = all(x > y for x, y in zip(numbers, numbers[1:]))
    return increasing or decreasing

def has_valid_difference(numbers: list) -> bool:
    return all(1 <= abs(x - y) <= 3 for x, y in zip(numbers, numbers[1:]))

def is_valid_with_one_removal(numbers: list) -> bool:
    for i in range(len(numbers)):
        new_numbers = numbers[:i] + numbers[i+1:]
        if is_increasing_or_decreasing(new_numbers) and has_valid_difference(new_numbers):
            return True
        
    return False

def main():
    list1 = []
    store_list(list1)
    print(len(list1))
    
if __name__ == "__main__":
    main()