
# iterative algorithm to compute v (DP slides)
# study-sleep-beer example

import math

Vs = [0, 0, 0]
Rs = [0, -10, -10]
P = [[0.1, 0.4, 0.5],[0.6, 0.2, 0.2],[0, 0.4, 0.6]]
#P = [[1, 0, 0],[0.6, 0.4, 0],[0, 0.6, 0.4]]
gamma = 0.9

print(f"----- init -----")
print(Vs)
print()

Vss = [0,0,0]
term = False
k = 0
while not term:
    input()
    print(f"----- iteration {k} -----")
    for i in range(len(Vs)):
        fterm = 0
        string_fterm = ""
        for j in range(len(Vs)):
            fterm += P[i][j] * Vs[j]
            string_fterm = string_fterm + f"{P[i][j]} * {Vs[j]} +"
        Vss[i] = Rs[i] + gamma * fterm
        print(f"State {i}: {Rs[i]} + {gamma} * ({string_fterm})")
    print(Vss)

    term = True
    for i in range(len(Vs)):
        if abs(Vss[i] - Vs[i]) > 0.01:
            term = False

    Vs = Vss
    k += 1
    print()
