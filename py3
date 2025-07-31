print("Goverment of tamil nadu")
print("Electricity Borad")
print("-----------------")
no1=input(" enter the ebno:")
no2=input(" enter the coustmor name:")
previous=int(input("reading for previous month:"))
current=int(input("reading for current month:"))
total=current-previous
print("total unit consumed:",total)
paid=total*5
print("amount to be paid rs",paid)                   
