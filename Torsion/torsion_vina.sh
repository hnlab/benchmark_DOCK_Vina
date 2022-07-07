#!/bin/bash
# for i in aa2ar abl1 adrb1 adrb2 cxcr4 drd3
for i in `sed -n '7,101p' dude_list`
do
    cd /home/mxu02/dock37-test/test_dude/${i}/vina/output

    for j in `ls CHEMBL*.pdbqt`
    do
        babel ${j} test.sdf
        cat test.sdf >> ${i}.sdf
        echo ${j}
    done
    for j in `ls ZINC*.pdbqt`
    do
        babel ${j} test.sdf
        cat test.sdf >> ${i}.sdf
        echo ${j}
    done

    /home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/torsionchecker --license AAAAAAAliPQAAAAU0WVcW4zmBK/zhUqEZf+g8NeQaPg= \
    -m /home/mxu02/dock37-test/test_dude/${i}/vina/output/${i}.sdf -t /home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/lib/TorLibv21WCSDBins.xml -r /home/mxu02/dock37-test/test_dude/script/torsion/vina/${i}_out.csv
    echo "****************************${i}***********************************"
done
