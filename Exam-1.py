from collections import deque
sold = 0
pizzas_in_order = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
pizza = 0
while pizzas_in_order and employees:
    pizza = pizzas_in_order[0]
    first_pizza = pizza
    if pizza <= 0:
        pizzas_in_order.popleft()
        continue
    if pizza > 10:
        pizzas_in_order.popleft()
        continue
    if pizza == 10:
        while employees:
            pizza -= employees[-1]
            employees.pop()
            if pizza <= 0:
                pizzas_in_order.popleft()
                sold += first_pizza
                break
        continue
    if pizza <= employees[-1]:
        pizzas_in_order.popleft()
        employees.pop()
    elif pizza > employees[-1]:
        pizza -= employees[-1]
        employees.pop()
        while employees:
            pizza -= employees[-1]
            employees.pop()
            if pizza <= 0:
                pizzas_in_order.popleft()
                break
    else:
        pizzas_in_order.remove(pizza)
        employees.pop()
    sold += first_pizza
else:
    if pizza > 0:
        pizzas_in_order.popleft()
        pizzas_in_order.insert(0, pizza)
if len(pizzas_in_order) > 0:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizzas_in_order)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {sold}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
