def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)  # Perbaikan pembagi dari konstan 5 ke len(data)

print(rata_rata([80, 90, 70]))
print(rata_rata([100, 80]))
print(rata_rata([]))