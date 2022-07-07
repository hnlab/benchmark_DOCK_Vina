for i in `cat ../../dude_list`
# for i in inha nos1 pa2ga pgh1 pnph pyrd sahh tysy
do
    python ./3-filter_mol.py -i ../${i}_out.csv -o ${i}.csv
    echo ${i}
done
