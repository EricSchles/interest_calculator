
def calculate_interest_per_period(P,R,t):
    r = R/100.0
    return P*(1 +r*t)

def interest_over_time(num_years,number_of_compoundings_per_year,interest_rate,principal_balance):
    return sum([calculate_interest_per_period(principal_balance,interest_rate,1/float(number_of_compoundings_per_year)) for elem in xrange(num_years)])

print interest_over_time(1,5,15,4900)
