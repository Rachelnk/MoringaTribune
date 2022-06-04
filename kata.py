# def find_needle(haystack):
    # loop throught the haystack and check if any items matches needle
    # for i in haystack:
        # if i == "needle":
            # return "found the needle at position {}" .format(haystack.index("needle"))

# x="abcdef"
# i="e"
# while i in x [: -1]:
#     print(i, end =" ")
#     break
# hours=[8,8,11,10,9]
# list comprehension
# overtime=[h-8 for h in hours]  
# print(overtime)



# haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]

def find_needle(haystack):
    index_no = haystack.index('needle')
    return f"found the needle at position {index_no}"
    print(find_needle(haystack))