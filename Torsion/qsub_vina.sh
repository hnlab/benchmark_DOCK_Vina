#!/bin/bash
cd /home/mxu02/dock37-test/test_dude/nram/vina/output
python /home/mxu02/dock37-test/test_dude/script/torsion/2-extract_vina_pose.py
for name in `awk -F"," '{print $1}' out_lig.csv`
do
    energy=`grep ${name} out_lig.csv | awk -F"," '{print $NF}'`
    for mol in ${name}_*_final_*.pdbqt
    do
        mol_energy=`grep "REMARK VINA RESULT: " ${mol} | awk -F" " '{print $4}'`
        if [ ${energy}x = ${mol_energy}x ]; then
        # cat ${mol} >> unique.pdbqt
        babel ${mol} test.sdf
        cat test.sdf >> /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/nram.sdf
        echo ${mol}
        fi
    done
done

# for j in `ls CHEMBL*.pdbqt`
# do
#     babel ${j} test.sdf
#     cat test.sdf >> nram.sdf
#     echo ${j}
# done
# for j in `ls ZINC*.pdbqt`
# do
#     babel ${j} test.sdf
#     cat test.sdf >> nram.sdf
#     echo ${j}
# done
/home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/torsionchecker --license AAAAAAAliPQAAAAU0WVcW4zmBK/zhUqEZf+g8NeQaPg= \
-m /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/nram.sdf \
-t /home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/lib/TorLibv21WCSDBins.xml \
-r /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/nram_out.csv
echo "****************************nram***********************************"
