weight = 41.5
String1 = 'Your Package weighs: '
lbs='lbs'
W_Msg= String1 + str(weight) + lbs

print(W_Msg)

Price_Per_Pound = 0
MoneySign = '$'

#Ground Shipping
print('Ground Shipping:')

Flat_Charge_GS = 20

if weight <= 2:
  Price_Per_Pound += 1.50 * weight
elif weight >= 2 and weight <= 6 :
  Price_Per_Pound += 3.00 * weight
elif weight >= 6 and weight <= 10 :
  Price_Per_Pound += 4.00 * weight
elif weight >= 10 :
  Price_Per_Pound += 4.75 * weight

Cost = Price_Per_Pound + Flat_Charge_GS
End_Msg= str(Cost)+MoneySign
print(End_Msg)

#Ground Shipping Premium
print('Ground Shipping Premium:')

Flat_Charge_GSP = 125

Cost = Price_Per_Pound + Flat_Charge_GSP
End_Msg= str(Cost)+MoneySign
print(End_Msg)

#Drone Shipping
print('Drone Shipping:')

Flat_Charge_DS = 0

if weight <= 2:
  Price_Per_Pound += 4.50 * weight
elif weight >= 2 and weight <= 6 :
  Price_Per_Pound += 9.00 * weight
elif weight >= 6 and weight <= 10 :
  Price_Per_Pound += 12.00 * weight
elif weight >= 10 :
  Price_Per_Pound += 14.25 * weight

Cost = Price_Per_Pound + Flat_Charge_DS
End_Msg= str(Cost)+MoneySign
print(End_Msg)