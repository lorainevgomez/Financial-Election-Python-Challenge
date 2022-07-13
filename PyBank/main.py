#Modules
import os
import csv



#Set Path for File
csvpath = os.path.join("Resources", "budget_data.csv")

#Lists to store data and Initialize Variables
Months_List = []
ProfitLoss_List = []
ProfitLoss_Change_List = []
Total= 0 
num_months = 0


#Open the csv/ Read in cvs 
with open(csvpath, newline="") as csvfile:
    #note: delimiter parameter tells python that each comma in csv should move into a new column for a row
    csvreader = csv.reader(csvfile, delimiter=",")
    #Reads first row Header
    header = next(csvreader)    


        #Indention matter in Python/ Looping through values
    for row in csvreader:
        #Add the total months in the dataset
        num_months = num_months + 1
        #net amount of profit /losses of row 1 (Note: Python starts with 0)
        Total = Total + int(row[1])
        # Add Month to the List of Months
        Months_List.append(row[0])
        #Add int values to list of Profit
        ProfitLoss_List.append(int(row[1]))


 #The changes in "Profit/Losses" over the entire period, and then the average of those changes
 #Loop through profits to find monthly change in profits
    for i in range(len(ProfitLoss_List) - 1):

        #change of values in Profit/Losses
        Change_ProfLoss = (ProfitLoss_List[i+1] - ProfitLoss_List[i])
        #Change added to the profit and loss list 
        ProfitLoss_Change_List.append(Change_ProfLoss)

    #Total Changes in Profit and Losses
    Total_ProfitLoss_Change = sum(ProfitLoss_Change_List)
    #Use Line 48 to calculate the average
    Total_ProfitLoss_Change_Average= round(Total_ProfitLoss_Change/len(ProfitLoss_List),2)

    # Need to get the Greatest Increase and Greatest Decrease in profits from the changes in Profit/Losses
    Greatest_Inc = max(ProfitLoss_Change_List)
    Greatest_Dec = min(ProfitLoss_Change_List)

    #we need the index of max and min 
    Max_Profit = ProfitLoss_Change_List.index(Greatest_Inc)
    Min_Profit = ProfitLoss_Change_List.index(Greatest_Dec)

    #Now we need the proper month to match the max and min . We use + 1 because of the change of months 
    Max_Profit_Month = Months_List[Max_Profit + 1]
    Min_Profit_Month = Months_List[Min_Profit + 1] 




print("Financial Analysis")
print("---------------------------------------------")
print("Total Months: " + str(num_months))
print("Total: " + "$" + str(Total))
print("Average Change: " + "$" + str(Total_ProfitLoss_Change_Average))
print(f"Greatest Increase in Profits: {Max_Profit_Month} (${Greatest_Inc})")
print(f"Greatest Decrease in Profits: {Min_Profit_Month} (${Greatest_Dec})")
