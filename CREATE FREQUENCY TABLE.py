from math import log10
from statistics import mean,median,mode
from tabulate import tabulate

class color:
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
#----------------------------------------------------CREATING EMPTY TABLE-----------------------------------------------
def creating_empty_table():
    global table
    global table_2
    global color
    global n_intervals_round
    add_rows =  ["          ","  ","  ","  ","  ","  ","     "]
    table =          [[color.RED+"intervals"+color.ENDC,
                        color.RED+"Xi"+color.ENDC,
                        color.RED+"fi"+color.ENDC,
                        color.RED+"Fi"+color.ENDC,
                        color.RED+"fr"+color.ENDC,
                        color.RED+"Fr"+color.ENDC,
                        color.RED+"Xi.fi"+color.ENDC]]

    table_2 = [[color.RED+"MEAN"+color.ENDC,
               color.RED+"MEDIAN"+color.ENDC,
               color.RED+"MODE"+color.ENDC]]

    add_rows2 = ["     ","       ","    "]

    table_2.append(add_rows2)
    
    for x in range(n_intervals_round+1):   
        add_rows = add_rows[:]
        table.append(add_rows)

    table_2[1][0] = color.YELLOW+str(mean_1)+color.ENDC
    table_2[1][1] = color.YELLOW+str(median_1)+color.ENDC
    table_2[1][2] = color.YELLOW+str(mode_1)+color.ENDC
#----------------------------------------------------INTERVALS----------------------------------------------------------
def intervals(parameter1,parameter2):

    if column == 0 and row <= n_intervals_round:

        #Change symbols to include or not the numbers in the intervals
        if row == len(table)-1:
            inclusion = "]"
        else:
            inclusion = ")"
        
        table[row][0] = "[" + str(round(parameter1,2)) + "-" + str(round(parameter2,2)) + inclusion
        
        #Average of the intervals
        table[row][1] = round((parameter1 + parameter2) / 2,3)
#----------------------------------------------------ABSOLUTE FREQUENCY ( fi )------------------------------------------
def absolute_frequency(parameter1,parameter2):
    global sum_fi
    global column
    global create_diccionary
    global color
    
    #       |      0     | 1  |  2 |  3 |  4 |  5 |   6   |
    #       | intervals | Xi | fi | Fi | fr | Fr | Xi.fi |

    if column == 2 and row <= n_intervals_round:
        
        #Crear diccionario de frequency absolutas una vez
        if create_diccionary == True:
            for x in data:
                frecuencia_absoluta = data.count(x)
                frequency[x] = frecuencia_absoluta
            create_diccionary = False
            

        #frequency absolutas por intervalo
        for x in frequency:
            
            #Si no es la ultima row
            if row != (len(table)-2):
                if x >= parameter1 and x < parameter2:
                    sum_fi = sum_fi + frequency[x]
                
                if x == final:
                    total_fi.append(sum_fi)
                    table[row][2] = sum_fi
                    sum_fi = 0
            #Cuando trabajamos con la ultima row
            elif x >= parameter1 and x <= parameter2:
                sum_fi = sum_fi + frequency[x]
            
                if x == final:
                    total_fi.append(sum_fi)
                    table[row][2] = sum_fi
                    sum_fi = 0
    
    #Total de las frequency absolutas
    if row == n_intervals_round :
        table[row+1][2] = str(color.GREEN + str(sum(total_fi)) + color.ENDC)
#----------------------------------------------------CUMULATIVE ABSOLUTE FREQUENCY ( Fi )-------------------------------
def cumulative_absolute_frequency():
    sum_acumulate = 0
    for x in range(1,n_intervals_round+1):
        
        if x == n_intervals_round:
            table[x][3] = color.GREEN + str(int(table[x][2]) + sum_acumulate) + color.ENDC
        else:
            table[x][3] = table[x][2] + sum_acumulate
            sum_acumulate = table[x][3]
