import re

def read_fasta(file_name):
    with open(file_name, 'r') as fn:
        fn.readline()   # dump 1st line
        S = fn.read()   # extract sequence
    return S

def proto(S, start, end):
    S = S[:start].lower() + S[start:end].upper() + S[end+1:].lower()
    return S

def find_prosite(S, profile):
    regexp = profile.replace("-","")
    regexp = regexp.replace("x",".")
    regexp = regexp.replace("(","{")
    regexp = regexp.replace(")","}")
    match = re.search(regexp, S)
    tuple = match.span()
    print(proto(S, tuple[0], tuple[1]))

def main():
    file_name = "Q8RXD4.fasta.txt"
    S = read_fasta(file_name)
    profile = "C-x-H-x-[LIVMFY]-C-x(2)-C-[LIVMYA]"
    find_prosite(S, profile)

main()
    