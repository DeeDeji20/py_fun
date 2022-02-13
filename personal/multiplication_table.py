import itertools


print("Multiplication Table")
print()

for i in range(1, 13):
    print("    ",i, end="")
print()
print("-"*70)
for j in range(1, 13):
    print(j, "|", end="   ")
    
    for k in range(1, 13):
        print(j*k, end="    ")
    print()
