#!/bin/bash
for i in andr
do
    test -d /home/mxu02/dock37-test/test_dude/${i}/dock_vdw_all_reduced || mkdir /home/mxu02/dock37-test/test_dude/${i}/dock_vdw_all_reduced
    # scp mxu@z55:/pubhome/ftp/dataset/dude/decoys-${i}/*.gz z55:/pubhome/ftp/dataset/dude/ligands-${i}/*.gz ./ligand
    cd /home/mxu02/dock37-test/test_dude/${i}/dock_vdw_all_reduced
    scp -r x036:/home/xumin/data/dude/${i}/dock_vdw_all_reduced/dockfiles .
    scp x036:/home/xumin/data/dude/${i}/dock_vdw_all_reduced/INDOCK .
    mkdir dock
    cd dock
    cp ../INDOCK .
    sed -i "s/mol2_score_maximum            -10.0/mol2_score_maximum            999999/g" INDOCK
    sed -i "s/atom_maximum                  25/atom_maximum                  100/g" INDOCK
    sed -i "s/check_clashes                 yes/check_clashes                 no/g" INDOCK
    sed -i "s/bump_rigid                    10.0/bump_rigid                    100.0/g" INDOCK
    cp /home/mxu02/dock37-test/test_dude/script/dock_akt1.sge ./dock_${i}.sge
    readlink -f /home/mxu02/dock37-test/test_dude/${i}/dock37/ligand/*.db2.gz > split_database_index
    qsub dock_${i}.sge
    echo ${i}
done
