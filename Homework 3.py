user_str = 'aabbcc'
sub_str1 = user_str[2::1]
sub_str2 = user_str[1:4]
sub_str3 = user_str [1: :2]
sub_str4 = user_str[:-2]


print(sub_str4)
index_int  = 0
for index in range (0, len(user_str)):
    print(user_str[index].upper())