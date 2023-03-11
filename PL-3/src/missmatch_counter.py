def hamming_distance(S, P):
    missmatch_counter = 0
    for i in range(0, len(P)):
        if P[i] != S[i]:
            missmatch_counter += 1
    return missmatch_counter

def main():
    S = "ATCCA"
    P = "CTCCC"
    missmatch_counter = hamming_distance(S, P)
    print(missmatch_counter)

main()