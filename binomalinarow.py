import numpy as np
import copy




def Find_Number_Of_Wins(n,x):
    array = np.zeros(n)
    Number_of_wins=0

    for i in range (pow(2,n)-1):
        win = 0
        check_index=0
        check = copy.deepcopy(array[check_index])
        while (1==check):
            check_index += 1
            check = copy.deepcopy(array[check_index])
        array[check_index] = 1
        if (check_index != 0):
            for i in range(check_index):
                array[i]=0
        #print(array)
        for i in range (n+1-x):
            if 1==array[i]:
                numbers_checked = 0
                for j in range(x):
                    if 1==array[i+j]:
                        numbers_checked +=1
                if numbers_checked == x:
                    win = 1
        if 1==win:
            Number_of_wins += 1
    return(int(Number_of_wins))
    #print(Number_of_wins)


#Big_array=np.zeros((9,9))
#for i in range (9):
#    for j in range(9):
#        if i>j:
#            Big_array[i][j]=Find_Number_Of_Wins(i+1,j+1)
#        elif i==j:
#            Big_array[i][j]=1

#print(Big_array)  

#print(Find_Number_Of_Wins(20,5))

def Find_Number_Of_Wins_with_probability(n,x,p):
    array = np.zeros(n)
    Number_of_wins=0
    List_of_wins=[]
    Total_Probability = 0

    for i in range (pow(2,n)-1):
        win = 0
        check_index=0
        check = copy.deepcopy(array[check_index])
        while (1==check):
            check_index += 1
            check = copy.deepcopy(array[check_index])
        array[check_index] = 1
        if (check_index != 0):
            for i in range(check_index):
                array[i]=0
        for i in range (n+1-x):
            if 1==array[i]:
                numbers_checked = 0
                for j in range(x):
                    if 1==array[i+j]:
                        numbers_checked +=1
                if numbers_checked == x:
                    win = 1
        if 1==win:
            Number_of_wins += 1
            List_of_wins.append(copy.deepcopy(array))
            print(array)

    for i in range (len(List_of_wins)):
        prob_of_this_result = 1
        for j in range(n):
            if(List_of_wins[i][j]==1):
                prob_of_this_result = p*prob_of_this_result
            else:
                prob_of_this_result = (1-p)*prob_of_this_result
        Total_Probability +=prob_of_this_result

    return(Total_Probability)

print(Find_Number_Of_Wins_with_probability(20,5,pow(20,-1)))
