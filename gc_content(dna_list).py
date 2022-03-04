def gc_content(dna_list):
    gc_dict = {}
    for i in range(len(dna_list)):
        gc_dict[i] = dna_list[i].count('G') + dna_list[i].count('C')
    return (max(gc_dict, key=gc_dict.get),((max(gc_dict.values()))/(len(dna_list[max(gc_dict, key=gc_dict.get)])))*100)
    
    