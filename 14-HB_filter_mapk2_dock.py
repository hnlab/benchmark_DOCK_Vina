#!/usr/bin/python
"""
    1. Filter actives according to HBs between 3 key AAs and ligand.
    > python ./HB_filter_mapk2.py -p rec.crg.pdb -l poses.mol2 -x xtal-lig.pdb
"""
import argparse
import os
import re
import subprocess
import tempfile
import time
# 计算密集性用进程Pool.
from multiprocessing import Pool
# 非计算密集型或者是调用其他程序用线程dummy, https://mozillazg.com/2014/01/python-use-multiprocessing-dummy-run-theading-task.html
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-p', '--protein', required=True)
parser.add_argument('-l', '--ligand', required=True)
parser.add_argument('-x', '--xtal_lig', required=True)
args = parser.parse_args()

rec_file = Path(args.protein).absolute()  # absolute path
xtal_file = Path(args.xtal_lig).absolute()

def read_frame(filename):
    with open(filename) as f:
        lines = []
        for line in f:
            if '##########                 Name:' in line:
                if lines:
                    yield lines
                lines = []
            lines.append(line)
        if lines:
            yield lines


def count_hbond(pdb_frame):
    with tempfile.TemporaryDirectory() as tempdir:
        # https://stackoverflow.com/questions/30793080/how-to-remove-tempfile-in-python
        # deletes everything automatically at end of with
        # time.sleep(5)
        tempdir = Path(tempdir)
        lig_file = tempdir / "ligand.mol2"
        com_file = tempdir / "tmp.com"
        hbond_file = tempdir / "hbond.outs"

        com_str = (
            f'open {xtal_file} {rec_file} {lig_file}\n'
            f'sel #1:141.A@N\n'
            f'close #0\n'
            f'hbonds intermodel true intramodel false selRestrict cross relax true showDist true savefile {hbond_file}\n'
            f'stop\n')

        with open(lig_file, 'w') as f:
            for line in pdb_frame:
                f.write(line)

        with open(com_file, 'w') as f:
            # chimera command file need end with '.com'
            f.write(com_str)

        subprocess.run(['chimera', '--nogui', com_file])

        hbond_count = 0
        try:
            with open(hbond_file) as f:
                for line in f:
                    if '#2:1' in line:
                        hbond_count += 1
        except IOError:
            print("File is not accessible.")

    return hbond_count


with ThreadPool() as pool:
    frames = list(read_frame(args.ligand))
    results = pool.map(count_hbond, frames)
    # auto pool.close()

out = open('hbond.out', 'w')
out_mol2 = open('hbond.mol2', 'w')

for frame, hbond_count in zip(frames, results):
    if hbond_count >= 1:
        remark = frame[0].split(":")[1].split()[0]
        remark = remark.strip()  # remove '\n' in the end
        out.write(f'{remark} hbond={hbond_count}\n')
        for line in frame:
            out_mol2.write(f'{line}')

out.close()
out_mol2.close()
