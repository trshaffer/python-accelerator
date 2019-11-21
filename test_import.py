#! /usr/bin/env python3
dependencies = []
source = open("import_normal.py", "r")
for line in source.readlines():
    line = line.rstrip()
    if line == "":
        continue
    words = line.split()
    if words[0][0] == '#':
        continue
    if words[0] != "from" and words[0] != "import":
        break
    print(line)
    dependencies.append(line)
d = "import sympy as asdf"
exec(d)
print(asdf.Rational(3,4))
print(dependencies)
