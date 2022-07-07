#!/bin/bash
# for i in `sed -n '19,87p' dude_list`
# for i in `sed -n '11,12p' dude_list`
# for i in `sed -n '13,101p' dude_list`
for i in adrb1 adrb2 cxcr4 drd3 abl1 akt1 akt2 braf cdk2
do
    cd /home/mxu02/dock37-test/test_dude/script/torsion
    sed "s/nram/${i}/g" qsub_vina.sh > /home/mxu02/dock37-test/test_dude/script/torsion/script/${i}.sh
    sed "s/sge-logs/${i}.log/g;s/qsub_vina.sh/${i}.sh/g" vina_torsion.sge > /home/mxu02/dock37-test/test_dude/script/torsion/script/${i}.sge
    cd /home/mxu02/dock37-test/test_dude/script/torsion/script
    qsub ${i}.sge
    echo ${i}
done
