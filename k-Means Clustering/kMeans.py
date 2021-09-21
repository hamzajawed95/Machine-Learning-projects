import sys

def centroids(c1,c2,c3):
    
    d1 = [0]*rows
    d2 = [0]*rows
    d3 = [0]*rows
    
    global a1,a2,a3
    a1 = c1
    a2 = c2
    a3 = c3

    for row in range(rows):
            d1[row] = (((float(x[row][1])-c1[0])**2) + (float(x[row][2])-c1[1])**2)

    for row in range(rows):
            d2[row] = (((float(x[row][1])-c2[0])**2) + (float(x[row][2])-c2[1])**2) 

    for row in range(rows):
            d3[row] = (((float(x[row][1])-c3[0])**2) + (float(x[row][2])-c3[1])**2)
        
    c1 = [0,0]
    c2 = [0,0]
    c3 = [0,0]
    
    d = 0
                
    i=0
    for row in range(rows):
            if(d1[row]<d2[row] and d1[row]<d3[row]):
                    c1[0]+=float(x[row][1])
                    c1[1]+=float(x[row][2])
                    d+=d1[row]
                    i+=1              
    c1[0]=c1[0]/i
    c1[1]=c1[1]/i
    c1 = c1[0],c1[1]
               
    i=0
    for row in range(rows):
            if(d2[row]<d1[row] and d2[row]<d3[row]):
                    c2[0]+=float(x[row][1])
                    c2[1]+=float(x[row][2])
                    d+=d2[row]
                    i+=1              
    c2[0]=c2[0]/i
    c2[1]=c2[1]/i
    c2 = (c2[0],c2[1])
             
    i=0
    for row in range(rows):
            if(d3[row]<d1[row] and d3[row]<d2[row]):
                    c3[0]+=float(x[row][1])
                    c3[1]+=float(x[row][2])
                    d+=d3[row]
                    i+=1             
    c3[0]=c3[0]/i
    c3[1]=c3[1]/i
    c3 = (c3[0],c3[1])

    return c1,c2,c3,d



                

def kMeans(data, output1, output2):

	datafile = open(data)
	outputfile1 = output1
	outputfile2 = output2

        global x
	x = []
	
        #Reading the data file
	
	i=0
	for line in datafile:
		x.insert(i,line.split())
		i=i+1
	global rows	
	rows = len(x)

	global c1,c2,c3 
        c1 = [0,5]
        c2 = [0,4]
        c3 = [0,3]
        
        with open(outputfile1, "w+") as output:
                output.write(str(c1[0]))
                output.write(',')
                output.write(str(c1[1]))
                output.write("\t")
                        
                output.write(str(c2[0]))
                output.write(',')
                output.write(str(c2[1]))
                output.write("\t")
                        
                output.write(str(c3[0]))
                output.write(',')
                output.write(str(c3[1]))
                output.write("\n")
                
        with open(outputfile2, "w+") as output2:
                        output2.close()



                                    
        while(1):

                
                c1,c2,c3,d = centroids(c1,c2,c3)
                
                if (c1==a1 and c2==a2 and c3==a3):
                        
                        c1,c2,c3,d = centroids(c1,c2,c3)
                        break
               
                #Output
                
                with open(outputfile1, "a+") as output:
                        output.write(str(c1[0]))
                        output.write(',')
                        output.write(str(c1[1]))
                        output.write("\t")
                        
                        output.write(str(c2[0]))
                        output.write(',')
                        output.write(str(c2[1]))
                        output.write("\t")
                        
                        output.write(str(c3[0]))
                        output.write(',')
                        output.write(str(c3[1]))
                        output.write("\n")
                        
                        
                with open(outputfile2, "a+") as output2:
                        output2.write(str(d))
                        output2.write("\n")

        
        with open(outputfile2, "a+") as output2:
                        output2.write(str(d))
                        output2.write("\n")      

        print("Check the Output file!")		
	
kMeans(sys.argv[1], sys.argv[2], sys.argv[3])