#----------------------------------------------------RELATIVE FREQUENCY ( fr )------------------------------------------ 
def relative_frequency():

    for x in range(1,n_intervals_round+1):
        table[x][4] = round((table[x][2] / len(data)),2)
        total_fr.append(table[x][4])
    table[n_intervals_round+1][4] = str(color.GREEN + str(sum(total_fr)) + color.ENDC)
#----------------------------------------------------CUMULATIVE RELATIVE FREQUENCY ( Fr )-------------------------------
def cumulative_relative_frequency():
    sumar_relativa = 0
    for x in range(1,n_intervals_round+1):
        
        if x == n_intervals_round:
            table[x][5] = color.GREEN + str(table[x][4] + sumar_relativa) + color.ENDC
        else:
            table[x][5] = round(table[x][4] + sumar_relativa,2)
            sumar_relativa = table[x][5]
#----------------------------------------------------XI * fi------------------------------------------------------------
def Xi_fi():
    for x in range(1,n_intervals_round+1):
        table[x][6] = round(table[x][1] * table[x][2],3)
        total_xi_fi.append(table[x][6])
    table[n_intervals_round+1][6] = str(color.GREEN + str(sum(total_xi_fi)) + color.ENDC)
#----------------------------------------------------MAIN---------------------------------------------------------------
def main():

    #-------------------------------data---------------------------------------------------
   
    """ EXAMPLE 1 : [6,6,6,7,7,7,7,8,8,8,9,9,9,9,9,9,9,9,9,9,9,10,10,10,11,12,12,12,12,12] """
    """ EXAMPLE 2 : [15,15,25,25,27,27,27,30,30,30,30,30,30,30,30,30,35,35,36,
                    36,37,37,37,40,40,40,40,40,40,45,45,45,46,46] """
    
    global mean_1
    global mode_1
    global median_1
    global sum_acumulate
    global total_fi
    global create_diccionary
    global frequency
    global sum_fi
    global final
    global n_intervals_round
    global color
    global data
    global column
    global row
    global total_xi_fi
    global total_fr

    data = [15,15,25,25,27,27,27,30,30,30,30,30,30,30,30,30,35,35,36,
            36,37,37,37,40,40,40,40,40,40,45,45,45,46,46]
    data = sorted(data)
    mean_1      = mean(data)
    mode_1      = mode(data)
    median_1    = median(data)
    sum_acumulate = 0
    total_fi = []
    total_xi_fi = []
    total_fr = []
    create_diccionary = True
    frequency = {}
    sum_fi     = 0
    start      = min(data)
    final       = max(data)

    #-----------------------------RANGE----------------------------------

    intervals_range = max(data)-min(data)

    #-----------------------------------------------
    print("\033[H\033[J") 
    n_intervals = 1 + 3.322 * log10(len(data))
    n_intervals_round = round(n_intervals)
    

    #------------------ WTIDTH ------------------------------------

    width = round(intervals_range/n_intervals_round,2)
    
    
    #------------------CREATE EMPTY TABLE ------------------------------
    creating_empty_table()
    
    for row in range(0,len(table)):
        for column in range(0,7):
            #------------------------------------FIRST ROW-----------------------------------------
            if row != 0 and row == 1:

                #---------------------Intervals--------------------------------------
                intervals(parameter1=start,
                            parameter2=(start+width))
                #----------------------Absolute frequency----------------------------
                absolute_frequency(parameter1=start,
                                    parameter2=(start+(width*row)))
                #---------------------Cumulative absolute frequency -----------------

            #---------------------------------- OTHER ROWS -----------------------------------------
            elif row != 0 and row != 1:
                
                #---------------------Intervals--------------------------------------
                intervals(parameter1=(start+((width*row)-width)),
                           parameter2=(start+((width*row))))
                
                #------------------Absolute frequency---------------
                absolute_frequency(parameter1=start+(width*row)-width,
                                    parameter2=(start+(width*row)))
    
    cumulative_absolute_frequency()
    relative_frequency()
    cumulative_relative_frequency()
    Xi_fi()
    print(tabulate(table, headers="firstrow",tablefmt="fancy_grid"))
    print(tabulate(table_2, headers="firstrow",tablefmt="fancy_grid"))           

main()






    