#!/bin/bash
# take fgfr1 as an example.
for i in fgfr1
do
    test -d /home/mxu02/dock37-test/test_dude/${i} || mkdir /home/mxu02/dock37-test/test_dude/${i}
    cd /home/mxu02/dock37-test/test_dude/${i}
    mkdir mol2_active pdbqt_active mol2_decoy pdbqt_decoy
    cd /home/mxu02/dock37-test/test_dude/${i}/mol2_active
    cp /home/mxu02/dock37-test/test_dude/dude/all/${i}/actives_final.mol2.gz .
    gunzip -d actives_final.mol2.gz
    echo actives_final | parallel 'csplit -f {}_ -b %06d.mol2 {}.mol2 /@\<TRIPOS\>MOLECULE/ {*}'
    rm *_000000.mol2
    ls actives_final_*.mol2 > list_lig
    cat list_lig | parallel "/home/mxu02/soft/ADFRsuite_x86_64Linux_1.0/myFolder/bin/prepare_ligand \
    -l  `basename {} .mol2` \
    -o /home/mxu02/dock37-test/test_dude/${i}/pdbqt_active/`basename {} .mol2`.pdbqt"
    rm actives_final_*.mol2
    # grep ^CHEMBL actives_final.mol2 > name
    sed -n '/@<TRIPOS>MOLECULE/{n;p;}' actives_final.mol2 > name
    cd /home/mxu02/dock37-test/test_dude/${i}/pdbqt_active
    ls * > li
    paste /home/mxu02/dock37-test/test_dude/${i}/mol2_active/name li -d"," > merge.csv
    for j in `cat li`
    do
    name=$(grep ${j} merge.csv | awk -F"," '{print $1}')
    sed "/ active torsions:/ a\REMARK ${name}_${j}" ${j} > ${name}_${j}
    done
    rm li actives_final_0*.pdbqt
    echo ${i}

    cd /home/mxu02/dock37-test/test_dude/${i}/mol2_decoy
    cp /home/mxu02/dock37-test/test_dude/dude/all/${i}/decoys_final.mol2.gz .
    gunzip -d decoys_final.mol2.gz
    echo decoys_final | parallel 'csplit -f {}_ -b %06d.mol2 {}.mol2 /@\<TRIPOS\>MOLECULE/ {*}'
    rm *_000000.mol2
    ls decoys_final_*.mol2 > list_lig
    cat list_lig | parallel "/home/mxu02/soft/ADFRsuite_x86_64Linux_1.0/myFolder/bin/prepare_ligand \
    -l  `basename {} .mol2` \
    -o /home/mxu02/dock37-test/test_dude/${i}/pdbqt_decoy/`basename {} .mol2`.pdbqt"
    rm decoys_final_*.mol2
    sed -n '/@<TRIPOS>MOLECULE/{n;p;}' decoys_final.mol2 > name
    cd /home/mxu02/dock37-test/test_dude/${i}/pdbqt_decoy
    ls decoys_final_*.pdbqt > li
    paste /home/mxu02/dock37-test/test_dude/${i}/mol2_decoy/name li -d"," > merge.csv
    for j in `cat li`
    do
    name=$(grep ${j} merge.csv | awk -F"," '{print $1}')
    sed "/ active torsions:/ a\REMARK ${name}_${j}" ${j} > ${name}_${j}
    done
    rm li decoys_final*.pdbqt
    echo ${i}
done
