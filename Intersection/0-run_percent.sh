#!/bin/bash
for i in `awk -F"\t" '{print $2}' du.txt`
do
    python 0-ligand_rank_percent5.py ${i}
    echo "**************************${i}***************************"
done
