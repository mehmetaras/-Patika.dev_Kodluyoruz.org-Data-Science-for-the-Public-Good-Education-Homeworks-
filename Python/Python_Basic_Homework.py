""" 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]"""

""" 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]] """

#1--
flatten_m=[]
def flatten(l):
    for e in l:
        if type(e) !=list:
            flatten_m.append(e)
        else:
            flatten(e)
    return flatten_m


#2--
reverse_=[]
def reverse(l):
    for e in l:
        if type(e) !=list:
            reverse_.append(e)
        else:
            reverse(e)
    return reverse_[::-1]



