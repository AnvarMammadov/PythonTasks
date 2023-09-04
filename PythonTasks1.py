import random as rm ,string as str      



#1. Ölçüsü 5 olan massivə rəqəmlər daxil edin, daha sonra həmin
#massivi tərsinə ekrana çıxarın.
myList=[]

#Example1
def ReverseList(myList):
    return myList[::-1]
for i in range(5):
    word=input("Deyer daxil edin : ")
    myList.append(word)
print(ReverseList(myList))

#Example2
def ReverseList2(myList):
    myList.reverse()
    return myList
for i in range(5):
    word=input("Deyer daxil edin : ")
    myList.append(word)
print(ReverseList2(myList))






#2. Ölçüsü 20 olan massiv yaradın, random rəqəmlərlə doldurun, indeksi
#cüt olan rəqəmləri ekrana çıxarın.
def CreateList():
    myList=[]
    for i in range(20):
        num=rm.randint(0,100)
        myList.append(num)
    return myList
myList=CreateList()
print("List : ",myList)

#Example1

for i in range(len(myList)):
    if i%2==0 and i!=0:
        print(myList[i],",",end="")
print()

#Example2
for i in range(0,len(myList),2):
    if i!=0:
        print(myList[i],",",end="")
print()







#3. -20 və 20 arasında random rəqəmlərdən ibarət ölçüsü 10 olan massiv
#yaradın. Müsbət ədədlərin ədədi ortasını tapan program yazın.
def PosAvrg():
    myList=[]
    count=0
    total=0
    for i in range(10):
        num=rm.randint(-20,20)
        myList.append(num)
    for i in myList:
        if i>0:
            total+=i
            count+=1
    return myList,total/count
print("List : ",PosAvrg()[0],"\nMusbet ededlerin ededi ortasi : ",PosAvrg()[1])





#4. -5 və 5 arasında random rəqəmlərdən ibarət ölçüsü 20 olan massiv
#yaradın. Mənfilərin, müsbətlərin, və sıfırların sayını tapan program
#yazın.
def CreateList():
    myList=[]
    for i in range(20):
        num=rm.randint(-5,5)
        myList.append(num)
    return myList
def CountNegative(myList):
    count=0
    for i in myList:
        if i<0:
            count+=1
    return count
def CountPositive(myList):
    count=0
    for i in myList:
        if i>0:
            count+=1
    return count
def CountZero(myList):
    count=0
    for i in myList:
        if i==0:
            count+=1
    return count
myList=CreateList()
print("List : ",myList)
print("Menfi ededlerin sayi : ",CountNegative(myList),"\nMusbet ededlerin sayi : ",CountPositive(myList))
print("Sifirlarin sayi : ",CountZero(myList))






#5. Ölçüsü 10 olan massiv yaradın və içərsini random rəqəmlərlə
#doldurun. İndeksi cüt olan ədədlərin cəmini, indeksi tək olan
#ədədlərin isə ədədi ortasını tapın.
def CreateList():
    myList=[]
    for i in range(10):
        num=rm.randint(0,100)
        myList.append(num)
    return myList
def IndexPairNumSum(myList):
    total=0
    for i in range(len(myList)):
        if i%2==0:
            total+=myList[i]
    return total
def IndexOddNumAvg(myList):
    total=count=0
    for i in range(len(myList)):
        if i%2!=0:
            total+=myList[i]
            count+=1
    return total/count
myList=CreateList()
print("List : ",myList)
print("İndeksi cüt olan ədədlərin cəmi : ",IndexPairNumSum(myList))
print("İndeksi tək olan ədədlərin isə ədədi ortası : ",IndexOddNumAvg(myList))





#6. 10 simvoldan ibarət char massivi yaradın (random doldurun- nəzərə
#alın ki char 0-dan 255-ə qədərdir). Neçə hərf, rəqəm və punktuasiya
#simvolu olduğunu hesablayan program yazın.

def CreateList():
    myList=[]
    for i in range(10):
        allSymbol=rm.choice(str.ascii_letters+str.digits+str.punctuation)
        myList.append(allSymbol)
    return myList
def CountLetter(myList):
    count=0
    for i in myList:
        if i in str.ascii_letters:
            count+=1
    return count
def CountDigits(myList):
    count=0
    for i in myList:
        if i in str.digits:
            count+=1
    return count
