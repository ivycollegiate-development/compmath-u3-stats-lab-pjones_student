with open("data/u3_donations.txt") as f:
    raw = [line.strip() for line in f if line.strip()]

donations = [float(line) for line in raw if not line.startswith("#")]
print(len(donations), "values")

n = len(donations)
total = sum(donations)
mean = total / n

print(f"n = {n}, total = {total:.2f}")
print(f"mean = {mean:.2f}")

clean = [d for d in donations if d < 5000]
print(f"mean with    outlier: {sum(donations)/len(donations):.2f}")
print(f"mean without outlier: {sum(clean)/len(clean):.2f}")

ordered = sorted(donations)
n = len(ordered)

if n % 2 == 1:
    median = ordered[n // 2]
    print("odd count, middle value:", median)
else:
    lower = ordered[n // 2 - 1]
    upper = ordered[n // 2]
    median = (lower + upper) / 2
    print(f"even count, mean of the two middle: ({lower:.2f} + {upper:.2f}) / 2 = {median:.2f}")

    from collections import Counter

counts = Counter(donations)
top = counts.most_common(3)
print("three most common values:", top)

max_count = top[0][1]
print("highest frequency:", max_count)
print("how many distinct values:", len(counts))