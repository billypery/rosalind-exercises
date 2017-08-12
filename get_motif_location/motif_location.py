"""This code receives 2 sequences - the first is a DNA sequence and the second is a certain DNA motif.
 The code finds whether the motif exists at the DNA sequence and returns it's locations"""

dna_seq = open("dna_seq.txt","r")
dna_seq = dna_seq.readlines()

def get_motif_location(seq):
    original_seq = seq[0].strip()
    motif = seq[1].strip()
    locations_of_motif = []
    current_location_index = 0
    while True:
        next_motif_location = original_seq.find(motif,current_location_index,-1)
        if next_motif_location == -1:
            break
        locations_of_motif.append(next_motif_location)
        current_location_index = next_motif_location +1
    all_locations = map(str,locations_of_motif)
    all_locations=' '.join(all_locations)
    return all_locations

print(get_motif_location(dna_seq))


