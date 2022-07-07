# for i in `cat /home/mxu02/dock37-test/test_dude/du.txt | awk -F"\t" '{print $2}'| tail -n100`
for i in aa2ar
do
    cd /home/mxu02/dock37-test/test_dude/${i}/vina/output
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
            cat test.sdf >> /home/mxu02/dock37-test/test_dude/script/torsion/vina_uniq_mol/$i.sdf
            echo ${mol}
            fi
        done
    done
    # grep "REMARK VINA RESULT: " unique.pdbqt |awk -F" " '{print $4}' > energy
    # grep ".pdbqt" unique.pdbqt |awk -F" " '{print $2}' > name
    # paste -d" " name energy > uniq_name_energy.csv
    # rm name energy
    echo ${i}
done
