#----------------------------------------------------------------------------------------------
#
# Varies functions
#
#LdV2018
#----------------------------------------------------------------------------------------------
import random as rnd
import numpy as np


# Randomize function with a restriction in the order
def resrand(vec,maxseq):
    
    #if maxseq = 3, it check for 4 numbers in an order
    maxseq += 1

    #shuffle untill sequence does not contain more tha maxseq in a row
    passed = False
    while passed == False:
        
        #new assignment each time to get track of order
        newvec=vec[:]
        
        #define as true
        passed = True
    
        #randomize
        r_ind=rnd.sample(range(0, len(newvec)), len(newvec))
        newvec = [newvec[x-1] for x in r_ind]
        
        
        #loop over sequences
        for i in range(maxseq,len(newvec)+1):

            #check if a sequence diff adds up to 0 for example > [4,4,4,4]                    
            if sum(abs(np.diff(newvec[i-maxseq:i])))==0:
                
                #define false and loop continues
                passed = False
    return newvec,r_ind

def makeiti(stimcat,itiminmax):
    
    l_iti = [0] * len(stimcat)
    
    #settings
    v_min = itiminmax[0]
    v_max = itiminmax[1]
    
    #for each category make a list
    v_unique = list(set(stimcat))
    
    #loop over categories    
    for c_cat in v_unique:
        
        #create a fixed list
        temp_l_iti = np.linspace(v_min,v_max,stimcat.count(c_cat))
        temp_l_iti=[int(x) for x in temp_l_iti]
        
        #shuffle for each category
        rnd.shuffle(temp_l_iti)
        
        #get position in orginal list
        pos = [x for x, y in enumerate(stimcat) if y == c_cat]
        
        #loop over itis
        for c_pos in range(len(pos)):
            
            #place iti in final list
            l_iti[pos[c_pos]] = temp_l_iti[c_pos]

    #return randomized ITI list with equal ITIs for all categories
    return l_iti

#print a list to a txt file
def savetxt(thelist,filename):
    
    #thelist=list(map(list, zip(*thelist)))
    
    thefile = open(filename, 'w')
    
    for item in thelist:
        thefile.write("%s\n" % item)
    
    thefile.close()

#read in txt file 
def readtriallist(filename):


    triallist=[ [], [], [], [], [], [], [], [], [], []]
    with open(filename) as f:
        for line in f:
            dat=line.replace("'","").replace("[","").replace("]","").replace("\n","").split(', ')
            for i,val in enumerate(dat):
                triallist[i].append(val)       
    
    return triallist 

#makes a trial list based on n conditions
def make_unique_list(my_dict,reps):
    
    """
    EXAMPLE DICTIONARY ADD INPUT:
    my_dict = {
            'A' : [1,2], 
            'B' : ['a','b'],
            'C' : ['l','m','h'],
            'D' : [0.10, 0.25, 0.50, 1.00, 2.00]}
    
    reps = number of repetitions
    """
    
    #get total number of trials
    n_tot=1
    for val in my_dict:
        n_tot=n_tot*len(my_dict[val])
    
    #make large vec which will be the output
    my_total_list=[]
    
    #copy var for later use and keep original
    new_tot=n_tot
    
    #loop over conditions
    for val in my_dict:

        #account for n of each level
        new_tot=int(new_tot/len(my_dict[val]))
        
        #loop over N within each dictionary entree
        my_list=[]
        for num in my_dict[val]:
            my_list.extend([num]*new_tot)
         
        #combine to match cb length
        temp_list=my_list*int((n_tot/len(my_list)))
        
        #copy in case of repetitions
        temp_list=temp_list*reps
            
        #add to big list
        my_total_list.append(temp_list)

    return my_total_list
