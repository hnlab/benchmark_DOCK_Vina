#!/usr/bin/env python
import collections
frequency = collections.defaultdict(int)
smile_list = []
f = open('all_red.csv', 'r')
# f = open('test.csv', 'r')
for line in f:
    smile = line.split()[0]
    smile_list.append(smile)
for word in smile_list:
    frequency[word] += 1
final_dic = sorted(frequency.items(), key = lambda kv:(kv[1], kv[0]))
output = open('smiles_type.csv','w')
# for k,v in frequency.items():
for k,v in final_dic:
    output.write("{}\t{}\n".format(k, v))
f.close()
output.close()
