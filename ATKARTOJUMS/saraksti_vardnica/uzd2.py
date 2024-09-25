'''edieni= ['abols','cepums','cipsi']
print(edieni)

print(edieni[1])  #otrais elemetns pēc kārtas

print(edieni[::-1]) #apgreiezta secība

#izveidto sarakstu ar for ciklu, lai elementi būt ar pirmo lielo burtu
lielie_burti=[]
for ediens in edieni:
    lielie_burti.append(ediens.capitalize())
print(lielie_burti)'''

burti = ['A','B','C','D','E','F','G','H']
print(len(burti))



#pēdejo saraksat elementu
print(burti[-1])


#konkrēti elemti no sarksat
konkreti = burti[3:6]
print(konkreti)