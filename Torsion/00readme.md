### Analysis Tosion distribution of docking poses.
- Analysis dock result
```bash
    bash ./torsion_dock.sh
    cd /home/mxu02/dock37-test/test_dude/script/torsion/dock/filter
    bash ./0-extract_right.sh  #output: ${i}.csv
    bash ./1-merge_right.sh  #output: dock.csv dock_uniq.csv
    bash ./2-extract_wrong.sh  #output: all_red.csv
    python ./4-count_wrong.py  #output: smiles_type.csv

```

- Analysis vina result
```bash
    bash vi.sh # seperate every target as single job, then qsub to node.
    cd /home/mxu02/dock37-test/test_dude/script/torsion/vina/filter
    bash ./2-extract_wrong.sh  #output: all_red.csv
    python ./4-count_wrong.py  #output: smiles_type.csv
```
