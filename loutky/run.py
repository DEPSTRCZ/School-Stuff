many = int(input("Enter how many [INT]\n"))
maxweight = int(input("Enter max weight [INT]\n"))
weights = []
for x in range(many):
    weights.append(int(input("Enter weight puppet [INT]\n")))

total = sum(weights)
result = round((total/maxweight))
print(f"You will need: {result}")