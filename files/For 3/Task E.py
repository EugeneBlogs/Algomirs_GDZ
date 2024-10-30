n = int(input())
k = int(input())
n_fact = 1
for i in range(1, n + 1):
    n_fact *= i
k_fact = 1
for i in range(1, k + 1):
    k_fact *= i
raznost = n - k
raznost_fact = 1
for i in range(1, raznost + 1):
    raznost_fact *= i
C = int(n_fact / (k_fact * raznost_fact))
print(C)
