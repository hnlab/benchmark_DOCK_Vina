#!/bin/bash

for i in fa10 mapk2 fkb1a def comt andr
do
    grep -E "  none.*R" /home/mxu02/dock37-test/test_dude/script/torsion/dock/${i}_out.csv |awk -F"\t" '{print $3" "$NF}' >> ${i}_red.csv
    echo ${i}
done
