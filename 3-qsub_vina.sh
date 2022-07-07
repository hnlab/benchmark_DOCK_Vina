#!/bin/bash
for i in aa2ar
do
    cd /home/mxu02/dock37-test/test_dude/${i}/vina
    mkdir output
    cp /home/mxu02/dock37-test/benchmark_script/vina_script/vina_aa2ar.sge ./vina_${i}.sge
    cp /home/mxu02/dock37-test/benchmark_script/vina_script/vina.sh .
    sed -i "s/aa2ar/${i}/g" vina.sh
    qsub vina_${i}.sge
done
