# 1. Ekrana istifadəçinin daxil etdiyi say qədər, ulduzlardan üfiqi xətt
# çıxaran proqram yazın.
count=int(input("Ulduzlarin sayini daxil edin :")) 
for i in range(count):
    print("*",end="")




#2. Ekrana, 1-50 aralığındakı rəqəmlərdən ancaq cüt olanları çıxaran
#proqram yazın.
for i in range(1,50):
    if i%2==0:
        print(i)




#3. İstifadəçinin daxil etdiyi aralıqda (məs 10 və 30) cüt rəqəmlərin cəmini
#tək rəqəmlərin hasilini hesablayan proqram yazın.
start=int(input("Enter start :"))
end=int(input("Enter end :"))
total=0
hasil=1
for i  in range(start,end):
    if i%2==0:
        total+=i
    else:
        hasil*=i
print("Cut ededlerin cemi :",total)
print("Tek ededlerin hasili :",hasil)




#4. 1-100 diapazonunda 3-ə bölünüən bütün ədədləri ekrana çıxaran
#proqram yazın.
for i in range(1,100):
    if i%3==0:
        print(i)
    



#5. Ədədin faktorialını tapan proqram yazın. (Məsələn (! - faktorial
#işarəsidir), 5! = 1*2*3*4*5)
num=int(input("Ededi daxil edin :"))
fc=1
for i in range(1,num+1):
    fc*=i
print(fc)





#6. Ədədin üstünü hesablayan proqram yazın (istifadəçi iki ədəd daxil
#edəcək əsas və üst məs. 2 və 3 cavab 8 alınmalıdır)
esasNum=int(input("Ededi daxil edin :"))
ustNum=int(input("Ededin ustunu daxil edin:"))
result=1
for i in range(0,ustNum):
    result*=esasNum
print(result)




#7. İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, onun rəqəmlərinin
#sayını və onların cəmini hesablayan proqram yazın.
num=int(input("Eded daxil edin :"))
total=counter=0

for i in range(num):
    if num>0:
        dg=num%10
        total+=dg
        num//=10
        counter+=1
print(total)
print(counter)




#8. İstifadəçi istənilən sayda rəqəmli ədəd daxil edir, ədədi əksinə çevirən
#proqram yazın.
num=int(input("Eded daxil edin :"))
reverse=""
for i in range(num):
    if num>0:
        dg=num%10
        reverse+=str(dg)
        num//=10
print(reverse)




#9.İstifadəçi tam ədəd daxil edir, bu ədədin qalıqsız bölündüyü bütün
#rəqəmləri ekrana çıxaran proqram yazın.
num=int(input("Eded daxil edin :"))
realNum=num
for i in range(num):
    if num>0:
        dg=num%10
        if realNum%dg==0:
            print("Ededin qaliqsiz bolunduyu reqemleri :",dg)
        num//=10





#10.İstifadəçi tam ədəd daxil edir , bu ədədin sadə olub olmamasını
#tapan proqram yazın.
num=int(input("Eded daxil edin :"))
counter=0
if num<=0:
    print("Daxil etdiyiniz eded natural eded deyil!!!\a")
for i in range(1,num+1):
    if num%i==0:
        counter+=1
if counter==1:
    print("Daxil etdiyiniz eded ne sade ne de murekkeb ededdir")
elif counter==2:
    print("Daxil etdiyiniz eded sade ededdir")
elif counter>2 and num>0:
    print("Daxil etdiyiniz eded murekkeb ededdir")





#11. Daxil edilmiş ədəddə iki ard arda rəqəmin olub olmamasını
#yoxlayan proqram yazın.
num=int(input("Eded daxil edin :"))
sonReqem=num%10
num//=10
reqemYoxla=0
for i in range(num):
    if num>0:
        dg=num%10
        if sonReqem==dg:
            reqemYoxla=1
            break

        sonReqem=dg
        num//=10
if reqemYoxla==1:
    print("Iki ve daha cox ard arda reqem var")
else:
    print("Ard arda reqem yoxdur")





#12. İstifadəçi ədəd daxil edir, bu ədədin rəqəmlərinin artan ardıcıllıqla
# olub olmamasını yoxlayan proqram yazın. (12299 artan ardıcıllıq,
# 122044 artan ardıcıllıq deyil).
num=int(input("Eded daxil edin :"))
sonReqem=num%10
num//=10
reqemYoxla=0
for i in range(num):
    if num>0:
        dg=num%10
        if sonReqem<dg:
            reqemYoxla=1
            break
        else:
            reqemYoxla=0
        sonReqem=dg
        num//=10
if reqemYoxla==0:
    print("Ededin reqemleri artan ardicilliqla duzulmusdur")
else:
    print("Azalan ardicilliq!!!")





# #13.“Ədədi tap” oyununu yazın. İstifadəçi ağlında bir rəqəm tutacaq, və
#yazdığınız proqram həmin ədədi bir neçə dəfə təxmin edərək
#tapmalıdır.
import random
numComp=random.randint(0,9)
bll=False
print("Ədədi tap oyunu.Proqramın hansı rəqəmi seçdiyini tapın.")
araliq=int(input("Ədədi neçə cəhdə tapmaq istədiyinizi daxil edin :"))
for i in range(0,araliq):
    numUser=int(input("Ededi daxil edin :"))
    if numUser==numComp:
        print("Ededi texmin etmeyi bacardiniz")
        br=True
        break
    else:
        print("Yanlisdir")
if bll==False:
    print("Haqqiniz bitdi . Ededi texmin etmeyi bacarmadiniz :/")
    






#13.1 “Ədədi tap” oyununu yazın. İstifadəçi ağlında bir rəqəm tutacaq, və
#yazdığınız proqram həmin ədədi bir neçə dəfə təxmin edərək
#tapmalıdır.
import random
counter=0
secimCehd=""
maxN=9
minN=0
numTexmin=random.randint(0,4)
print("\t\t\tƏdədi tap oyununa xoş gəlmisiniz (:\n\t\tAğlınızda tutduğunuz rəqəmi maksimum 3 cehdde tapmağa çalışacağıq.\n\n")
print("Diqqət!!! Əgər təxmin etdiyimiz ədəd doğrudursa bizə \"bəli\" cavabını , yanlışdırsa \"xeyr\" cavabını daxil edin\n")
num=int(input("aglinizdaki ededi daxil edin :"))
for i in range(0,4):
    print("Ağlınızda tutduğunuz eded-->",numTexmin)
    secimCehd=input("Təxmin doğrudur? 1)Bəli   2)Xeyr->( '1' və yaxud '2' daxil edin ) :")
    if secimCehd=="1":
        print("Tapıldı")
        break
    elif secimCehd=="2":                           
            if numTexmin>num:
                maxN=num
                numTexmin=random.randint(minN,num)
            elif numTexmin<num:
                minN=num
                numTexmin=random.randint(num,maxN)
            counter+=1   
            if counter==4:
                print(":/")
