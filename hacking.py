time = 0
times = []
fastest = 10000

def average(times):
    return sum(times) / len(times)

while time != -1:
    time = int(input("What was your time: "))
    times.append(time)

    if time < fastest:
        fastest = time


average_times = average(times)
print(times)
print(f"The fastest time was {fastest}")
print(f"The average time was {average_times} seconds. ")