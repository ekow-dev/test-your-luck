import random
luck = 1
number = 0
hluck = 0
while True:
    if luck > hluck:
        hluck = luck
        print("your best luck is: 1/", hluck)
    luck = 1
    number = 1
    while number == 1:
        number = random.randrange(1, 3)
        if number == 1:
            luck = luck * 2
