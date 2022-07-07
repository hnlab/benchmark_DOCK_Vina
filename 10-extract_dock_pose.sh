#!/bin/bash
export DOCKBASE=`readlink -f /home/soft/ucsfdock/DOCK-3.7b-bela30c/`
for i in aa2ar
do
cd /home/mxu02/dock37-test/test_dude/${i}/dock37
number=`cat /home/mxu02/dock37-test/test_dude/${i}/dock37/extract_all.sort.uniq.txt | wc -l`
$DOCKBASE/analysis/getposes.py -l ${number}
scp poses.mol2 dock/ligand.name x036:/home/xumin/data/dude/${i}/DOCK3.7
echo "***************************${i}******************************"
done
