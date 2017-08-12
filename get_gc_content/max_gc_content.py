"""This code receives few FASTA files and returns the FASTA file with the highest G-C content, and the
 the calculated %G-C"""

all_fasta_file = open("fasta_all","r")
fasta_file_string = all_fasta_file.read()


class FastaSequence:
    def __init__(self, seq_id, seq):
        self.seq_id = seq_id
        self.seq = seq

    def calculate_gc_percantage(self):
        num_of_gc = self.seq.count("G") + self.seq.count("C")
        return float((num_of_gc / len(self.seq)) * 100)

def break_to_fasta_files(file_of_fasta):
    fasta_sequence_list = []
    list_of_fasta = fasta_file_string.split('>')
    for fasta_seq in list_of_fasta:
        is_fasta_sequence = fasta_seq != ""
        if is_fasta_sequence:
            separated_fasta_seq_list = fasta_seq.split('\n', 1)
            fasta_id = separated_fasta_seq_list[0]
            fasta_seq = separated_fasta_seq_list[1].replace('\n','')
            fasta_sequence = FastaSequence(fasta_id, fasta_seq)
            fasta_sequence_list.append(fasta_sequence)

    return fasta_sequence_list

def max_gc_percentage(list_of_fasta_sequences):
    max_fasta_sequence = None
    for fasta_sequence in list_of_fasta_sequences:
        if max_fasta_sequence is None or \
                (fasta_sequence.calculate_gc_percantage() > max_fasta_sequence.calculate_gc_percantage()):
            max_fasta_sequence = fasta_sequence
    return max_fasta_sequence

fasta_sequences = break_to_fasta_files(fasta_file_string)
fasta_sequence_with_max_gc = max_gc_percentage(fasta_sequences)
print ("The FASTA ID with the highest GC content is: %s" %fasta_sequence_with_max_gc.seq_id,\
       "With GC contect of: %s" %fasta_sequence_with_max_gc.calculate_gc_percantage())


















