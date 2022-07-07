#!/bin/bash
for i in `awk -F"," '{print $2}' dude_target_classification.csv`
# for i in aa2ar
do
    echo $i
    echo -n $i",DOCK 3.7," >> computational_time.csv
    echo -n `grep "elapsed time (sec):" /home/mxu02/dock37-test/test_dude/$i/dock37/dock/OUTDOCK |awk -F" " '{print $NF}'`",Vina_real," >> computational_time.csv
    echo -n `grep "real" /home/mxu02/dock37-test/test_dude/$i/vina/sge-logs |awk -F"\t" '{print $NF}'`",Vina_user," >> computational_time.csv
    echo -n `grep "user" /home/mxu02/dock37-test/test_dude/$i/vina/sge-logs |awk -F"\t" '{print $NF}'`",Vina_sys," >> computational_time.csv
    echo `grep "sys" /home/mxu02/dock37-test/test_dude/$i/vina/sge-logs |awk -F"\t" '{print $NF}'` >> computational_time.csv
done
