#!/bin/bash

for i in `cat ../../dude_list`
do
    grep -E ".pdbqt	B.*R" /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/${i}_out.csv |awk -F"\t" '{print $3" "$NF}' >> all_red.csv
    echo ${i}
done
