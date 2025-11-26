name = "Danya Varenik"
a = [name.upper()]
b = [name.lower()]
d = [ord(symbol) for symbol in a]
c = [ord(symbol) for symbol in b]
print((sum(d) + sum(c)))