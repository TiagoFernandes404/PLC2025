import re

# Expressão regular para strings binárias sem "011"
pattern = re.compile(r'^(?:0|1|01(0))*1?$')

# Exemplos de strings para testar
validos = ["", "0", "1", "010", "1001", "1111", "0100"]
invalidos = ["011", "1011", "00011"]

print("Testando strings VÁLIDAS:")
for s in validos:
    print(f"{s!r} ->", bool(pattern.fullmatch(s)))

print("\nTestando strings INVÁLIDAS:")
for s in invalidos:
    print(f"{s!r} ->", bool(pattern.fullmatch(s)))