def CountPunc(myList):
    count=0
    for i in myList:
        if i in str.punctuation:
            count+=1
    return count
myList=CreateList()
print("List : ",myList)
print("Herf sayi : ",CountLetter(myList),"\nReqem sayi : ",CountDigits(myList),"\nPunktuasiya sayi : ",CountPunc(myList))

    
    


#7. Ölçüsü 50 olan massiv yaradın və içərisini random doldurun(1-100) .
#İstifadəçi 1-100 arasında rəqəm daxil edir, və massivdə bu əddədən
#neçə dənə olduğunu hesablayan program yazın.
def CreateList():
    myList=[]
    for i in range(50):
        num=rm.randint(1,100)
        myList.append(num)
    return myList
def CountInputNum(num,myList):
    count=0
    for i in myList:
        if num==i:
            count+=1
    return count
num=int(input("(1 - 100) araliginda eded daxil edin : "))
myList=CreateList()
print("List : ",myList,"\nDaxil etdiyiniz ededin siyadaki sayi : ",CountInputNum(num,myList))

    



#8. 1 və 100 arasında random rəqəmlərdən ibarət ölçüsü 10 olan massiv
#yaradın. 3-ə, 5-ə.7-ə bölünən rəqəmlərin sayını tapın. (ayrı-ayrı)
def CreateList():
    myList=[]
    for i in range(10):
        num=rm.randint(1,100)
        myList.append(num)
    return myList
def DivisibleByThree(myList):
    count=0
    for i in myList:
        if i%3==0:
            count+=1
    return count
def DivisibleByFive(myList):
    count=0
    for i in myList:
        if i%5==0:
            count+=1
    return count
def DivisibleBySeven(myList):
    count=0
    for i in myList:
        if i%7==0:
            count+=1
    return count
myList=CreateList()
print("List : ",myList)
print("3-e bolunenler : ",DivisibleByThree(myList))
print("5-e bolunenler : ",DivisibleByFive(myList))
print("7-e bolunenler : ",DivisibleBySeven(myList))





#9. 1 və 100 arasında random rəqəmlərdən ibarət ölçüsü 10 olan massiv
#yaradın. 3-ə bölünüb 5-ə bölünməyən rəqəmlərin sayını çıxarın. (eyni
#anda həm 3ə bölünsün həm 5-ə bölünməsin)
def CreateList():
    myList=[]
    for i in range(10):
        num=rm.randint(1,100)
        myList.append(num)
    return myList
def myFunc(myList):
    count=0
    for i in myList:
        if i%3==0 and i%5!=0:
            count+=1
    return count
myList=CreateList()
print("List : ",myList,"\n3-ə bölünüb 5-ə bölünməyən rəqəmlərin sayı : ",myFunc(myList))






'''10. -10 və 30 arasında random rəqəmlərdən ibarət ölçüsü 10 olan
massiv yaradın. Birinci mənfi ədəddən sonra gələn bütün rəqəmləri
toplayan program yazın. (1,2,-3,4,5,-6,7 bu halda , 4+5+(-6)+7
olacaq)'''
def CreateList():
    myList=[]
    for i in range(10):
        num=rm.randint(-10,30)
        myList.append(num)
    return myList
def GetSumNegRem(myList):
    total=0
    resultList=[]
    for i in range(0,len(myList)):
        if myList[i]<0:
            resultList=myList[i+1:]
            break
    for i in resultList:
        total+=i
    return total
myList=CreateList()
print("List : ",myList,"\nNetice : ",GetSumNegRem(myList))

            
           
            

#11. -30 və 20 arasında random rəqəmlərdən ibarət ölçüsü 10 olan
#massiv yaradın. Birinci müsbət ədəddən sonra gələn bütün rəqəmləri
#toplayan program yazın.
def CreateList():
    myList=[]
    for i in range(10):
        num=rm.randint(-30,20)
        myList.append(num)
    return myList
def GetSumPosRem(myList):
    total=0
    resultList=[]
    for i in range(len(myList)):
        if myList[i]>0:
            resultList=myList[i+1:]
            break
    for i in resultList:
        total+=i
    return total
myList=CreateList()
print("List : ",myList,"\nNetice : ",GetSumPosRem(myList))





