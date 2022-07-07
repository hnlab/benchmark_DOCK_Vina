#!/bin/bash
for i in aa2ar
do
    mkdir /home/mxu02/dock37-test/test_dude/${i}/dock37 /home/mxu02/dock37-test/test_dude/${i}/vina
    test -d /home/mxu02/dock37-test/test_dude/${i}/dock37/ligand || mkdir /home/mxu02/dock37-test/test_dude/${i}/dock37/ligand
    cd /home/mxu02/dock37-test/test_dude/${i}/dock37
    scp mxu@z55:/pubhome/ftp/dataset/dude/decoys-${i}/*.gz z55:/pubhome/ftp/dataset/dude/ligands-${i}/*.gz ./ligand
    mkdir dock
    scp -r x036:/home/xumin/data/dude/${i}/DOCK3.7/dockfiles .
    cd dock
    scp x036:/home/xumin/data/dude/${i}/DOCK3.7/INDOCK .
    sed -i "/^mol2_score_maximum/d" INDOCK
    sed -i "s/atom_maximum                  25/atom_maximum                  100/g" INDOCK
    cp /home/mxu02/dock37-test/benchmark_script/dock_script/dock_akt1.sge ./dock_${i}.sge
    readlink -f /home/mxu02/dock37-test/test_dude/${i}/dock37/ligand/*.db2.gz > split_database_index
    qsub dock_${i}.sge
    echo ${i}
done
