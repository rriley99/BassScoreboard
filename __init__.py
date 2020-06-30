#import tkinter
import pandas as pd
import os
import xlrd

"""
This is a program to manage the backend of an active scoreboard to be run locally on a machine.
Ideas: 
    Validate roster data
    Drop excel file as back up on each iteration? Add check for excel when loading
    Add big bass 
 """
# def if __name__ == "__main__":
#tally = pd.DataFrame(columns=["place", "boat_num", "anglers", "school", "total_weight", "big_bass"])
roster = pd.read_excel(os.path.join(os.getcwd(), 'roster.xlsx'))
tally = roster
tally.insert(loc=3, column="total_weight", value=0.0)
tally.insert(loc=4, column="big_bass", value=0.0)
print(tally)
#     return None
    
def calculate_sack(tally, max_num_fish=5):
    """This function adds fish to the tally"""
    sack_array = []
    big_bass = float
    boat_number = input("Please insert boat number: ")
    fish_counter = 0
    is_big_bass = False
    add_fish = True
    while fish_counter < max_num_fish: 
        #request weight input
        new_fish = input ("Enter a weight (in pounds): ")
        #validate float
        try:
            val = float(new_fish)
        except ValueError:
            print("Invalid entry format, please use pounds in decimal format (1.5)")
            new_fish = input ("Enter a weight (in pounds): ")
        #append to array
        sack_array.append(new_fish)
        #print array
        print(sack_array)
        #increase fish counter
        fish_counter += 1
        
        add_fish = input ("Add another fish? Y/N: ")
        if add_fish.casefold() == 'y':
            continue
        elif add_fish.casefold() == 'n':
            add_score(tally, boat_number, sack_array)
            tally.sort_values(by=['total_weight'], ascending=False, inplace=True, ignore_index=True)
            print(tally)
            break
        else:
            add_fish = input ("Add another fish? Y/N: ")
    return

def add_score(tally, boat_number, sack_array):
    find_row = tally[tally['Boat Number'] == int(boat_number)].index[0]
    print(find_row)
    find_col = tally.columns.get_loc("total_weight")
    print(find_col)
    total_weight_sum = 0

    for ele in range(0, len(sack_array)): 
        total_weight_sum = total_weight_sum + int(sack_array[ele]) 
    
    tally.iat[find_row, find_col] = total_weight_sum
    
    return


calculate_sack(tally, max_num_fish=5)
