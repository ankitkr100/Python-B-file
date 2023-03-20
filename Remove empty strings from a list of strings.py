#str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#res_list = []
#for s in str_list:
#	#check for non empty string
#
#	if s:
#		res_list.append(s)
#print(res_list)

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_str_list = list(filter(None, str_list))
print("After removing empty strings")
print(new_str_list)