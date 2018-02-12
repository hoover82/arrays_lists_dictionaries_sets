def list_duplicates ( inbound ): 
# Returns duplicate items from a list or array; 
#  Items returned multiple times if multiple appearances 
#  (ie: if item appears three times, it will be returned twice) 
# Always returned as list
# Dan Stober: 2018/02/12

    dups= []
    already_seen = set()

    for item in inbound:
        if item in already_seen:
            dups.append (item)
        else:
            already_seen.add (item)
    return ( dups )

my_list = [1,2,3,2,4,5,1,5,6,7,1,5]

my_array  = (1,2,3,2,4,5,1,5,6,7,1,5)

print ( list_duplicates ( my_list ))
print ( list_duplicates ( my_array ))
