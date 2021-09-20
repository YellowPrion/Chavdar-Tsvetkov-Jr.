from collections import deque
first_numbers = set(int(x) for x in input().split())
second_numbers = set(int(x) for x in input().split())
n = int(input())
for _ in range(n):
    string = deque(input().split())
    if string[0] == "Add":
        if string[1] == "First":
            string.popleft()
            string.popleft()
            for ele in string:
                first_numbers.add(int(ele))
        else:
            string.popleft()
            string.popleft()
            for ele in string:
                second_numbers.add(int(ele))
    elif string[0] == "Remove":
        if string[1] == "First":
            string.popleft()
            string.popleft()
            for b in string:
                if int(b) in first_numbers:
                    first_numbers.remove(int(b))
        else:
            string.popleft()
            string.popleft()
            for b in string:
                if int(b) in second_numbers:
                    second_numbers.remove(int(b))
    else:
        if first_numbers.issubset(second_numbers) or second_numbers.issubset(first_numbers):
            print("True")
        else:
            print("False")
first_sorted = sorted(first_numbers)
second_numbers = sorted(second_numbers)
print(', '.join(str(x) for x in first_sorted))
print(', '.join(str(x) for x in second_numbers))