#12. Ölçüsü 20 olan və random rəqəmlərdən ibarət massiv yaradın.
#Massivin maximum və minimum elemtini tapan program yazın.
#(Dəyəri və indeksi qaytarın)
def CreateList():
    myList=[]
    for i in range(20):
        num=rm.randint(-100,100)
        myList.append(num)
    return myList
def MaxNum(myList):
    max=0
    for i in range(len(myList)):
        if myList[i]>=max:
            max=myList[i]
            index=i
    return max ,index
def MinNum(myList):
    min=0
    index=0
    for i in range(len(myList)):
        if myList[i]<=min:
            min=myList[i]
            index=i
    return min , index
myList=CreateList()
MaxNumAndIndexList=MaxNum(myList)
MinNumAndIndexList=MinNum(myList)
print("List : ",myList)
print("\nEn boyuk element : ",MaxNumAndIndexList[0],"\nEn boyuk elementin indeksi : ",MaxNumAndIndexList[1])
print("\nEn kicik element : ",MinNumAndIndexList[0],"\nEn kicik elementin indeksi : ",MinNumAndIndexList[1])





#13. 10 ölçülü kəsr ədədlərdən ibarət massiv yaradın. Neçə rəqəmin
#kəsr hissəsinin olmadığını ekrana çıxaran program yazın. (məs: {12,
#12.5, 10.1, 1,2} kəsr hissəsi olmayan ədədlər 3)
def CreateList():
    myList=[]   
    for i in range(10):
        secimBext=rm.randint(0,1)
        if secimBext==0:
            onluqEded=round(rm.uniform(0,50),2)
            myList.append(onluqEded)
        else:
            tamEded=rm.randint(0,50)
            myList.append(tamEded)
    return myList
def CountInt(myList):
    count=0
    for i in myList:
        if i%1==0:
            count+=1
    return count
myList=CreateList()
print("List : ",myList,"\nTam ededlerin sayi : ",CountInt(myList))





#14. 1 və 200 arasında random rəqəmlərdən ibarət ölçüsü 20 olan
#massiv yaradın. 1 rəqəmli, 2 rəqəmli, 3 rəqəmli ədədlərin faiz nisbəti
#ilə müqayisəsini edən program yazın.
def CreateList():
    myList=[]
    for i in range(20):
        num=rm.randint(1,200)
        myList.append(num)
    return myList
def PercentageNumOfList(myList):
    
    countSingleDigit=0
    countTwoDigit=0
    countThreeDigit=0
    lenNum=len(myList)
    for i in myList:
        count=0
        numI=i
        while numI>0:           
            numI//=10 
            count+=1          
        if count==1:
            countSingleDigit+=1
        elif count==2:
            countTwoDigit+=1
        else:
            countThreeDigit+=1    
    percentageSingleDigit=countSingleDigit*100/lenNum
    percentageTwoDigit=countTwoDigit*100/lenNum
    percentageThreeDigit=countThreeDigit*100/lenNum
    return percentageSingleDigit,percentageTwoDigit,percentageThreeDigit
myList=CreateList()
percentageList=PercentageNumOfList(myList)
print("List : ",myList)
print("Listin",percentageList[0],"% - i bir reqemli ededdir")
print("Listin",percentageList[1],"% - i iki reqemli ededdir")
print("Listin",percentageList[2],"% - i uc reqemli ededdir")


  


#15. 2 və 200 arasında random rəqəmlərdən ibarət ölçüsü 20 olan
#massiv yaradın. Massivdəki bütün sadə rəqəmləri ekrana çıxaran
#program yazın.
def CreateList():
    myList=[]
    for i in range(20):
        num=rm.randint(2,200)
        myList.append(num)
    return myList
def SimpleNumber(myList):
    simpleNumberList=[]
    for i in myList:
        a=1
        count=0
        while a<=i:
            if i%a==0:
                count+=1
            a+=1
        if count==2:
            simpleNumberList.append(i)
    return simpleNumberList
print("List : ",CreateList(),"\nSade ededler : ",SimpleNumber(CreateList()))






#16. Ölçüsü 10 olan massiv yaradın və içərsini random rəqəmlərlə
#doldurun. Massivdəki rəqəmlərin yerlərini tərsinə çevirən program
#yazın. (0-cı indeksi 9-la, 1-i 8-lə və s.)
def CreateList():
    myList=[]
    for i in range(10):
        num=rm.randint(0,100)
        myList.append(num)
    return myList
