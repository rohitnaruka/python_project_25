score = 0

print("Quiz Start")

ans = input("Q1: Capital of India? ")
if ans.lower() == "delhi":
    score += 1

ans = input("Q2: 5 + 5 = ? ")
if ans == "10":
    score += 1

ans = input("Q3: Python is a snake or language? ")
if ans.lower() == "language":
    score += 1

print("\nScore:", score, "/ 3")
