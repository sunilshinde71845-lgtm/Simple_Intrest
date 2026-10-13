import sys

def simInt(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = int(sys.argv[1])
    r = int(sys.argv[2])
    t = int(sys.argv[3])

    si = simInt(p, r, t)

    print("Simple Interest =", simInt(p,r,t))
    print(sys.argv[0])