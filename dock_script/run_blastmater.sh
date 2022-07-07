#!/bin/bash

conda activate dock37

export DOCKBASE=`readlink -f /home/soft/ucsfdock/DOCK-3.7b-bela30c/`
python2.7 $DOCKBASE/proteins/blastermaster/blastermaster.py --addhOptions=" -HIS -FLIPs " -v
cd dockfiles
$DOCKBASE/proteins/showsphere/doshowsph.csh matching_spheres.sph 1 matching_spheres.sph.pdb
