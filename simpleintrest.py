def simInt(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = int(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = int(input("Enter time in years: "))

    si = simInt(p, r, t)

    print("Simple Interest =", simInt(p,i,t))