#!/bin/bash
export MGLPATH="/home/mxu02/soft/mgltools_x86_64Linux2_1.5.6/InstDir"
# for i in `awk -F"\t" '{print $2}' du.txt | sed -n '93,102p'`
for i in aa2ar
do
cd /home/mxu02/dock37-test/test_dude/${i}
mkdir vina dock37
cd vina
scp x036:/home/xumin/data/dude/${i}/DOCK3.7/working/rec.crg.pdb x036:/home/xumin/data/dude/${i}/DOCK3.7/working/xtal-lig.pdb .
scp -r x036:/home/xumin/data/dude/${i}/DOCK3.7/dockfiles x036:/home/xumin/data/dude/${i}/DOCK3.7/INDOCK /home/mxu02/dock37-test/test_dude/${i}/dock37
    for file in rec.crg.pdb
    do
    echo "$file to pdbqt begining"
    $MGLPATH/bin/pythonsh $MGLPATH/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py -r $file -o `basename $file .pdb`.pdbqt -A checkhydrogens
    echo "$file to pdbqt done"
    echo "\n"
    done
    echo "preparing of receptor done"
    for file in xtal-lig.pdb
    do
    echo "$file to pdbqt begining"
    $MGLPATH/bin/pythonsh $MGLPATH/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -l $file -o `basename $file .pdb`.pdbqt
    echo "$file to pdbqt done"
    echo "\n"
    done
    echo "preparing of  all  ligands done"

    $MGLPATH/bin/pythonsh $MGLPATH/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_gpf4.py -l xtal-lig.pdbqt -r rec.crg.pdbqt -p npts='86,86,86' -p ligand_types='A,SA,P,N,Cl,F,I,Br,C,HD,H,OA,NA,S' -y -o box.gpf 

    echo "receptor = rec.crg.pdbqt" > conf.txt
    echo >> conf.txt
    echo "center_x = `grep gridcenter box.gpf | awk '{print $2}'`" >> conf.txt
    echo "center_y = `grep gridcenter box.gpf | awk '{print $3}'`" >> conf.txt
    echo "center_z = `grep gridcenter box.gpf | awk '{print $4}'`" >> conf.txt
    python /home/mxu02/dock37-test/benchmark_script/vina_script/cal_box.py
done
