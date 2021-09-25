import math

if __name__ == "__main__":
    x = 4.8

    while x <= 7.9:
        y = ((3*x + 2) ** 2) / (math.sin(x) + 3)
        print(f'when x = {round(x, 2)}, y = {round(y, 2)}')
        x += 0.4
