#Liron Binyamin 
#******************************
import time
import random
#שלב 1 - ניהול המירוץ
def HorseRace(name1,name2,range1):
    space=lambda y:y*60       #להדפסת הפרדה
    start=range1//20
    end=range1//10                   #להוספת מספר רנדומלי כל פעם
    sum1,sum2=0,0            #לחישוב התקדמות הסוסים 
    while sum1<range1:
        rnd1 = random.randint(start,end) #הדפסת התקדמות של סוס 1
        rnd2 = random.randint(start,end) #הדפסת התקדמות של סוס 2
        sum1+=rnd1
        sum2+=rnd2
        print('Horse:{} range:{}   vs   Horse:{} range:{}'.format(name1[0],sum1,name2[0],sum2))
        time.sleep (0.2)
    print (space('-'))
    if sum1>sum2: return name1
    else: return name2

#שלב 2 - יצירת
#שלב 2 - יצירת רשימת סוסים
def ChoiceHorses(horses_list, number_horses_default=4):
    new_horses_list=[]     #רשימה חדשה 
    List=[]         #שמירת האינדקס ברשימה לבדיקה 
    for i in range (number_horses_default):
        save_random = random.randrange(0,len(horses_list)) #משתנה לשמירת מספר אקראי
        while save_random in List:   # אם יש כבר את המספר ברשימה
            save_random = random.randrange(0,len(horses_list))
        new_horses_list.append(horses_list[save_random])
        List.append(save_random)  # הוספת המספר לרשימה לצורך בדיקה
    return new_horses_list

#שלב 3- הרצת תחרות
def HorseRacing(horses_list, name='Champions League', range1=500, number_horses_default=2**2):
    horses_list_for_competition = []  # רשימה לשמירת סוסים לתחרות
    horses_list_for_competition.extend(ChoiceHorses(horses_list, number_horses_default))  # הוספת סוסים לרשימה
    winner = [] #  רשימת מנצחים
    print(horses_list_for_competition)
    for horse in range(0, len(horses_list_for_competition), 2):    #ריצה על רשימת סוסים לתחרות
        name1 = horses_list_for_competition[horse]   
        name2 = horses_list_for_competition[horse + 1] 
        name = HorseRace(name1, name2,range1)  # שם של סוס מנצח מבין ה2 שנשלחו
        if name == name1: loser = name2   
        else: loser = name1             
        name[2] += 1   #ניצחון במירוץ
        name[3] += 5   # נקודות במירוץ
        print('{} came in first place , \n{} came in second'.format(name[0], loser[0]))
        print('*' * 60)
        winner.append(name)    # winner תוסיף את השם המנצח לרשימת
    while len(winner) > 1:   #יותר משם אחד winner כל עוד יש ברשימת
        winner_horse = HorseRace(winner[0], winner[1],range1)  #תריץ תחרות בין הסוס באינקדס 0 לסוס באינדקס 1
        horse_one=winner[0]
        horse_two=winner[1]
        if winner_horse == horse_one:   # אם סוס 1 ניצח
            horse_one[2]+=1
            horse_one[3]+=5
            loser = horse_two
            print('final\n{} came in first place , \n{} came in second'.format(horse_one[0], horse_two[0]))
            print('*' * 60)
        else:                          # אם סוס 2 ניצח
            horse_two[2]+=1
            horse_two[3]+=5
            loser = horse_one
            print('final\n{} came in first place , \n{} came in second'.format(horse_two[0], horse_one[0]))
            print('*' * 60)
        winner.remove(horse_one)
        winner.remove(horse_two)
        winner.insert(len(winner), winner_horse)   # להוסיף את הסוס המנצח לסוף הרשימה
        horse_one[3]+=5
    print('The winner is:{}'.format(winner[0]))

