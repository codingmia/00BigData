#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------
total		   = 0
print_total	   = 0
prev_word          = None       

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list

    #note: for simple debugging use print statements, ie:  
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
    
    if prev_word != curr_word:
        if print_total == 1:		#ready to print previous word
	    print( '%s %s' % (prev_word, total) ) 
	    print_total = 0
	    total = 0
	if value_in != 'ABC': 		#it is a count which we can use
	    tmp = int(value_in)
	    total = tmp		#count for current word
    else:			#accumulte count
	if value_in != 'ABC':
	    total   += int(value_in)         #add to running total when not AVC
    	if value_in == 'ABC':		
	    print_total = 1	#get ready for next show
    prev_word = curr_word
