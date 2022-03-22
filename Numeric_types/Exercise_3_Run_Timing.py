def run_timing():
    sum = 0
    iteration = 0
    while True:
        answer = input("Enter 10 km run time:")
        if not answer:
            print("Average of {}, over {} runs".format((sum / iteration), iteration))
            break
        iteration += 1
        sum += int(answer)


run_timing()
