#!/bin/bash
# for i in `awk -F"\t" '{print $2}' du.txt | sed -n '1,30p'`
for i in `sort dude.name dock_target dock_target |uniq -u |head`
do
    test -d /home/mxu02/FDA_approved_drugs/dude_db2/${i} || mkdir /home/mxu02/FDA_approved_drugs/dude_db2/${i}
    cd /home/mxu02/FDA_approved_drugs/dude_db2/${i}
    # scp xumin@k058:/mirrors/pub/auto-dud-e/dude_e_db2/${i}/*.db2.gz .
    scp mxu@z55:/pubhome/ftp/dataset/dude/decoys-${i}/*.gz /pubhome/ftp/dataset/dude/ligands-${i}/*.gz .
    echo ${i}
done
