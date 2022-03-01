#!/usr/bin/env python
# coding: utf-8

# In[12]:


def mendels_law(hom, het, rec):
    total = hom+het+rec
    combinations = 0
    for i in range(total):
        combinations += i
    weight_hom = 0
    for i in range(hom):
        weight_hom += total-(i+1)
    weight_het = 0
    for i in range(1,het):
        weight_het += .75*i
    weight_het += .5*(het*rec)
    probability = (weight_hom + weight_het)/combinations
    return probability

