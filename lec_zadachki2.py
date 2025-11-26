name = "Danya Varenik"
s = "_".join(name).upper()
print(s)
a = [ord(i) for i in s]
print(a)

w = "_".join(name).lower()
print(w)
b = [ord(i) for i in w]
print(b)

print(min(min(a), min(b)))
print(max(max(a), max(b)))

