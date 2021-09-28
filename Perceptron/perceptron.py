import sys

def Perceptron(data, output):

	datafile = open(data)
	outputfile = output

	x = []          #x values
	t = []          #target values 
	
        #Reading the data file	
	i=0	
	for line in datafile:
            
		x.insert(i,line.split())
		
		if(x[i][0] == 'A'):
			t.insert(i,1)
		else:
			t.insert(i,0)
					
		x[i][0] = 1		
		i=i+1
		
	rows = len(x)
	columns = len(x[0])

	print(rows,columns)
	
	delta_w = columns*[0]
	delta_w_annealing = columns*[0]
	
	w = [0]*columns
	w_annealing = [0]*columns
	
	o = [0]*rows
	o_annealing = [0]*rows
	
	errors = [0]*101
	errors_annealing = [0]*101
	
	for i in range(101):              
                
		for row in range (rows):

			#Classify

			for a in range(columns):
                                o[row] +=  (w[a] * float(x[row][a]))
                                o_annealing[row] +=  (w_annealing[a] * float(x[row][a]))
	
                        if (o[row] > 0):
                                o[row] = 1
                        else:
                                o[row] = 0
		
                        if (o_annealing[row] > 0):
                                o_annealing[row] = 1
                        else:
                                o_annealing[row] = 0
			
			#Calculate delta w
			
			for b in range(columns):
                                diff = (float(t[row]) - o[row])
                                x_value = float(x[row][b])
                                rate = 1
                                delta_w[b] += (diff*x_value*rate)
		
                                diff_annealing = (float(t[row]) - o_annealing[row])
                                rate_annealing = 1/(i+1)
                                
                                delta_w_annealing[b] += (diff_annealing*x_value*rate_annealing)
                                                         
                        #Error Classification 
                        if (o[row] != t[row]):
                                errors[i] = errors[i] + 1
                        if (o_annealing[row] != t[row]):
                                errors_annealing[i] = errors_annealing[i] + 1
                        o[row] = 0
                        o_annealing[row] = 0			
                                                                      
		#Calculate w
                
                for c in range(columns):
                        w[c] = w[c] + delta_w[c]
                        delta_w[c] = 0
		
                        w_annealing[c] = w_annealing[c] + delta_w_annealing[c]
                        delta_w_annealing[c] = 0              

	print("Check the Output file!")	
		
	#Output
	with open(outputfile, "a+") as output:
		for d in range(101):
			output.write(str(errors[d]))
			output.write("\t")
		output.write("\n")
		for e in range(101):
			output.write(str(errors_annealing[e]))
			output.write("\t")
		output.write("\n\n")
	
Perceptron(sys.argv[1], sys.argv[2])

