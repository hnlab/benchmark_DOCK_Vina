#! /bin/bash
source ~/.bashrc
for f in `ls /home/mxu02/dock37-test/test_dude/aa2ar/pdbqt_active/*.mol2.pdbqt | cat`; do
    b=`basename $f .mol2.pdbqt`
    echo Processing ${f}
    /home/mxu02/soft/Vina/vina_mxu --cpu 8 --config conf.txt --receptor rec.crg.pdbqt --num_modes 1 --ligand $f --out output/${b}.pdbqt
done
cd /home/mxu02/dock37-test/test_dude/aa2ar/pdbqt_decoy/
find -type f -name '*.pdbqt' > input.name
for f in `cat input.name`; do
    b=`basename $f .mol2.pdbqt`
    echo Processing ${f}
    /home/mxu02/soft/Vina/vina_mxu --cpu 8 --config /home/mxu02/dock37-test/test_dude/aa2ar/vina/conf.txt --receptor /home/mxu02/dock37-test/test_dude/aa2ar/vina/rec.crg.pdbqt --num_modes 1 --ligand $f --out /home/mxu02/dock37-test/test_dude/aa2ar/vina/output/${b}.pdbqt
done
