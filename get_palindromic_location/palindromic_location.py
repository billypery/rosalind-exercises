"""This code receives a txt file of FASTA sequence and returns the locations of the palindromic sequences
 and their length (from 4-12)"""

fasta_file = open("fasta_file.txt","r")
fasta_file = fasta_file.readlines()

def get_forward_seq(fasta_seq):
    forward_seq = []
    for line in fasta_seq:
        if line[0] != ">":
            line = line.replace("\n","")
            forward_seq.append(line)

    forward_seq = ''.join(forward_seq)
    return forward_seq

def get_reverse_seq(forward):
    complementary_nucleotide_dict = {"A":"T","T":"A","G":"C","C":"G"}
    reverse_seq = ""
    for nuct in forward:
        if nuct in complementary_nucleotide_dict:
            reverse_seq += complementary_nucleotide_dict[nuct]

    return reverse_seq

def get_palindromic_seq(forward,reverse):
    palindromic_seq_len = range(4,13)
    palindromic_location_dict = {}
    for length in palindromic_seq_len:
        for i in range(len(forward)-(length-1)):
            forward_sub_seq = forward[i:i+length]
            reverse_sub_seq = reverse[i:i+length]
            reversed_reverse = reverse_sub_seq[::-1]
            if forward_sub_seq == reversed_reverse:
                palindromic_location_dict[i+1] = length
    return palindromic_location_dict

forward_seq = get_forward_seq(fasta_file)
reverse_seq = get_reverse_seq(forward_seq)
my_dict = get_palindromic_seq(forward_seq,reverse_seq)
for k, v in sorted(my_dict.items()):
    print("Palindromic location: %s " %k,"Length: %s" %v)



