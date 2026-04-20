def total(rice , millet , wheat):
    return rice + millet + wheat

cost = [100,50,200]

cost = {"rice": 100, "millet": 50, "wheat": 200}

print(total(**cost))