class H:
    s = 'class H'


class G(H):
    s = 'G'


class F(H):
    s = 'F'


class D(H):
    s = 'D'


class E(H):
    s = 'E'


class B(D, E):
    s = 'B'


class C(F, G):
    s = 'C'


class A(B, C):
    s = 'A'


print(A.__mro__)