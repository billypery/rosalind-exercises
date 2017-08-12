"""This code receives 2 DNA strands equal in size, and returns the number of point mutations, i.e.,
the Hamming distance"""

dna_strands = open("dna_strands","r")
dna_strands = dna_strands.readlines()


def count_point_mutations(dna_seq):
    first_strand = dna_seq[0].replace("\n","")
    second_strand = dna_seq[1].replace("\n", "")
    count = 0
    for i in range(len(first_strand)):
        if first_strand[i] != second_strand[i]:
            count += 1
    return count

print ("The Hamming distance is %s" %count_point_mutations(dna_strands))
