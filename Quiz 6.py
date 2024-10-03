initial = int(input("what is the initial number of zombies?: "))
day = int(input("how many humans does one zombie affect per day?: "))
days = int(input("how many days has it been since Mr. Chatard was infected: "))
rate = (day + 1)

day1 = 1

for zombies in range(days):
    final = rate * initial
    print("day", day1,":", final)
    initial = final
    day1 = day1 + 1