def ReverseList(myList):
    reverseList=myList[::-1]
    return reverseList
myList=CreateList()
print("List : ",myList,"\nList reverse : ",ReverseList(myList))


            
        


#17. Ölçüsü 10 olan massiv yaradın və içərsini random rəqəmlərlə
#doldurun. Massivdəki qonşu elementlərin yerini dəyişən program               
#yazın.
def CreateList():
    myList=[]
    for i in range(10):
        num=rm.randint(0,100)
        myList.append(num)
    return myList
myList=CreateList()
def ReverseList(myList):
    itemPair=[]
    itemOdd=[]  
    l=len(myList)
    for i in range(l):
        if i%2==0:
            itemPair.append(myList[i])
        else:
            itemOdd.append(myList[i])
    j=b=a=0
    while a<l:
        if a%2==0:
            myList[a]=itemOdd[j]
            j+=1
        else:
            myList[a]=itemPair[b]
            b+=1
        a+=1
    return myList

print("List :  ",myList)
print("Reverse:",ReverseList(myList))

        



#18. Ölçüsü 5 olan iki massiv yaradın A və B . Ölçüsü 10 olan üçüncü
#massiv yaradın C. C massivinə A və B dən sıra ilə elemntləri
#kopyalayın . (məs: С[0]=A[0], С[1]=B[0], C[2]=A[1], C[3]=B[1] və s.)

def CreateList():
    listA=[]
    listB=[]
    listC=[]
    for i in range(5):
        letters=rm.choice(str.ascii_letters)
        listA.append(letters)
    for i in range(5):
        punc=rm.choice(str.punctuation)
        listB.append(punc)
    for i in range(10):
        num=rm.randint(0,1)
        listC.append(num)
    return listA , listB , listC
def ReplaceIndex(listA,listB,listC):
    l=len(listC)
    a=b=j=0
    while a<l:
        if a%2==0:
            listC[a]=listA[b]
            b+=1
        else:
            listC[a]=listB[j]
            j+=1
        a+=1
    return listC
listA=CreateList()[0]
listB=CreateList()[1]
listC=CreateList()[2]
print("List A : ",listA,"\nList B : ",listB,"\nList C : ",ReplaceIndex(listA,listB,listC))





#19. Bir massivi ikinci massivə kopya edən program yazın. Şərt: kopya
#edərkən birinci sıfırdan kiçik elementlər daha sonra 0-lar daha sonra
#0-dan böyük elementləri kopya etməlidir.
def CreateList():
    listA=[]
    for i in range(10):
        num=rm.randint(-50,50)
        listA.append(num)
    return listA
listA=CreateList()


#Example 1


def CopyList(listA):
    listB=[]
    listB=listA.copy()
    listB.sort()
    return listB
print("List A : ",listA,"\nList B : ",CopyList(listA))


#Example 2 


def ListItems(listA):
    negList=[]
    zeroList=[]
    posList=[]
    for i in listA:
        if i<0:
            negList.append(i)
        elif i==0:
            zeroList.append(i)
        else:
            posList.append(i)
    return negList,posList,zeroList
def CopyList2(negList,posList,zeroList):
    listB=[]
    for i in negList:
        listB.append(i)
    for i in zeroList:
        listB.append(i)
    for i in posList:
        listB.append(i)
    return listB
negPosZeroList=ListItems(listA)
negList=negPosZeroList[0]
posList=negPosZeroList[1]
zeroList=negPosZeroList[2]
print("List A : ",listA,"\nList B : ",CopyList2(negList,posList,zeroList))





#20. Ölçüsü 10 olan C massivini , ölçüləri 5 olan A və B massivinə
#kopiya etməlisniz. Şərt => (məs : A[0]=C[0], B[0]=C[1], A[1]=C[2],
#B[1]=C[3] və s. )
def CreateList():
    listC=[]
    for i in range(10):
        num=rm.randint(1,100)
        listC.append(num)
    return listC
def CopyLists(listC):
    listA=[]
    listB=[]
    for i in range(len(listC)):
        if i%2==0:
            listA.append(listC[i])
        else:
            listB.append(listC[i])
    return listA ,listB
listC=CreateList()
listsA_B=CopyLists(listC)
print("List C : ",listC,"\nList A :",listsA_B[0],"\nList B : ",listsA_B[1])