#שלב 4- טבלת סוסים
def printList(horses_list,num=0):
    def table(horses_list,i,num):
        while i<num:
            info=horses_list[i]
            name=info[0]
            age=info[1]
            wins=info[2]
            Score=info[3]
            print ( "{:<12s} {:<5d} {:<1d} {:>8d}".format(name,age,wins,Score))
            i+=1

    print ( "{:<12s} {:<5s} {:<1s} {:>8s}".format('name','age','wins','Score'))
    i=0  # בשביל ריצה באינדקסים
    if num==0:
        num=len(horses_list)  #להדפסת כל הרשימה 
        table(horses_list,i,num)
    elif num<0:
        horses_list.reverse()
        num=abs(num)      #ערך מוחלט
        table(horses_list,i,num)
    else:table(horses_list,i,num)
    
#שלב 5 - מיון טבלה
def sortHorses (horses_list,choice='points',order=2):
    if choice=='points':i=3
    elif choice=='wins':i=2
    elif choice=='age':i=1
    func=lambda x:x[i]
    
    for _ in range(len(horses_list)):
        horses_list.sort(key=func)   # ממיין את הרשימה לפי אינדקס שנשמר 
        if order ==2: horses_list.reverse()
    return printList(horses_list,num=0)

#שלב 6- הוספת סוס
def addHorse (horses_list):
    name=input("name: ")
    age=int(input("age: "))
    wins=int(input("wins: "))
    points= int(input("points: "))
    new_horse=[name,age,wins,points] # הוספת כל הנתונים לרשימה חדשה
    horses_list.append(new_horse)
    return(sortHorses(horses_list,choice='points',order=2))
    
#שלב 7- מחיקת סוס
def removeHorse (horses_list):
    sortHorses(horses_list,choice='points',order=2)
    last_horse=horses_list[len(horses_list)-1]  #הגדרת משתנה שמקבל את הסוס במקום האחרון
    horses_list.remove(last_horse)
    return printList(horses_list,num=0)

#שלב 8- תפריט
def menu(horses_list):
    ch=0
    space=lambda x:x*40
    while ch!=6:
        print (space('*'))
        print ('-- Menu --')
        print('[1]Print horses list.')
        print('[2]Sort horses list.')
        print('[3]Add horse.')
        print('[4]Remove horse.')
        print('[5]Horse Racing.')
        print('[6]Exit')
        print (space('-'))
        ch=int(input('Enter your choice:'))
        if ch==6:print('End')
        elif ch>6 or ch<1:print('There is no such option. Please select a number from 1 to 6.')
        elif ch==1:
            num=input('For the entire list, select 0 key or press "Enter".\n* Descending order - press negative number.\n* Escending order - press positive number\n')
            if num=="": printList(horses_list)
            else:printList(horses_list,int(num))
        elif ch==2:
            choice=input('Choose according to which figure to sort the table - age / wins / points:')
            order=input('To view the list in ascending order, press 1,\nin descending order, press 2 or press "Enter".:')
            if choice=="":sortHorses(horses_list,'points',int(order))
            elif order=="":sortHorses(horses_list,choice)
            elif choice=="" and order=="":sortHorses(horses_list)
            else:sortHorses(horses_list,choice,int(order))
        elif ch==3:addHorse (horses_list) 
        elif ch==4:removeHorse(horses_list)
        elif ch==5:
            name='Champions League'
            number_horses_default=input('Select the number of horses for the race - 4/8: ')
            range1=input('Enter the length of the race (default is 500 meters): ')
            if number_horses_default=="":HorseRacing(horses_list,name,int(range1))
            elif range1=="":HorseRacing(horses_list,name,500,int(number_horses_default))
            elif number_horses_default=="" and range1=="":HorseRacing(horses_list)
            else:HorseRacing(horses_list,name,int(range1),int(number_horses_default))
#-*-*-*-*-*-*-*-*-*-*-*-*-*-Main-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
horses_list=[["Ziv",3,5,25],["Jon",9,2,10],
             ["Khal",5,4,20],["Drogo",5,5,25],
             ["Star",7,3,15],["Rio",4,6,30],
             ["Sansa",6,2,10],["Arya",7,1,5]]

(menu(horses_list))
