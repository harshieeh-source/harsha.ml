import pandas as pd
import numpy as np

# Load the training data
data = pd.read_csv('lab1.csv')
concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

def candidate_elimination(concepts, target):
    s = concepts[0].copy()
    g = [["?" for _ in range(len(s))] for _ in range(len(s))]

    print("Initialization of specific h and general h")
    print(s)
    print(g)

    for i, h in enumerate(concepts):
        if target[i].lower() == "yes":
            for j in range(len(s)):
                if s[j] != h[j]:
                    s[j] = '?'
                    g[j][j] = '?'
        else:
            for j in range(len(s)):
                if s[j] != h[j]:
                    g[j][j] = s[j]
                else:
                    g[j][j] = '?'

        print(f"\nSteps of Candidate Elimination Algorithm {i+1}")
        print(s)
        print(g)

    # Remove overly general hypotheses
    g = [gh for gh in g if gh != ["?"] * len(s)]

    print("\nFinal Specific h:")
    print(s)
    print("\nFinal General h:")
    print(g)

    return s, g

s_final, g_final = candidate_elimination(concepts, target)

