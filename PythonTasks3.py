#1. Ədədin kubunu qaytaran funksiya yazın
def NumCube(num):
    num**=3
    return num  

print(NumCube(5))




#2. İki ədəddən böyüyünü tapan funksiya yazın.
def GetCompared(num1,num2):
    if num1>num2:
        return num1
    elif num1==num2:
        return num1,num2
    else:
        return num2

n1=int(input("First number :"))
n2=int(input("Second number :"))
print(GetCompared(n1,n2))




#3. Ədəd müsbətdirsə doğru, mənfidirsə yanlış qaytaran funksiya yazın.
def IsPositive(num):
    if num>0:
        return True
    elif num==0:
        return num
    else:
        return False

print(IsPositive(-10))
print(IsPositive(10))
print(IsPositive(0))




#4. İstifadəçinin seçimindən asılı olaraq Toplama, Çıxma , Vurma, Bölmə
#funksiyalarından birini çağıran , funksiya yazın.

def Toplama(num1,num2):
    result=num1+num2
    return result
def Cixma(num1,num2):
    result=num1-num2
    return result
def Bolme(num1,num2):
    if num2==0:
        print("Sifira bolme yoxdur")
    else:
        result=num1/num2
        return result
def Vurma(num1,num2):
    result=num1*num2
    return result
def Emeliyyat(secim):
    if secim=="+":
        # print(Toplama(num1,num2))
        return Toplama(num1,num2)
    elif secim=="-":
        return Cixma(num1,num2)
    elif secim=="*":
        return Vurma(num1,num2)
    elif secim=="/":
        return Bolme(num1,num2)
    else:
        print("Istediyiniz secim  ucun emeliyyat tapilmadi!!!")
num1=int(input("1-ci ededi daxil edin :"))
num2=int(input("2-ci ededi daxil edin :"))
secim=input("Ededler uzerinde etmek istediyiniz emeliyyati secin ('+' , '-' , '*' , '/') : ")
print(Emeliyyat(secim))




#5. Parametr kimi tərfinin uzunluğunu qəbul edən , və ekrana həmin
#ölçüdə kvadrat çıxaran funksiya yazın.
def Kvadrat(teref):   
    i=0
    while i<teref:
        print(2*teref*"*") 
        i+=1
    # ulduzlar alt alta yazilanda arasinda elave bosluqlar olur
    # deye  kvadrat alinmirdi ,ona gore de hesablamada 2-ye vurdum
Kvadrat(8)





#6. Göndərilən rəqəmin sadə olub olmadığını yoxlayan funksiya yazın.
def IsSimple(num):
    count=0
    i=1
    while i<num:
        if num%i==0:
            count+=1
        i+=1
    if count==1:
        return True
    else: 
        return False
print(IsSimple(13))





#7. Ədədin faktorialını qaytaran funksiya yazın.
def Factorial(num):
    i=1
    fc=1
    while i<=num:
        fc*=i
        i+=1
    return fc
print(Factorial(5))





#8. İki parametr qəbul edən : Üst və Qüvvət , və ədədin qüvvətini
#qaytaran funksiya yazın.
def PowerOfNumber(num,power):
    num**=power
    return num
print(PowerOfNumber(2,3))




#9. Funksiya 2 ədəd qəbul edir və bunlar arasındakı bütün ədədləri
#toplayıb qaytarır.
def IkiEdedArasindaToplam(num1,num2):
    total=0
    while num1<=num2: #axirinci eded daxil olmaqla 
        total+=num1
        num1+=1
    return total
print(IkiEdedArasindaToplam(1,10))

