#!/bin/bash
export DOCKBASE=`readlink -f /home/soft/ucsfdock/DOCK-3.7b-bela30c/`
for i in aa2ar
do
    cd /home/mxu02/dock37-test/test_dude/${i}/dock37
    ls -d dock > dirlist
    $DOCKBASE/analysis/extract_all.py  --done
    $DOCKBASE/analysis/getposes.py -l number
    $DOCKBASE/analysis/enrich.py --ligand-file=ligand.name -d decoys.name

    cd /home/mxu02/dock37-test/test_dude/${i}/vina/output
    for n in *.pdbqt
    do
        echo -n `basename ${n} .pdbqt` " " >> vina_energy.txt
        sed -n "2p" ${n} | awk -F" " '{print $4}' >> vina_energy.txt
    done
    sort -u /home/mxu02/dock37-test/test_dude/${i}/mol2_active/name > ligand.name
    sort -u /home/mxu02/dock37-test/test_dude/${i}/mol2_decoy/name > decoys.name
    cat ligand.name > ./mol.name
    cat decoys.name >> ./mol.name
    
    cp vina_energy.txt vina.txt
    python3 /home/mxu02/dock37-test/benchmark_script/vina_script/get_best_score.py
    sort -n -k 2 vina_out.txt > vina_uniq.txt
    awk '$1=$1" 1 11178 31140 2.11 12 2 1263 1 1 -0.48 0.00 -11.85 13.87 -0.34 0.00 0.00 0.00 0.00"' vina_uniq.txt > extract_all.sort.uniq.txt
    sed -i "s/^/dock\/ 0000 &/g " extract_all.sort.uniq.txt
    rm vina_list out.txt vina_out.txt vina_uniq.txt vina.txt
    $DOCKBASE/analysis/enrich.py --ligand-file=ligand.name -d decoys.name

    cd /home/mxu02/dock37-test/test_dude/${i}
    python2.7 $DOCKBASE/analysis/plots.py --ligand-file=ligand.name -d decoys.name -i ./dock37 -l DOCK_3.7 -i ./vina/output -l Vina $lengend -t ${i}
echo "**************************${i}**********************************"
done
