for i in `cat /home/mxu02/dock37-test/test_dude/du.txt | awk -F"\t" '{print $2}'| tail -n100`
do
    cd /home/mxu02/dock37-test/test_dude/${i}/vina/output
    python ./vina_script/extract_vina_active_pose.py
    for name in `grep CHEMBL out_lig.csv| awk -F"," '{print $1}'`
    do
        energy=`grep ${name} out_lig.csv | awk -F"," '{print $NF}'`
        for mol in ${name}_actives_final_*.pdbqt
        do
            mol_energy=`grep "REMARK VINA RESULT: " ${mol} | awk -F" " '{print $4}'`
            if [ ${energy}x = ${mol_energy}x ]; then
            cat ${mol} >> active_unique.pdbqt
            echo ${mol}
            fi
            # echo ${mol}
        done
    done
    scp active_unique.pdbqt x036:/home/xumin/data/dude/${i}/vina_e8
    echo ${i}
done
