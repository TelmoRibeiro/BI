# assumption: len(nl) > 0
def min_avg_max(nl):
    min = nl[0]
    sum = nl[0]
    max = nl[0]
    for i in range(1, len(nl)):
        if nl[i] < min:
            min = nl[i]
        if nl[i] > max:
            max = nl[i]
        sum += nl[i]
    avg = sum / len(nl)
    return (min, avg, max)

def main():
    nl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(min_avg_max(nl))

main()