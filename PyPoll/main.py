import os
import csv

data_file = os.path.join('Resources', 'election_data.csv')

#defining veriables
voter_id = [] #column 1, id of voter
county = [] #column 2, county of voter
candidate = [] #comume 3, candidate the voter voted for
all_candidate = [] #new list, list of all candidates
percent_of_votes = [] #percent of votes each candidate got


#open/read csv and add content to lists
with open(data_file, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    for row in reader:
         #add voter ID
         voter_id.append(int(row[0]))

         #add county
         county.append(row[1])

         #add candidate voted for
         candidate.append(row[2])

#creates a list of candidates that recieved votes
unique_candidate = []
for i in list(candidate):
    if i not in unique_candidate:
        unique_candidate.append(i)

len_voter_id = (len(voter_id))
khanvotes = (candidate.count(unique_candidate[0])) #Total votes candidate won
correyvotes = (candidate.count(unique_candidate[1])) #Total  votes candidate won
livotes = (candidate.count(unique_candidate[2])) #Total  votes candidate won
otooleyvotes = (candidate.count(unique_candidate[3])) #Total  votes candidate won
khanperc = round((khanvotes/len_voter_id)*100,3) #Total votes candidate won
correyperc = round((correyvotes/len_voter_id)*100,3) #% of votes candidate won
liperc = round((livotes/len_voter_id)*100,3) #% of votes candidate won
otooleyperc = round((otooleyvotes/len_voter_id)*100,3) #% of votes candidate won
kvpairs = {khanvotes:'Khan',correyvotes:'Correy',livotes:'Li',otooleyvotes:"O'Tooley"} #% of votes candidate won

#print to terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {len_voter_id}')
print('-------------------------')
print(f'Khan: {khanperc}% ({khanvotes})')
print(f'Correy: {correyperc}% ({correyvotes})')
print(f'Li: {liperc}% ({livotes})')
print(f"O'Tooley: {otooleyperc}% ({otooleyvotes})")
print('-------------------------')
print(f'Winner: {(kvpairs[max(kvpairs)])}')
print('-------------------------')

#write to txtfile
txtfile = open('PyPolloutput.txt', 'w+')
txtfile.write('Election Results\n')
txtfile.write('-------------------------\n')
txtfile.write(f'Total Votes: {len_voter_id}\n')
txtfile.write('-------------------------\n')
txtfile.write(f'Khan: {khanperc}% ({khanvotes})\n')
txtfile.write(f'Correy: {correyperc}% ({correyvotes})\n')
txtfile.write(f'Li: {liperc}% ({livotes})\n')
txtfile.write(f"O'Tooley: {otooleyperc}% ({otooleyvotes})\n")
txtfile.write('-------------------------\n')
txtfile.write(f'Winner: {(kvpairs[max(kvpairs)])}\n')
txtfile.write('-------------------------')