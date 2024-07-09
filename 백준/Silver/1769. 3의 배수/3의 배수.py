def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def main():
    X = input().strip()
    count = 0
    while len(X) > 1:
        X = str(sum_of_digits(X))
        count += 1
    
    print(count)
    if int(X) % 3 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()