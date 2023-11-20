#!/bin/bash

for LAMBDA in $(seq 0. 0.01 1.)
do
	cp oldinput input
	echo 'lambda		' $LAMBDA >>input
	#sed 's/propagator)/propagator)\nlambda \t $LAMBDA /' oldinput >> input
	../../bin/optle
	cp PROFILES changeLambda/Ciccotti/ProfilLambda_${LAMBDA}
	cat LogL >> changeLambda/Ciccotti/LogL0-1.txt
	cp colvar_disp_scaled_from_prop changeLambda/Ciccotti/colvar_disp_scaled_from_prop_${LAMBDA}
done
