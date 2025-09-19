import re

pattern = re.compile(r'^(?!.*011)[01]*$')

tests = ["", "0", "1", "010", "1001", "1111", "0100", "011", "1011", "00011"]
for s in tests:
    print(s, bool(pattern.fullmatch(s)))
