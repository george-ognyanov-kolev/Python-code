# Write a function for converting BGN, USD, EUR and GBP between each other, 
#based on user prompt input regarding source currency, target currency and source amount. 
# Round the results to two digits after the decimal point using the following fixed rates:
def convfunc():
    sc = input ("source currency: ")
    tc = input ("target currency: ")
    sa = int(input ("source amount: "))
# Convert BGN to USD and USD to BGN
    if sc == 'BGN' and tc == 'USD':
        ta = sa * 1.57558
    elif sc == 'USD' and tc == 'BGN':
        ta = sa / 1.57558
# Convert BGN to EUR and EUR to BGN
    elif sc == 'BGN' and tc == 'EUR':
        ta = sa * 1.95583
    elif sc == 'EUR' and tc == 'BGN':
        ta = sa / 1.95583
# Convert BGN to GBP and GBP to BGN
    elif sc == 'BGN' and tc == 'GBP':
        ta = sa * 2.206240
    elif sc == 'GBP' and tc == 'BGN':
        ta = sa / 2.206240
# Convert USD to GBP and GBP to USD
    elif sc == 'USD' and tc == 'GBP':
        ta = sa * 0.814130
    elif sc == 'GBP' and tc == 'USD':
        ta = sa / 0.814130
    else:
        print ("Invalid currency!")
    print(round(ta,2))
convfunc()