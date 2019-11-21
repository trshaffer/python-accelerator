#! /usr/bin/env python3


#exec("import sympy \nimport sys \nimport os")
import sys, os
exec("from sympy import Rational")
print(Rational(4,5))
print(os.getpid())
