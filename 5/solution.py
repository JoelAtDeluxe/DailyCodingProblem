

# Given
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def f(a, b):
        return a
    return pair(f)


def cdr(pair):
    def f(a, b):
        return b
    return pair(f)


a_pair = cons(3, 4)

print(car(a_pair))

print(cdr(a_pair))
