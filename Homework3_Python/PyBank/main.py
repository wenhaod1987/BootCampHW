import os
import csv

csv_path = os.path.join("..","PyBank","Budget_data.csv")
output = os.path.join("..","PyBank","output.txt")

with open(csv_path,newline='') as csvfile:
	csvreader = csv.reader(csvfile,delimiter=',')
	csvheader = next(csvreader)
	month = []
	reve_data  = []
	total =0.00
	for row in csvreader:			# put month/year and revenue into each list
		month.append(row[0])
		reve_data.append(float(row[1]))
		total = total + float(row[1])  #calculate total revenue

	count = len(month)         # get # of month
	reve_change = [0]

	for x in range(1, count):  # calculate revenue change for each month, reve_change is wirrtien starting at index 1
		reve_change.append(reve_data[x] - reve_data[x-1])  
		
	total_change = 0.00
	change_high = 0.00
	change_low = 0.00

	for y in range (1,count):
		total_change = total_change + reve_change[y]
		if reve_change[y]> change_high:
			change_high = reve_change[y]
			change_high_month=month[y]
		elif reve_change[y]< change_low:
			change_low = reve_change[y]
			change_low_month = month[y]

average_change = round(total_change / count,2)
print ("Financial Analysis") 
print ("------------------------------------")  
print(f"Total Months: {count+1}") 
print(f"Total: {total}")  
print(f"Average Change: ${average_change}")  
print(f"Greaest Increase in Profits: {change_high_month} (${change_high})")  
print(f"Greaest Decrease in Profits: {change_low_month} (${change_low})")	

file = open(output,"w")
file.write("Financial Analysis")
file.write("\n")
file.write("------------------------------------")  
file.write("\n")
file.write(f"Total Months: {count+1}") 
file.write("\n")
file.write(f"Total: {total}")  
file.write("\n")
file.write(f"Average Change: ${average_change}")  
file.write("\n")
file.write(f"Greaest Increase in Profits: {change_high_month} (${change_high})")  
file.write("\n")
file.write(f"Greaest Decrease in Profits: {change_low_month} (${change_low})")	
file.close()







