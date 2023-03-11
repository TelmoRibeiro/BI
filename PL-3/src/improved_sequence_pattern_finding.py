def hamming_distance(S, P):
    missmatch_counter = 0
    for i in range(0, len(P)):
        if P[i] != S[i]:
            missmatch_counter += 1
    return missmatch_counter

def search_all_occurrences_mismatch(S, P, m):
    index_list = []
    found = False
    i = 0
    while i <= len(S)-len(P):
        if not found:
            subS = S[i:i+len(P)]
            missmatch_counter = hamming_distance(subS, P)
            if missmatch_counter <= m:
                found = True
        if found:
            index_list.append(i)
            found = False
        i = i + 1
    return index_list

def main():
    S = "ATATCAGATAT"
    P = "AT"
    index_list = search_all_occurrences_mismatch(S, P, 1)
    print(index_list)

main()