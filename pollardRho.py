import pdb
import math
import random
def gcd(a,b) :
	if a > b :
		divident=a
		divisor=b
	elif a < b :
		divident=b
		divisor=a
	else :
		return a
	
	remainder = divident % divisor
	if remainder == 0 :
		return divisor
	elif remainder >= 1 :
		answer = gcd(divisor,remainder)
	
	return answer
		
#pollards rho integer factoring algorithm
def factor(number) :
	#xrange lazily generates the next number in the sereis unlike range() which simply produces an array   
        #returns 1 if no common factor was found
        answer = 0
	for x in xrange(int(math.sqrt(number))) :
		ran1 = random.randint(1,number)
                ran2 = random.randint(1,number)
                diff = ran1-ran2
                if diff<0 :
                        diff = -1 * diff
                elif diff == 0 :
                        continue
                result = gcd(diff,number)
                if result > 1 :
                        answer = result
                        break
                elif result == 1 :
                        answer = 1

        return answer

val = factor(16)
print val
