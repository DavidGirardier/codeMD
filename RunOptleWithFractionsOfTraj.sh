#!/bin/bash
INPUT=fraction100shooting_modif_newdt0_1
SETUP=g40m0_12 
for FRACTION in {1..5}
do
	cp ${INPUT}_${FRACTION} colvarFrac
	../../bin/optle
	cp PROFILES Prof${SETUP}_${INPUT}_${FRACTION}
	cp colvar_disp_scaled_from_prop Noise${SETUP}_${INPUT}_${FRACTION}
done
