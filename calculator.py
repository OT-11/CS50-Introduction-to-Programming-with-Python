#calculator.py
def main():
    x = float(input("What's x? "))
    print("x squared is", square (x))

def square(n):
    return n ** 2
y = float(input ("What's y? "))

z = round(x / y, 2)

print(f"{z:,}")
