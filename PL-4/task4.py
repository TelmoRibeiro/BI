import re
import sys

def read_fasta(file_name):
    with open(file_name, 'r') as fn:
        fasta_data = fn.read()
    fn.close()
    return fasta_data

def get_identifiers(fasta_data):
    identifiers = []
    sequence_match = re.search(">[^>]*", fasta_data)
    while sequence_match:
        match_span  = sequence_match.span()
        sequence    = fasta_data[match_span[0]:match_span[1]]
        fasta_data  = fasta_data[match_span[1]:]
        match_span  = re.search(" ", sequence).span()
        identifiers.append(sequence[1:match_span[0]])
        sequence_match = re.search(">[^>]*", fasta_data)
    return identifiers

def get_species_frequency(fasta_data):
    species_dictionary = {}
    sequence_match = re.search(">[^>]*", fasta_data)
    while sequence_match:
        match_span = sequence_match.span()
        sequence   = fasta_data[match_span[0]:match_span[1]]
        fasta_data = fasta_data[match_span[1]:]
        match_span = re.search("OS=[^OX=]*OX=", sequence).span()
        species    = sequence[match_span[0]+3:match_span[1]-3]
        # print(species) # testing
        if    species in species_dictionary: species_dictionary[species] += 1
        else:                                species_dictionary[species]  = 1
        sequence_match = re.search(">[^>]*", fasta_data)
    return species_dictionary

def get_header_dictionary(fasta_data):
    header_dictionary = {}
    sequence_match = re.search(">[^>]*", fasta_data)
    while sequence_match:
        match_span = sequence_match.span()
        sequence   = fasta_data[match_span[0]:match_span[1]]
        fasta_data = fasta_data[match_span[1]:]
        match_span = re.search(" ", sequence).span()
        ID         = sequence[1:match_span[0]]
        # print(ID) # testing
        match_span = re.search("OS=[^OX=]*OX=", sequence).span()  
        OS         = sequence[match_span[0]+3:match_span[1]-3]
        # print(OS) # testing
        match_span = re.search("OX=[^ ]* ", sequence).span()
        OX         = sequence[match_span[0]+3:match_span[1]-1]
        # print(OX) # testing
        match_span = re.search("GN=[^ ]* ", sequence).span()
        GN         = sequence[match_span[0]+3:match_span[1]-1]
        # print(GN) # testing
        match_span = re.search("PE=[^ ]* ", sequence).span()
        PE         = sequence[match_span[0]+3:match_span[1]-1]
        # print(PE)
        match_span = re.search("SV=[^\n]*\n", sequence).span()
        SV         = sequence[match_span[0]+3:match_span[1]-1]
        # print(SV)
        header_dictionary[ID] = (OS, OX, GN, PE, SV)
        sequence_match = re.search(">[^>]*", fasta_data)
    return header_dictionary

def main():
    file_name   = sys.argv[1]
    fasta_data  = read_fasta(file_name)
    # print(fasta_data) # testing
    print(f"1)\n{get_identifiers(fasta_data)}\n")
    print("2)")
    species_dictionary = get_species_frequency(fasta_data)
    for species in species_dictionary:
        print(f"{species}: {species_dictionary[species]}")
    print("\n3)")
    header_dictionary = get_header_dictionary(fasta_data)
    for identifier in header_dictionary:
        print(f"{identifier}: {header_dictionary[identifier]}")
    return
main()  