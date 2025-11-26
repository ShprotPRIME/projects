symbols = 'Python'
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes)  # список

# генераторные выражения - genexp - на выходе получаем
# объект-генератор (вычисляет значения по порядку):
symbols = 'Snake'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes)  # объект-генератор

for object in symbol_codes:
    print(object)