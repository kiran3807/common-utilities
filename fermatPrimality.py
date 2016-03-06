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

def isItPrime(number):
    answer = False
    #more the number of iterations more we can be sure that the number we have in mind is prime
    #This is due to conditional probability
    for index in xrange(20):
        base = random.randint(1,number-1)
        #We use two tests to increase the accuracy. we test for gcd and the we apply fermat's little theorem
        if(gcd(number,base) == 1):
            result = ( base**(number - 1) )%number
            if result == 1 :
                answer = True
            else :
                return False
    return answer

