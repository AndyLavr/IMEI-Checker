import ast

IMEI = raw_input("Enter your IMEI number: ")
while (IMEI == ""):
	IMEI = raw_input("Enter your IMEI number: ")

TOTAL = 0
SUM = 0
x1 = 0
x2 = 0
MOD = IMEI[:-1]
DIGITS = len(MOD)
ORGDIG = len(IMEI)
CHECK = ast.literal_eval(IMEI[DIGITS])
country = IMEI[6:8]

for i in range(1,DIGITS,2):
	num_1 = IMEI[i]
	num1 = ast.literal_eval(num_1)
	mul1 = num1*2
	if mul1 < 10:
		x1 += mul1
	else:
		STR = str(mul1)
		y = ast.literal_eval(STR[0])
		z = ast.literal_eval(STR[1])
		v = y + z
		x1 += v

RESULT1 = x1

for j  in range(0,DIGITS,2):
	num_2 = IMEI[j]
	x2 += ast.literal_eval(num_2)

RESULT2 = x2

RESULT = RESULT1 + RESULT2
REMAIN = RESULT % 10
MUST = 10 - REMAIN

CASE = {
	'00': 'Your phone is originated from the actual country of Phone Company itself and it s quality is the "BEST"',
    "01": "Your phone is manufactured in 'Finland' and it's quality is 'VERY GOOD'",
	"10": "Your phone is manufactured in 'Finland' and it's quality is 'VERY GOOD'",
    "02": "Your phone is manufactured in 'Emirates' and it's quality is 'LOW'",
	"20": "Your phone is manufactured in 'Emirates' and it's quality is 'LOW'",
    "03": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
	"04": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
	"30": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
	"40": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
    "05": "Your phone is manufactured either in 'Brazil,USA or Finland' and it's quality is 'GOOD'",
	"50": "Your phone is manufactured either in 'Brazil,USA or Finland' and it's quality is 'GOOD'",
    "06": "Your phone is manufactured either in 'Hong-Kong or Mexico' and it's quality is 'NOT BAD'",
	"60": "Your phone is manufactured either in 'Hong-Kong or Mexico' and it's quality is 'NOT BAD'",
    "08": "Your phone is manufactured in 'Finland' and it's quality is 'FAIR'",
	"80": "Your phone is manufactured in 'Finland' and it's quality is 'FAIR'",
    "13": "Your phone is manufactured in 'Finland' and it's quality is 'TOO BAD and DANGEROUS for health!'"
}

if MUST == CHECK:
	print ("Your IMEI is VALID")
	print (CASE[country])
else:
	print ("Your IMEI is not VALID")
