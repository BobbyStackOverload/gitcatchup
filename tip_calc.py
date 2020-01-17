bill_total = int(input "How much was your bill? ")) 
service = input(" How was your service? good, fair, or bad? ").lower()
if service == "good":
    tip_amount = bill_total * 0.2
elif service == "fair":
    tip_amount = bill_total * 0.15
elif serivce = "bad":
    tip_amount = bill_total * 0.1
else:
    print("tip amount: ${:.2f}" .format(tip_amount))
    print 