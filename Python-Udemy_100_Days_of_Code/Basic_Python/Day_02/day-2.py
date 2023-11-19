print("welcome to the tip calculator")
total_bill = input("what your total bill?\n")
total_num_people = input("how many people to split the bill?\n")
gst = input('What is gst?')

total_amt = round(float(total_bill) + (float(total_bill) * float(gst)),2)
amt_split = (float(total_bill)/int(total_num_people))
amt_pay = round((amt_split + float(gst) * amt_split),2)

# "{:.2f}.format(variabe  name)"

print ("Total Amount is "+ "$"+ str(total_amt))
print ("Amount per person is " +"$" +str(amt_pay))

#f-String
#print(f"your score is {}")