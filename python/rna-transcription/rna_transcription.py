def to_rna(dna_strand):

    dna_strand = list(dna_strand)

    for i in range(len(dna_strand)):
        if dna_strand[i] == "G":
            dna_strand[i] = "C"
        elif dna_strand[i] == "C":
            dna_strand[i] = "G"
        elif dna_strand[i] == "T":
            dna_strand[i] = "A"
        elif dna_strand[i] == "A":
            dna_strand[i] = "U"

    return "".join(dna_strand)
