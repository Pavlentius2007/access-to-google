
def minus(a, b):
    return a - b

def summary(a, b):
    return a + b


def main(a, b, param):
    if param == "+":
        return summary(a, b)

result = main(1, 3, '+')
print(result)




