#!/bin/bash
for i in `cat ../../dude_list`
do
    sed -i '1d' ${i}.csv
    awk -F"," '{print $1}' ${i}.csv >> dock.csv
    echo ${i}
done
sort -u dock.csv > dock_uniq.csv
