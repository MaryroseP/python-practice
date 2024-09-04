import time as t

rows = 2
columns = 3
symbols = '@'

for i in range(rows):
    for j in range(columns):
        print(symbols, end="", flush=True)
        t.sleep(1)
    print()
