#Modules
import os
import csv



#Set Path for File
csvpath = os.path.join("Resources", "election_data.csv")

#Lists to store data and Initialize Variable
Total = 0
Candidates_List = []
Unique_Candidates_List = []
Percentage_Rate = []
Unique_Winner = []





#Open the csv/ Read in cvs 
with open(csvpath, encoding='utf') as csvfile:
    #note: delimiter parameter tells python that each comma in csv should move into a new column for a row
    csvreader = csv.reader(csvfile, delimiter=",")
    #Reads first row Header
    header = next(csvreader)    


        #Indention matter in Python/ Looping through values
    for row in csvreader:
        
        #Find The total amount of votes
        Total = Total + 1
        #Add candidate names to candidates list
        Candidates_List.append(row[2])

        #Loop to get unique value of candidates
        if row[2] not in Unique_Candidates_List:
            Unique_Candidates_List.append(row[2])
    #Print out of the Loop
    print("Election Results")
    print("-----------------------------------------")
    print("Total Votes: " + str(Total))
    print("-----------------------------------------")

    for i in range(len(Unique_Candidates_List)):

        #Add a candidate's voter count
        Unique_Candidates_Votes = Candidates_List.count(Unique_Candidates_List[i])
        #This Unique winner will help find the max votes we need
        Unique_Winner.append(Unique_Candidates_Votes)
        Percentage = round((Unique_Candidates_Votes/ Total)* 100, 2)
        Percentage_Rate.append(Percentage)
      
        candidates_summary= (f"{Unique_Candidates_List[i]}: "
                f"{str(Percentage)}% "
                f"({str(Unique_Candidates_Votes)})")
        print(candidates_summary)

    #To find winner, find the Max Amount of Votes
    Max_Votes_Index = Unique_Winner.index(max(Unique_Winner))
    winner = Unique_Candidates_List[Max_Votes_Index]
    print("-----------------------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------------------")



#Set variable for output file
output_file = os.path.join("results.txt")

#Open the output file
with open(output_file, "w") as datafile:
   datafile.write("Election Results\n")
   datafile.write("-----------------------------------------\n")
   datafile.write(f"Total Votes: {Total}\n")
   datafile.write("-----------------------------------------\n")
   for i in range(len(Unique_Candidates_List)):
        Unique_Winner.append(Unique_Candidates_Votes)
        Percentage = round((Unique_Candidates_Votes/ Total)* 100, 2)
        Percentage_Rate.append(Percentage)

        candidates_summary= (f"{Unique_Candidates_List[i]}: "
                f"{(Percentage)}% "
                f"{(Unique_Candidates_Votes)}")
   datafile.write(f"{candidates_summary}")
   datafile.write('\n') 
   datafile.write("-----------------------------------------\n")
   datafile.write(f"Winner: {winner}\n")
   datafile.write("-----------------------------------------\n")