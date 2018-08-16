import os
import csv

csv_path = os.path.join("..","PyPoll","election_data.csv")
output = os.path.join("..","PyPoll","output.txt")

with open(csv_path,newline='') as csvfile:
	csvreader = csv.reader(csvfile,delimiter=',')
	csvheader = next(csvreader)
	name_list=[]
	vote_count=[]
	for row in csvreader:
		if row[2] not in name_list:				#if name is not in the list
			name_list.append(row[2])			# add name & vote count to both list
			vote_count.append(1)
		else:									# if name is already in the list
			for x in name_list:					# let count add 1
				if x ==row[2]:
					vote_count[name_list.index(x)] += 1

total_votes = 0
for y in vote_count:
	total_votes += y                                #get total votes

vote_percentage = []
highest_vote = 0
for z in vote_count:
	vote_percentage.append(z/total_votes)
	if z>=highest_vote:
		highest_vote = z                               #get highest votes

winner = name_list[vote_count.index(highest_vote)]     #get winner name 

print ("Election Results") 
print ("------------------------------------")  
print (f"Total Votes: {total_votes}")
print ("------------------------------------")
for name in name_list:
	print(f"{name}: {round(vote_percentage[name_list.index(name)]*100,3)}% ({vote_count[name_list.index(name)]})")
print ("------------------------------------")
print(f"Winner: {winner}")
print ("------------------------------------")

file = open(output,"w")
file.write("Election Results\n") 
file.write("------------------------------------\n")  
file.write(f"Total Votes: {total_votes}\n")
file.write("------------------------------------\n")
for name in name_list:
	file.write(f"{name}: {round(vote_percentage[name_list.index(name)]*100,3)}% ({vote_count[name_list.index(name)]})\n")
file.write("------------------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("------------------------------------\n")