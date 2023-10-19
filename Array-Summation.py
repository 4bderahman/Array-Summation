N = int(input("Enter the size of the arrays T1 and T2: "))
T = []
T1 = []
T2 = []

print("Enter values for array T1:")
for i in range(N):
    value = int(input(f"Enter value {i+1}: "))
    T1.append(value)

print("Enter values for array T2:")
for i in range(N):
    value = int(input(f"Enter value {i+1}: "))
    T2.append(value)

for i in range(N):
    T.append(T1[i] + T2[i])

print(T)
