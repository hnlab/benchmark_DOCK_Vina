#!/bin/bash
cd /home/mxu02/dock37-test/test_dude/nram/vina/output

for j in `awk -F" " '{print $1}' uniq_name_energy.csv`
do
    babel ${j} test.sdf
    cat test.sdf >> /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/nram.sdf
    echo ${j}
done
# for j in `ls ZINC*.pdbqt`
# do
#     babel ${j} test.sdf
#     cat test.sdf >> nram.sdf
#     echo ${j}
# done
/home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/torsionchecker --license AAAAAAAliPQAAAAU0WVcW4zmBK/zhUqEZf+g8NeQaPg= \
-m /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/nram.sdf -t /home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/lib/TorLibv21WCSDBins.xml \
-r /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/nram_out.csv
echo "****************************nram***********************************"
