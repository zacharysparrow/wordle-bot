#!/bin/bash

#SBATCH -J nece_opt
#SBATCH -p vega
#SBATCH -c 48
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --time=4:00:00
#SBATCH --mem-per-cpu=4GB

python compute_depth_hist.py
