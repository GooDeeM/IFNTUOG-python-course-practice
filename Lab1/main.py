import math

if __name__ == "__main__":
    x = 5
    u = math.log(math.fabs(1-x)) + (math.tan(x) - (math.sin(x)**2)) / (1 - math.sqrt(math.log(x)))

    print(u)
