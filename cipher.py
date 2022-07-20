# # Encryption
# p = str(input("Enter your plain message: "))
# key = int(input("Enter Key:"))
# arr = list(p)
# result = []
# final_output = ""
# for i in range(len(arr)):
#     if(ord(arr[i])>=65 and ord(arr[i])<=90):
#         mid_value = ((ord(arr[i])-65)+ key)%26
#         mid_final_value = mid_value +65
#     else:
#         mid_value = ((ord(arr[i]))-97 + key)%26
#         mid_final_value = mid_value + 97
#
#     result.append(chr(mid_final_value))
#
# for i in result:
#     final_output += i
#
# ot = print(final_output)
# print("Encrypted Message is" + ot)

#Decryption
decode_p = str(input("Enter your plain message: "))
key = int(input("Enter Key:"))
decode_arr = list(decode_p)
decode_result = []
decode_final_output = ""
for i in range(len(decode_arr)):
    if(ord(decode_arr[i])>=65 and ord(decode_arr[i])<=90):
        mid_value = ((ord(decode_arr[i])-65)- key)%26
        mid_final_value = mid_value +65
    else:
        mid_value = ((ord(decode_arr[i]))-97 - key)%26
        mid_final_value = mid_value + 97

    decode_result.append(chr(mid_final_value))

for i in decode_result:
    decode_final_output += i

print(decode_final_output)

