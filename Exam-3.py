from collections import deque

def flights(*destinations):
    my_dict = {}
    counter = 0
    parameters = deque([x for x in destinations])
    while parameters:
        ele = parameters[0]
        place = parameters.index(ele)
        if ele == "Finish":
            break
        if counter % 2 == 0:
            if ele in my_dict:
                my_dict[ele] += int(parameters[place + 1])
            else:
                my_dict[ele] = int(parameters[place + 1])
        parameters.popleft()
        counter += 1
    return my_dict

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
