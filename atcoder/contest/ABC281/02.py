S = str(input())
start = S[0]
ll = S[1:len(S)-1]
end = S[-1]
#print(start,ll,end)
if len(S)!=8:
    print("No")
elif not (start.isalpha()) or not start.isupper():
    print("No")
elif not (end.isalpha()) or not end.isupper():
    print("No")
elif not ll.isdigit():
    print("No")
elif int(ll)<100000 or int(ll)>999999:
    print("No")
else:
    print("Yes")
