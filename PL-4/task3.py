import re
import sys

def read_fasta(file_name):
    with open(file_name, 'r') as fn:
        fasta_data = fn.read()   # extract sequences
    fn.close()
    return fasta_data

def find_prosite(S, profile):
    regexp = profile.replace("-","")
    regexp = regexp.replace("x",".")
    regexp = regexp.replace("(","{")
    regexp = regexp.replace(")","}")
    match = re.search(regexp, S)
    return match != None

def process_sequences(fasta_data):
    sequence_match = re.search(">[^>]*", fasta_data)
    while sequence_match:
        sequence_span = sequence_match.span()
        sequence      = fasta_data[sequence_span[0]:sequence_span[1]]
        id_span       = re.search(" ", sequence).span()
        print(sequence[1:id_span[0]], end = " ")
        if   find_prosite(sequence, "N-x-G-x-R-[LIVM]-D-[LIVMFYH]-x-[LV]-x-S"):
            print("MATCH")
        else:
            print("NOT_MATCH")
        fasta_data     = fasta_data[sequence_span[0]:]
        sequence_match = re.search(">[^>]*", fasta_data)

def main():
    file_name  = sys.argv[1]
    fasta_data = read_fasta(file_name)
    process_sequences(fasta_data)

main()