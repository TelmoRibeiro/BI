def search_all_occurrences(S, P):
    index_list = []
    found = False
    i = 0
    while i <= len(S)-len(P):
        if not found:
            j = 0
            while j < len(P) and P[j] == S[i + j]:
                j = j + 1
            if j == len(P): 
                found = True
        if found: 
            index_list.append(i)
            found = False
        i = i + 1
    return index_list

def main():
    S = "ATATCAGATAT"
    P = "AT"
    index_list = search_all_occurrences(S, P)
    print(index_list)

main()