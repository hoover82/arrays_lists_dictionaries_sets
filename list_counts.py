def counts_of_items ( inbound ): 

#Accepts an array or list, returns a dictionary conprehension of how many times each element appears in the list
# Dan Stober: 2018/02/12

    counting_dict = {}

    for item in inbound:
        if item not in counting_dict:
            counting_dict [item]  = 1

        else:
            counting_dict [item]  += 1

		
    return ( counting_dict )
	

def counts_of_items_sorted ( inbound ): 
#Accepts an array or list, returns a dictionary conprehension of how many times each element appears in the list
#Dictionary returns values sorted. -- This is the same code as above, but with sorting of resutlant dictionary added 
# Dan Stober: 2018/02/12

    counting_dict = {}

    for item in inbound:
        if item not in counting_dict:
            counting_dict [item]  = 1

        else:
            counting_dict [item]  += 1

    #Dictionary of counts is complete, now sort by creating a set of the dictionary keys
    sorted_keys = set()		
    sorted_dict = {}

    for item in counting_dict:
        sorted_keys.add ( item )	

    sorted_keys = sorted(sorted_keys)
		
    for item in sorted_keys:
        sorted_dict [item] = counting_dict [item]

		#    return ( counting_dict )
    return ( sorted_dict )
	
my_list = [1,5,3,2,3,2,4,5,1,5,6,7,1,5]

my_array  = (1,5,3,2,3,2,4,5,1,5,6,7,1,5)

#These are printed out in the order that the key is first encountered in the list or array
print( counts_of_items ( my_list ))
print( counts_of_items ( my_array ))
print ()

#These are printed out with the values sorted in numeric order 
print( counts_of_items_sorted ( my_list ))
print( counts_of_items_sorted ( my_array ))
print ()


my_list = ["SLC","CDG","LHR","HKG","YYZ",'CDG','AMS','SLC','MCO',"SLC",'LAX','PHL',"MEX","YYZ"]
my_array  = ("SLC","CDG","LHR","HKG","YYZ",'CDG','AMS','SLC','MCO',"SLC",'LAX','PHL',"MEX","YYZ")

#These are printed out in the order that the key is first encountered in the list or array
print( counts_of_items ( my_list ))
print( counts_of_items ( my_array ))
print ()

#These are printed out with the values sorted in alphabetical order 
print( counts_of_items_sorted ( my_list ))
print( counts_of_items_sorted ( my_array ))




