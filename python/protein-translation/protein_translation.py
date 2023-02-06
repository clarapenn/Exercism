def proteins(strand):
    codons_list = []

    while strand:
        next_triplet = strand[:3]
        if next_triplet in ["UAA", "UAG", "UGA"]:
            break

        codons_list.append(next_triplet)
        strand = strand[3:]

    # now do somethng with codons_list

    proteins_list = []

    for item in codons_list:
        if item == "AUG":
            proteins_list.append("Methionine")
        if item == "UUU":
            proteins_list.append("Phenylalanine")
        if item == "UUC":
            proteins_list.append("Phenylalanine")
        if item == "UUA":
            proteins_list.append("Leucine")
        if item == "UUG":
            proteins_list.append("Leucine")
        if item == "UCU":
            proteins_list.append("Serine")
        if item == "UCC":
            proteins_list.append("Serine")
        if item == "UCA":
            proteins_list.append("Serine")
        if item == "UCG":
            proteins_list.append("Serine")
        if item == "UAU":
            proteins_list.append("Tyrosine")
        if item == "UAC":
            proteins_list.append("Tyrosine")
        if item == "UGU":
            proteins_list.append("Cysteine")
        if item == "UGC":
            proteins_list.append("Cysteine")
        if item == "UGG":
            proteins_list.append("Tryptophan")

    return proteins_list
