def agregatno_stanje(temperatura):
    if temperatura>0 and temperatura<100:
        return("tecno")
    elif temperatura<=0:
        return("cvrsto")
    else:
        return("gasovito")


def narcissictic(n):
    suma=0
    broj_cifara=len(str(n))
    i=n
    while i>0:
        suma+=(i%10)**broj_cifara
        i=i//10       
    return suma==n


def split_string(string, number):
    list_of_chunks=[]
    for i in range(0,len(string),number):
        list_of_chunks.append(string[i:i+number])
    return list_of_chunks


print(narcissictic(153))
print(split_string("danas polažemo test", 5))
print(split_string("kurs web program.", 6))
print(split_string("da",7))
print(agregatno_stanje(100))
print(agregatno_stanje(0))
print(agregatno_stanje(10))
print(agregatno_stanje(-15))
print(agregatno_stanje(105))


