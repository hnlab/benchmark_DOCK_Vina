#!/bin/bash
export DOCKBASE=`readlink -f /home/soft/ucsfdock/DOCK-3.7b-bela30c/`
for i in andr
do
    cd /home/mxu02/dock37-test/test_dude/${i}/dock_vdw_all_reduced
    ls -d dock > dirlist
    $DOCKBASE/analysis/extract_all.py  --done
    # $DOCKBASE/analysis/getposes.py -l number
    awk -F" " '{print $3}' /home/mxu02/dock37-test/test_dude/${i}/dock37/ligand/actives_final.ism | sort -u > ligand.name
    awk -F" " '{print $2}' /home/mxu02/dock37-test/test_dude/${i}/dock37/ligand/decoys_final.ism | sort -u > decoys.name

    $DOCKBASE/analysis/enrich.py --ligand-file=ligand.name -d decoys.name

    cd /home/mxu02/dock37-test/test_dude/${i}
    python2.7 $DOCKBASE/analysis/plots.py --ligand-file=ligand.name -d decoys.name -i ./dock37 -l DOCK_3.7 -i ./vina/output -l Vina -i ./dock_vdw_all_reduced -l DOCK3.7_vdw_all_reduced $lengend -t ${i}_vdw
echo "**************************${i}**********************************"
done
