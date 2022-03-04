def locate_substring(dna_snippet, dna):
    indices = []
    indices.append(dna.find(dna_snippet))
    for i in range(len(dna)):
        if i > indices[0]:
            indices.append(dna.find(dna_snippet,i))
    unscuffed_indices = []
    for i in indices:
        if i!=-1 and i not in unscuffed_indices:
            unscuffed_indices.append(i)
    return unscuffed_indices