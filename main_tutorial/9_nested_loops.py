# nested loops =    The "inner loop" will finish all of its iterations before finishing one iteration of the outer loop

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbols = input("What symbol? ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()




