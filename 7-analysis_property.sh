#!/bin/bash
for i in aa2ar
do
sed "s/kpcb/${i}/g" ./analysis_property.py > analysis_${i}.py
python analysis_${i}.py
echo "*************************${i}*****************************"
done
