times200 = []
times400 = []
fastest100 = 10000
fastest200 = 10000
fastest400 = 10000
race_selection = int(input("What race would you like. \n"
                           "100m, 200m or 400m: "))
if race_selection == 100:
    times100 = []
    def average(times100):
        return sum(times100) / len(times100)

    time100 = int(input("What was your time: "))
    while time100 != -1:

        times100.append(time100)

        if time100 < fastest100:
            fastest100 = time100
        time100 = int(input("What was your time: "))

    average_times100 = average(times100)
    print(times100)
    print(f"The fastest time was {fastest100}")
    print(f"The average time was {average_times100} seconds. ")
elif race_selection == 200:
        def average(times200):
            return sum(times200) / len(times200)

        time200 = int(input("What was your time: "))
        while time200 != -1:


            times200.append(time200)
            if time200 < fastest200:
                fastest200 = time200
            time200 = int(input("What was your time: "))

        average_times200 = average(times200)
        print(times200)
        print(f"The fastest time was {fastest200}")
        print(f"The average time was {average_times200} seconds. ")
elif race_selection == 400:
    def average(times400):
        return sum(times400) / len(times400)


    time400 = int(input("What was your time: "))
    while time400 != -1:

        times400.append(time400)

        if time400 < fastest400:
            fastest400 = time400
        time400 = int(input("What was your time: "))

    average_times400 = average(times400)
    print(times400)
    print(f"The fastest time was {fastest400}")
    print(f"The average time was {average_times400} seconds. ")
else:
    print("Done")

option = input("Would you like to see the results from any other race?")
if option == "Yes" or "yes":
    recall = int(input("What race would you like to review: "))
    if recall == 100:
        print(times100)
        print(f"The fastest time was {fastest100}")
        print(f"The average time was {average_times100} seconds. ")
    elif recall == 200:
        print(times200)
        print(f"The fastest time was {fastest200}")
        print(f"The average time was {average_times200} seconds. ")
    elif recall == 400:
        print(times400)
        print(f"The fastest time was {fastest400}")
        print(f"The average time was {average_times400} seconds. ")
    else:
        print("Done")

next = input("Would you like continue and enter times for a different race")