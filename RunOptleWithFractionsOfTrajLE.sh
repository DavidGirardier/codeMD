#!/bin/bash
INPUT=fraction500TrajVECDW10m1g5t2psdt0_001_newdt0_05
SETUP=FixedGM4_53and1_25 
for FRACTION in {1..5}
do
	cp ${INPUT}_${FRACTION} colvarFrac
	../../bin/optle
	cp PROFILES Prof${SETUP}_${INPUT}_${FRACTION}
	cp colvar_disp_scaled_from_prop Noise${SETUP}_${INPUT}_${FRACTION}
done
