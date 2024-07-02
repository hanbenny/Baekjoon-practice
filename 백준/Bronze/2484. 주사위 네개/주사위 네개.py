def calculate_prize(dice):
    counts = [0] * 7  # 주사위 눈의 개수를 셀 리스트 (1~6 사용)
    
    for d in dice:
        counts[d] += 1
    
    if 4 in counts:
        eye = counts.index(4)
        return 50000 + eye * 5000
    
    if 3 in counts:
        eye = counts.index(3)
        return 10000 + eye * 1000
    
    if counts.count(2) == 2:
        eyes = [i for i in range(1, 7) if counts[i] == 2]
        return 2000 + eyes[0] * 500 + eyes[1] * 500
    
    if 2 in counts:
        eye = counts.index(2)
        return 1000 + eye * 100
    
    return max(dice) * 100

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    max_prize = 0
    
    for i in range(N):
        dice = list(map(int, data[4*i + 1 : 4*i + 5]))
        prize = calculate_prize(dice)
        if prize > max_prize:
            max_prize = prize
    
    print(max_prize)

if __name__ == "__main__":
    main()
