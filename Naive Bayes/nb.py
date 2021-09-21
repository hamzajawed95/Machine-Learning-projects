import sys
import math

def NB(data, output):

	datafile = open(data)
	outputfile = output

        
	x = []         
	t = []
	t1 = []
	t2 = []
                        
        #Reading the data file
	
	i=0
	for line in datafile:
		x.insert(i,line.split())
		if(x[i][0] == 'A'):
			t1.insert(i,1)
			t.insert(i,1)
		if(x[i][0] == 'B'):
			t2.insert(i,0)
			t.insert(i,0)
	
		i=i+1
		
	rows_A = [0]*2	
	rows_A[0] = len(t1)
	rows_A[1] = len(t2)
	
	rows = len(x)
	columns = len(x[0])
	
        uA = [0]*2
        u_A = [0]*2

        for column in range(columns-1):
                
                for row in range(rows_A[0]):
                        uA[column] += float(x[row][column+1])
                
                u_A[column] = uA[column]/rows_A[0]                                                                          
         

        uB = [0]*2
        u_B = [0]*2

        for column in range(columns-1):
                
                row = rows_A[0]
                
                while row<rows:
                        uB[column] += float(x[row][column+1])
                        row+=1
                          
                u_B[column] = uB[column]/rows_A[1]


        sA = [0]*2
        s_A = [0]*2
        
        for column in range(columns-1):
                for row in range(rows_A[0]):
                        sA[column] += (float(x[row][column+1])-u_A[column])**2

                s_A[column] = sA[column]/(rows_A[0]-1)


        sB = [0]*2
        s_B = [0]*2

        for column in range(columns-1):   
                row = rows_A[0]
                
                while row<rows:
                        sB[column] += (float(x[row][column+1])-u_B[column])**2
                        row+=1
                        
                s_B[column] = sB[column]/(rows_A[1]-1)


        p = [0]*2
        cl=2

        for c in range(cl):
                p[c] = float(rows_A[c])/rows
                
        ex = [1]*2
        ex2 = [1]*2
        P_A = [0]*2
        P_B = [0]*2
        ms = 0

        for row in range(rows):
                for column in range(columns-1):
    
                        pi = math.pi
                        
                        ex[column] = math.exp((-(float(x[row][column+1])-u_A[column])**2)/(2*s_A[column]))
                        ex2[column] = math.exp((-(float(x[row][column+1])-u_B[column])**2)/(2*s_B[column]))
                        
                        P_A[column] = (1/math.sqrt(2*pi*s_A[column]))*ex[column]
                        P_B[column] = (1/math.sqrt(2*pi*s_B[column]))*ex2[column]
                       
                        
                PA = p[0]*P_A[0]*P_A[1]
                PB = p[1]*P_B[0]*P_B[1]

                cs = 0

                if PA > PB:
                        cs=1
                       
                if PA < PB:
                        cs=0
                      
                if t[row]!=cs:
                        ms+=1 
        

	print("Check the Output file!")	
		

	#Output
	
	with open(outputfile, "a+") as output:
                for column in range(columns-1):
                        output.write(str(u_A[column]))
                        output.write("\t")
                        output.write(str(s_A[column]))
                        output.write("\t")  
                output.write(str(p[0]))
                output.write("\n")
                
                for column in range(columns-1):        
                        output.write(str(u_B[column]))
                        output.write("\t")
                        output.write(str(s_B[column]))
                        output.write("\t")
                output.write(str(p[1]))
                output.write("\n")
                output.write(str(ms))
                output.write("\n")
	
	
NB(sys.argv[1], sys.argv[2])

