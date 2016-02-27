#!/bin/sh
TOTAL=0
SUM=0
i=1
x=0
while [[ -z $IMEI ]]
	do
		read -p "Enter your IMEI number: " IMEI
	done
MOD=$(echo -n ${IMEI} | sed 's/.$//')
DIGITS=$(echo -n $MOD | wc -c)
ORGDIG=$(echo -n ${IMEI} | wc -c)
CHECK=$(echo ${IMEI} | cut -c ${ORGDIG})
COUNTRY=$(echo ${IMEI} | cut -c 7,8)
for (( i=2 ; i<=${DIGITS} ; i+=2 ))
	do
		NUM1=$(echo $(echo -n ${MOD} | cut -c $i))
		MUL1=$((${NUM1}*2))
		if [[ ${MUL1} -lt 10 ]]; then
			x=$((x+${MUL1}))
		else
			y=$(echo ${MUL1} | cut -c 1)
			z=$(echo ${MUL1} | cut -c 2)
			v=$(($y+$z))
			x=$((x+${v}))
		fi
RESULT1=${x}
	done
for (( j=1; j<=${DIGITS} ; j+=2 ))
	do
		NUM2=$(echo $(echo -n ${MOD} | cut -c $j))
		RESULT2=$((${RESULT2}+${NUM2}))
	done
RESULT=$((${RESULT1}+${RESULT2}))
REMAIN=`expr ${RESULT} % 10`
MUST=$((10 - ${REMAIN}))
if [[ ${MUST} = ${CHECK} ]]; then
	echo "Your IMEI number is VALID"
	case ${COUNTRY} in
	00)				echo "Your phone is originated from the actual country of Phone Company itself and it's quality is the 'BEST'";;
	01|10)			echo "Your phone is manufactured in 'Finland' and it's quality is 'VERY GOOD'";;
	02|20)			echo "Your phone is manufactured in 'Emirates' and it's quality is 'LOW'";;
	03|04|30|40)	echo "Your phone is manufactured in 'China' and it's quality is 'GOOD'";;
	05|50)			echo "Your phone is manufactured either in 'Brazil,USA or Finland' and it's quality is 'GOOD'";;
	06|60)			echo "Your phone is manufactured either in 'Hong-Kong or Mexico' and it's quality is 'NOT BAD'";;
	08|80)			echo "Your phone is manufactured in 'Finland' and it's quality is 'FAIR'";;
	13)				echo "Your phone is manufactured in 'Finland' and it's quality is 'TOO BAD and DANGEROUS for health!'";;
	esac
else
	echo "Your IMEI number is not VALID"
fi
