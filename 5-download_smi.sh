#!/bin/bash
for i in aa2ar
do
cd /home/mxu02/dock37-test/test_dude/${i}/dock37/ligand
# rm *.db2.gz
wget http://dude.docking.org/targets/${i}/actives_final.ism http://dude.docking.org/targets/${i}/decoys_final.ism
echo ${i}
done
