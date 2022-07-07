#!/bin/bash
for i in aa2ar
do
    echo ${i}
    sed "s/aa2ar/${i}/g" analysis_energy.py > analysis_energy_${i}.py
    sed -i "s/ZINC/C/g" /home/mxu02/dock37-test/test_dude/${i}/vina/output/extract_all.sort.uniq.txt
    python analysis_energy_${i}.py
done
