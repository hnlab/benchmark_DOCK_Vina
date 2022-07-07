for i in `cat dude_list`
# for i in inha nos1 pa2ga pgh1 pnph pyrd sahh tysy
do
    # rm /home/mxu02/dock37-test/test_dude/script/torsion/dock/filter/${i}.csv /home/mxu02/dock37-test/test_dude/script/torsion/dock/${i}_out.csv
    cd /home/mxu02/dock37-test/test_dude/${i}/dock37
    /home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/torsionchecker --license AAAAAAAliPQAAAAU0WVcW4zmBK/zhUqEZf+g8NeQaPg=\
    -m poses.mol2 -t /home/mxu02/soft/TorsionAnalyzer/Torsion\ Analyzer/lib/TorLibv21WCSDBins.xml -r /home/mxu02/dock37-test/test_dude/script/torsion/dock/${i}_out.csv
    echo ${i}
done
