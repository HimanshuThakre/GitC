class A:
    varA = "I am class A variable"

class B:
    varB = "I am class B variable"
class C(A,B):
    varc = "I am class C variable"

c1 =C()
print(c1.varA)
print(c1.varB)
print(c1.varc)