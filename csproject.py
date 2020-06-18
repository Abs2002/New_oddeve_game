import random
import time
import mysql.connector as msqc
import hashlib
from datetime import date

mydb1=msqc.connect(user="root", password="123456", database="oddeve_game")
erp1=mydb1.cursor()

def full_logingame(name):
    mydb1 = msqc.connect(user="root", password="123456", database="oddeve_game")
    erp1 = mydb1.cursor()
    try:
        # list of items for choosing randomly
        k = ["Tails", "Heads"]
        w = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



        # function to make the user's input t or h in tails or head
        def thy(f):
            if f == "2":
                return "Tails"
            elif f == "1":
                return "Heads"
            else:
                return "Abe Saaley!"



        a = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
        b = thy(a)
        print(f"$==========$ YOU CHOOSE {b} $==========$")
        print("\n\n")



        # to show loading......
        print("Tossing", end=" ")
        for i in range(0, 5):
            print(".", end=" ")
            time.sleep(1)
        m = random.choice(k)
        print(" ")
        print(f" $$$ {m} $$$")
        print("\n\n")


        # conditions start from winning the toss
        # here if the user wins the toss then
        if m == b:
            print("$==========$ YOU WON THE TOSS $==========$")
            print("\n\n")
            c = input("PRESS [1] FOR BATTING OR PRESS [2] FOR BOWLING : ")
            print("\n\n")
            # this will count user's run
            d = 0
            # this will count computer's run
            r = 0
            # when user chooses to bat


            if c == "1":
                while True:
                    n = random.choice(w)
                    s = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")
                    # if the input is greater than 10 then the value will be rejected


                    if s > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        # show the random value and the user's entered value
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {n} | {s}         $==========$")
                        print("\n\n")


                        if n == s:
                            # if the user's value and random value coincides then user is out
                            print("$==========$ YOU ARE OUT $==========$")
                            break


                        else:
                            # score will add up
                            d += s
                            print(f"$==========$ YOUR SCORE :{d} $==========$")
                            print("\n\n")


                            if d == 50:
                                # mark the runs till 50
                                print("$==========$ YOU MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif d == 100:
                                # mark runs till 100
                                print("$==========$ YOU MADE CENTURY $==========$")
                                print("\n\n")


                            elif d == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)
                print(" ")
                print("\n\n")
                    # print("---------------------------------")


                print(f"$==========$ YOU SCORED {d} RUNS $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER HAS TO SCORE {d} RUNS $==========$")
                print("\n\n")
                time.sleep(2)


                    # now batting of computer starts
                print("$==========$ NOW IT'S COMPUTER'S BATTING $==========$")
                print("\n\n")


                while True:
                    o = random.choice(w)
                    q = int(input("ENTER A NUMBER : "))
                    print("\n\n")


                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {o} | {q}         $==========$")
                        print("\n\n")


                        if o == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            r += o
                            print(f"$==========$ COMPUTER'S SCORE IS {r} RUNS $==========$")
                            print("\n\n")


                            if r == 50:
                                print("$==========$ COMPUTER MADE HALF CENTURY $==========$")
                                print("\n\n")


                            elif r == 100:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif r == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")


                            if r > d:
                                # if computer's run gets above user's run it will break the loop
                                break


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)


                print("\n\n")
                # print("---------------------------------")
                print(f"$==========$ COMPUTER SCORED {r} RUNS $==========$")
                print("\n\n")


                if d > r:
                    # if user's run is more than computer's run
                    print("$==========$ YOU WON THE GAME $==========$")
                    print("\n\n")
                    wa=input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")


                    if wa=="1":
                        erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{d}', 'VICTORY')")
                        mydb1.commit()


                    else:
                        pass


                elif d < r:
                    print("$==========$ COMPUTER WON THE GAME $==========$")
                    print("\n\n")
                    wb=input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")


                    if wb=="1":
                        erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{d}', 'LOSE')")
                        mydb1.commit()


                    else:
                        pass


                elif d == r:
                    # when user's and computer's run is same then
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("$==========$ IT'S TIME FOR SUPEROVER $==========$")
                    print("\n\n")
                    print("$==========$ YOU BAT FIRST $==========$")
                    print("\n\n")
                    # this is the counter
                    ta = 0
                    # this is used to record the runs of user
                    td = 0
                    # this is used to record the number of balls played
                    te = 0


                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOR NUMBER : "))
                        print("\n\n")


                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {tb} | {tc}         $==========$")
                            print("\n\n")


                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                                print("\n\n")
                                te += 1
                                print(f"BALLS PLAYED : {te}")
                                print("\n\n")
                        ta += 1
                    print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                    print("\n\n")
                    print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                    print("\n\n")
                    print("$==========$NOW COMPUTER WILL BAT $==========$")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0


                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENNTER YOUR NUMBER : "))
                        print("\n\n")


                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {tg} | {th}         $==========$")
                            print("\n\n")


                            if tg == th:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED : {tj} $==========$")
                                print("\n\n")


                            if ti > td:
                                break


                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")


                    if ti > td:
                        print("$==========$ COMPUTER WON THE MATCH $==========$")
                        print("\n\n")
                        wc=input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")


                        if wc=="1":
                            erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{d+td}', 'LOSE')")
                            mydb1.commit()


                        else:
                            pass


                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")
                        wd=input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SVE GAME : ")


                        if wd=="1":
                            erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{d+td}', 'VICTORY')")
                            mydb1.commit()


                        else:
                            pass


                    elif td == ti:
                        # if match even ties at this point then it will be decided by toss
                        tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                        print("\n\n")
                        tl = thy(tk)
                        print(f"YOUR CHOICE IS {tl}")
                        print("\n\n")
                        tm = random.choice(k)


                        print("calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)
                        print("")
                        print("\n\n")


                        if tm == tl:
                            print("YOU WON THE MATCH")
                            print("\n\n")
                            we=input("PRESS [1] TO SAVE OR PRESS [2] NOT TO SAVE : ")


                            if we=="1":
                                erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{d+td}', 'VICTORY')")
                                mydb1.commit()


                            else:
                                pass


                        else:
                            print("COMPUTER WON THE MATCH")
                            print("\n\n")
                            wf=input("PRESS [1] TO SAVE OR PRESS [2] NOT TO SAVE : ")


                            if wf=="1":
                                erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{d+td}', 'LOSE')")
                                mydb1.commit()


                            else:
                                pass

            elif c == "2":
                x = 0
                y = 0
                #BOWLING


                while True:
                    l = random.choice(w)
                    q = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")


                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {l} | {q}         $==========$")
                        print("\n\n")


                        if l == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            x += l
                            print(f"$==========$ COMPUTER'S SCORE IS {x} $==========$")
                            print("\n\n")


                            if x == 50:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif x == 100:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif x == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)


                print("")
                print("\n\n")
                print(f"COMPUTER SCORED {x} RUNS")
                print("\n\n")
                print(f"YOU NEED TO SCORE {x} RUNS")
                print("\n\n")
                time.sleep(2)
                print("NOW IT'S YOUR BATTING")
                print("\n\n")


                while True:
                    u = random.choice(w)
                    z = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")


                    if z > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER\n$==========$               {u} | {z}         $==========$")
                        print("\n\n")


                        if u == z:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            y += z
                            print(f"$==========$ YOUR SCORE IS {y} $==========$")
                            print("\n\n")


                            if y == 50:
                                print("$==========$ YOU MADE HALF CENTURY $==========$")
                                print("\n\n")


                            elif y == 100:
                                print("$==========$ YOU MADE CENTURY $==========$")
                                print("\n\n")


                            elif y == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")


                            if y > x:
                                break


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)


                print("")
                print("\n\n")
                print(f"$==========$ YOU SCORED {y} RUNS $==========$")
                print("\n\n")


                if x > y:
                    print("$==========$ COMPUTER WON THE MATCH $==========$")
                    print("\n\n")
                    wa = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                    if wa == "1":
                        erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{y}', 'LOSE')")
                        mydb1.commit()
                    else:
                        pass


                elif x < y:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("\n\n")
                    wb = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                    if wb == "1":
                        erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{y}', 'VICTORY')")
                        mydb1.commit()
                    else:
                        pass


                elif x == y:
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("IT'S TIME FOR SUPEROVER")
                    print("\n\n")
                    print("COMPUTER WILL BAT FIRST")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0


                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")


                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            if tg == th:
                                print("YOU ARE OUT")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED {tj} $==========$")
                                print("\n\n")
                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")
                    print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                    print("\n\n")
                    print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                    print("\n\n")
                    ta = 0
                    td = 0
                    te = 0


                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")


                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                                print("\n\n")
                                te += 1
                                print(f"$==========$ BALLS PLAYED {te} $==========$")
                                print("\n\n")


                                if td > ti:
                                    break
                        ta += 1
                        print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                        print("\n\n")


                        if ti > td:
                            print("$==========$ COMPUTER WON THIS MATCH $==========$")
                            print("\n\n")
                            wC = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                            if wC == "1":
                                erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{y+td}', 'LOSE')")
                                mydb1.commit()
                            else:
                                pass



                        elif ti < td:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")
                            wd = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                            if wd == "1":
                                erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{y+td}', 'VICTORY')")
                                mydb1.commit()
                            else:
                                pass


                        elif td == ti:
                            tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                            print("\n\n")


                            tl = thy(tk)
                            print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                            print("\n\n")
                            tm = random.choice(k)


                            print("Calculating", end=" ")
                            for i in range(0, 5):
                                print(".", end=" ")
                                time.sleep(1)


                            print("")
                            print("\n\n")


                            if tm == tl:
                                print("$==========$ YOU WON THE MATCH $==========$")
                                print("\n\n")
                                we = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                                if we == "1":
                                    erp1.execute(
                                        f"insert into score_table values('{name}', '{date.today()}', '{y+td}', 'VICTORY')")
                                    mydb1.commit()
                                else:
                                    pass


                            else:
                                print("$==========$ COMPUTER WON THE MATCH $==========$")
                                print("\n\n")
                                wf = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                                if wf == "1":
                                    erp1.execute(
                                        f"insert into score_table values('{name}', '{date.today()}', '{y+td}', 'LOSE')")
                                    mydb1.commit()
                                else:
                                    pass

        else:


            print("$==========$ COMPUTER WINS THE TOSS $==========$")
            print("\n\n")
            aa = ["bt", "bw"]
            ab = random.choice(aa)


            if ab == "bt":
                print("$==========$ COMPUTER CHOOSES TO BAT $==========$")
                print("\n\n")
                x = 0
                y = 0


                while True:
                    l = random.choice(w)
                    q = int(input("ENTER YOUR NUMBER :"))
                    print("\n\n")


                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {l} | {q}         $==========$")
                        print("\n\n")


                        if l == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            x += l
                            print(f"$==========$ COMPUTER'S SCORE IS {x} $==========$")
                            print("\n\n")


                            if x == 50:
                                print("$==========$ COMPUTER MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif x == 100:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif x == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)


                print("")
                print("\n\n")
                print(f"$==========$ COMPUTER SCORED {x} RUNS $==========$")
                print("\n\n")
                print(f"$==========$ YOU NEED TO SCORE {x} RUNS $==========$")
                print("\n\n")
                time.sleep(2)
                print("$==========$ NOW IT'S YOUR BATTING $==========$")
                print("\n\n")


                while True:
                    u = random.choice(w)
                    z = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")


                    if z > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {u} | {z}         $==========$")
                        print("\n\n")


                        if u == z:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            y += z
                            print(f"$==========$ YOUR SCORE IS {y} $==========$")
                            print("\n\n")


                            if y == 50:
                                print("$==========$ YOU MADE HALF CENTURY $==========$")
                                print("\n\n")


                            elif y == 100:
                                print("$==========$ YOU MADE CENTURY $==========$")
                                print("\n\n")


                            elif y == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")


                            if y > x:
                                break


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)


                print("")
                print("\n\n")
                print(f"YOU SCORED {y} RUNS")
                print("\n\n")


                if x > y:
                    print("$==========$ COMPUTER WON THIS MATCH $==========$")
                    print("\n\n")
                    wa = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                    if wa == "1":
                        erp1.execute(
                            f"insert into score_table values('{name}', '{date.today()}', '{y}', 'LOSE')")
                        mydb1.commit()
                    else:
                        pass


                elif x < y:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("---------------------------------")
                    wb = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                    if wb == "1":
                        erp1.execute(
                            f"insert into score_table values('{name}', '{date.today()}', '{y}', 'LOSE')")
                        mydb1.commit()
                    else:
                        pass


                elif x == y:
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("$==========$ IT'S TIME FOR SUPEROVER $==========$")
                    print("\n\n")
                    print("$==========$ COMPURTER WILL BAT FIRST $==========$")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0


                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")


                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            if tg == th:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ YOUR SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED {tj} $==========$")
                                print("\n\n")
                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")
                    print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                    print("\n\n")
                    print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                    print("\n\n")
                    ta = 0
                    td = 0
                    te = 0


                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")


                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:


                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"YOUR SCORE IS {td} RUNS")
                                print("\n\n")
                                te += 1
                                print(f" BALLS PLAYED {te}")
                                print("\n\n")


                                if td > ti:
                                    break
                        ta += 1
                        print(f"YOUR FINAL SCORE IS {td}")
                        print("\n\n")


                        if ti > td:
                            print("$==========$ COMPUTER WON THE MATCH $==========$")
                            print("\n\n")
                            wc = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                            if wc == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{y+td}', 'LOSE')")
                                mydb1.commit()
                            else:
                                pass


                        elif ti < td:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")
                            wd = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                            if wd == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{y+td}', 'VICTORY')")
                                mydb1.commit()
                            else:
                                pass


                        elif td == ti:
                            tk = input("PRESS [1] FOR HEADS  OR PRESS [2] FOR TAILS : ")
                            print("\n\n")
                            tl = thy(tk)
                            print(f"YOUR CHOICE IS {tl}")
                            print("\n\n")
                            tm = random.choice(k)


                            print("calculating", end=" ")
                            for i in range(0, 5):
                                print(".", end=" ")
                                time.sleep(1)


                            print("")
                            print("\n\n")


                            if tm == tl:
                                print("$==========$ YOU WON THE MATCH $==========$")
                                print("\n\n")
                                we = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                                if we == "1":
                                    erp1.execute(
                                        f"insert into score_table values('{name}', '{date.today()}', '{y + td}', 'VICTORY')")
                                    mydb1.commit()
                                else:
                                    pass


                            else:
                                print("$==========$ COMPUTER WINS THE MATCH $==========$")
                                print("\n\n")
                                wf = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                                if wf == "1":
                                    erp1.execute(
                                        f"insert into score_table values('{name}', '{date.today()}', '{y + td}', 'LOSE')")
                                    mydb1.commit()
                                else:
                                    pass


            elif ab == "bw":
                print("$==========$ COMPUTER CHOOSES TO BOWL $==========$")
                print("\n\n")
                d = 0
                r = 0


                while True:
                    n = random.choice(w)
                    s = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")


                    if s > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR'S NUMBER $==========$\n$==========$               {n} | {s}         $==========$")
                        print("\n\n")


                        if n == s:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            d += s
                            print(f"$==========$ YOUR SCORE IS {d} $==========$")
                            print("\n\n")


                            if d == 50:
                                print("$==========$ YOU MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif d == 100:
                                print("$==========$ YOU MADE A CENTURY $==========$")
                                print("\n\n")


                            elif d == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)


                print("")
                print("\n\n")
                print(f"$==========$ YOU SCORED {d} RUNS $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER NEEDS TO SCORE {d} RUNS $==========$")
                print("\n\n")
                time.sleep(2)
                print("$==========$ NOW IT'S COMPUTER'S BATTING $==========$")
                print("\n\n")


                while True:
                    o = random.choice(w)
                    q = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")


                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$               {o} | {q}         $==========$")
                        print("\n\n")


                        if o == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            r += o
                            print(f"$==========$ COMPUTER'S SCORE IS {r} $==========$")
                            print("\n\n")


                            if r == 50:
                                print("$==========$ COMPUTER MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif r == 100:
                                print("$==========$ COMPUTER MADE A CENTRUY $==========$")
                                print("\n\n")


                            elif r == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")


                            if r > d:
                                break


                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)


                print("")
                print("\n\n")
                print(f"$==========$ COMPUTER SCORED {r} RUNS $==========$")
                print("\n\n")


                if d > r:
                    print("$==========$ YOU WON THE GAME $==========$")
                    print("\n\n")
                    wa = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                    if wa == "1":
                        erp1.execute(
                            f"insert into score_table values('{name}', '{date.today()}', '{d}', 'VICTORY')")
                        mydb1.commit()
                    else:
                        pass


                elif d < r:
                    print("$==========$ COMPUTER WON THE MATCH $==========$")
                    print("\n\n")
                    wb = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                    if wb == "1":
                        erp1.execute(
                            f"insert into score_table values('{name}', '{date.today()}', '{d}', 'LOSE')")
                        mydb1.commit()
                    else:
                        pass


                elif d == r:
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("$==========$ IT'S TIME FOR SUPER OVER $==========$")
                    print("\n\n")
                    print("$==========$ YOU WILL BAT FIRST $==========$")
                    print("\n\n")
                    ta = 0
                    td = 0
                    te = 0


                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")


                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:


                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                                print("\n\n")
                                te += 1
                                print(f"$==========$ BALLS PLAYED {te} $==========$")
                                print("\n\n")
                        ta += 1
                    print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                    print("\n\n")
                    print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                    print("\n\n")
                    print("NOW IT'S COMPUTER'S TURN TO BAT")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0


                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")


                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:


                            if tg == th:
                                print("$==========$ COMPUTER ARE OUT $==========$")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ COMUTER'S SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED {tj} $==========$")
                                print("\n\n")


                            if ti > td:
                                break


                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")


                    if ti > td:
                        print("$==========$ COMPUTER WON THIS MATCH $==========$")
                        print("\n\n")
                        wc = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                        if wc == "1":
                            erp1.execute(
                                f"insert into score_table values('{name}', '{date.today()}', '{d + td}', 'LOSE')")
                            mydb1.commit()
                        else:
                            pass



                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")
                        wd = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                        if wd == "1":
                            erp1.execute(
                                f"insert into score_table values('{name}', '{date.today()}', '{d + td}', 'VICTORY')")
                            mydb1.commit()
                        else:
                            pass


                    elif td == ti:
                        tk = input("PRESS [1] FOR HEADS OR PRESS [2] FOR TAILS : ")
                        print("\n\n")
                        tl = thy(tk)
                        print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                        print("\n\n")
                        tm = random.choice(k)


                        print("calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)


                        print("")
                        print("\n\n")


                        if tm == tl:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")
                            we = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                            if we == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{d + td}', 'VICTORY')")
                                mydb1.commit()
                            else:
                                pass


                        else:
                            print("$==========$ COMPUTER WINS THE MATCH $==========$")
                            print("\n\n")
                            wf = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                            if wf == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{d + td}', 'LOSE')")
                                mydb1.commit()
                            else:
                                pass
    except:
        print("YOU MADE A MISTAKE")


def full_guestgame():
    try:
        # list of items for choosing randomly
        k = ["Tails", "Heads"]
        w = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        # function to make the user's input t or h in tails or head
        def thy(f):
            if f == "2":
                return "Tails"
            elif f == "1":
                return "Heads"
            else:
                return "Abe Saaley!"

        a = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
        b = thy(a)
        print(f"$==========$ YOU CHOOSE {b} $==========$")
        print("\n\n")

        # to show loading......
        print("Tossing", end=" ")
        for i in range(0, 5):
            print(".", end=" ")
            time.sleep(1)
        m = random.choice(k)
        print(" ")
        print(f" $$$ {m} $$$")
        print("\n\n")

        # conditions start from winning the toss
        # here if the user wins the toss then
        if m == b:
            print("$==========$ YOU WON THE TOSS $==========$")
            print("\n\n")
            c = input("PRESS [1] FOR BATTING OR PRESS [2] FOR BOWLING : ")
            print("\n\n")
            # this will count user's run
            d = 0
            # this will count computer's run
            r = 0
            # when user chooses to bat

            if c == "1":
                while True:
                    n = random.choice(w)
                    s = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")
                    # if the input is greater than 10 then the value will be rejected

                    if s > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        # show the random value and the user's entered value
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {n} | {s} $==========$")
                        print("\n\n")

                        if n == s:
                            # if the user's value and random value coincides then user is out
                            print("$==========$ YOU ARE OUT $==========$")
                            break


                        else:
                            # score will add up
                            d += s
                            print(f"$==========$ YOUR SCORE :{d} $==========$")
                            print("\n\n")

                            if d == 50:
                                # mark the runs till 50
                                print("$==========$ YOU MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif d == 100:
                                # mark runs till 100
                                print("$==========$ YOU MADE CENTURY $==========$")
                                print("\n\n")


                            elif d == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)
                print(" ")
                print("\n\n")
                    # print("---------------------------------")

                print(f"$==========$ YOU SCORED {d} RUNS $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER HAS TO SCORE {d} RUNS $==========$")
                print("\n\n")
                time.sleep(2)

                    # now batting of computer starts
                print("$==========$ NOW IT'S COMPUTER'S BATTING $==========$")
                print("\n\n")

                while True:
                    o = random.choice(w)
                    q = int(input("ENTER A NUMBER : "))
                    print("\n\n")

                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {o} | {q} $==========$")
                        print("\n\n")

                        if o == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            r += o
                            print(f"$==========$ COMPUTER'S SCORE IS {r} RUNS $==========$")
                            print("\n\n")

                            if r == 50:
                                print("$==========$ COMPUTER MADE HALF CENTURY $==========$")
                                print("\n\n")


                            elif r == 100:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif r == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")

                            if r > d:
                                # if computer's run gets above user's run it will break the loop
                                break

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)

                print("\n\n")
                # print("---------------------------------")
                print(f"$==========$ COMPUTER SCORED {r} RUNS $==========$")
                print("\n\n")

                if d > r:
                    # if user's run is more than computer's run
                    print("$==========$ YOU WON THE GAME $==========$")
                    print("\n\n")


                elif d < r:
                    print("$==========$ COMPUTER WON THE GAME $==========$")
                    print("\n\n")

                elif d == r:
                    # when user's and computer's run is same then
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("$==========$ IT'S TIME FOR SUPEROVER $==========$")
                    print("\n\n")
                    print("$==========$ YOU BAT FIRST $==========$")
                    print("\n\n")
                    # this is the counter
                    ta = 0
                    # this is used to record the runs of user
                    td = 0
                    # this is used to record the number of balls played
                    te = 0

                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOR NUMBER : "))
                        print("\n\n")

                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            print(
                                f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tb} | {tc} $==========$")
                            print("\n\n")

                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                                print("\n\n")
                                te += 1
                                print(f"BALLS PLAYED : {te}")
                                print("\n\n")
                        ta += 1
                    print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                    print("\n\n")
                    print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                    print("\n\n")
                    print("$==========$NOW COMPUTER WILL BAT $==========$")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0

                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENNTER YOUR NUMBER : "))
                        print("\n\n")

                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            print(
                                f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tg} | {th} $==========$")
                            print("\n\n")

                            if tg == th:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED : {tj} $==========$")
                                print("\n\n")

                            if ti > td:
                                break

                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")

                    if ti > td:
                        print("$==========$ COMPUTER WON THE MATCH $==========$")
                        print("\n\n")


                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")

                    elif td == ti:
                        # if match even ties at this point then it will be decided by toss
                        tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                        print("\n\n")
                        tl = thy(tk)
                        print(f"YOUR CHOICE IS {tl}")
                        print("\n\n")
                        tm = random.choice(k)

                        print("calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)
                        print("")
                        print("\n\n")

                        if tm == tl:
                            print("YOU WON THE MATCH")
                            print("\n\n")

                        else:
                            print("COMPUTER WON THE MATCH")
                            print("\n\n")

            elif c == "2":
                x = 0
                y = 0
                # BOWLING

                while True:
                    l = random.choice(w)
                    q = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {l} | {q} $==========$")
                        print("\n\n")

                        if l == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            x += l
                            print(f"$==========$ COMPUTER'S SCORE IS {x} $==========$")
                            print("\n\n")

                            if x == 50:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif x == 100:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif x == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)

                print("")
                print("\n\n")
                print(f"COMPUTER SCORED {x} RUNS")
                print("\n\n")
                print(f"YOU NEED TO SCORE {x} RUNS")
                print("\n\n")
                time.sleep(2)
                print("NOW IT'S YOUR BATTING")
                print("\n\n")

                while True:
                    u = random.choice(w)
                    z = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if z > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER\n$==========${u} | {z}$==========$")
                        print("\n\n")

                        if u == z:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            y += z
                            print(f"$==========$ YOUR SCORE IS {y} $==========$")
                            print("\n\n")

                            if y == 50:
                                print("$==========$ YOU MADE HALF CENTURY $==========$")
                                print("\n\n")


                            elif y == 100:
                                print("$==========$ YOU MADE CENTURY $==========$")
                                print("\n\n")


                            elif y == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")

                            if y > x:
                                break

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)

                print("")
                print("\n\n")
                print(f"$==========$ YOU SCORED {y} RUNS $==========$")
                print("\n\n")

                if x > y:
                    print("$==========$ COMPUTER WON THE MATCH $==========$")
                    print("\n\n")


                elif x < y:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("\n\n")


                elif x == y:
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("IT'S TIME FOR SUPEROVER")
                    print("\n\n")
                    print("COMPUTER WILL BAT FIRST")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0

                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")

                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            if tg == th:
                                print("YOU ARE OUT")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED {tj} $==========$")
                                print("\n\n")
                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")
                    print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                    print("\n\n")
                    print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                    print("\n\n")
                    ta = 0
                    td = 0
                    te = 0

                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")

                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                                print("\n\n")
                                te += 1
                                print(f"$==========$ BALLS PLAYED {te} $==========$")
                                print("\n\n")

                                if td > ti:
                                    break
                        ta += 1
                        print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                        print("\n\n")

                        if ti > td:
                            print("$==========$ COMPUTER WON THIS MATCH $==========$")
                            print("\n\n")


                        elif ti < td:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")

                        elif td == ti:
                            tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                            print("\n\n")

                            tl = thy(tk)
                            print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                            print("\n\n")
                            tm = random.choice(k)

                            print("Calculating", end=" ")
                            for i in range(0, 5):
                                print(".", end=" ")
                                time.sleep(1)

                            print("")
                            print("\n\n")

                            if tm == tl:
                                print("$==========$ YOU WON THE MATCH $==========$")
                                print("\n\n")

                            else:
                                print("$==========$ COMPUTER WON THE MATCH $==========$")
                                print("\n\n")
        else:

            print("$==========$ COMPUTER WINS THE TOSS $==========$")
            print("\n\n")
            aa = ["bt", "bw"]
            ab = random.choice(aa)

            if ab == "bt":
                print("$==========$ COMPUTER CHOOSES TO BAT $==========$")
                print("\n\n")
                x = 0
                y = 0

                while True:
                    l = random.choice(w)
                    q = int(input("ENTER YOUR NUMBER :"))
                    print("\n\n")

                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {l} | {q} $==========$")
                        print("\n\n")

                        if l == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            x += l
                            print(f"$==========$ COMPUTER'S SCORE IS {x} $==========$")
                            print("\n\n")

                            if x == 50:
                                print("$==========$ COMPUTER MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif x == 100:
                                print("$==========$ COMPUTER MADE CENTURY $==========$")
                                print("\n\n")


                            elif x == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)

                print("")
                print("\n\n")
                print(f"$==========$ COMPUTER SCORED {x} RUNS $==========$")
                print("\n\n")
                print(f"$==========$ YOU NEED TO SCORE {x} RUNS $==========$")
                print("\n\n")
                time.sleep(2)
                print("$==========$ NOW IT'S YOUR BATTING $==========$")
                print("\n\n")

                while True:
                    u = random.choice(w)
                    z = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if z > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {u} | {z} $==========$")
                        print("\n\n")

                        if u == z:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            y += z
                            print(f"$==========$ YOUR SCORE IS {y} $==========$")
                            print("\n\n")

                            if y == 50:
                                print("$==========$ YOU MADE HALF CENTURY $==========$")
                                print("\n\n")


                            elif y == 100:
                                print("$==========$ YOU MADE CENTURY $==========$")
                                print("\n\n")


                            elif y == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")

                            if y > x:
                                break

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)

                print("")
                print("\n\n")
                print(f"YOU SCORED {y} RUNS")
                print("\n\n")

                if x > y:
                    print("$==========$ COMPUTER WON THIS MATCH $==========$")
                    print("\n\n")


                elif x < y:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("---------------------------------")


                elif x == y:
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("$==========$ IT'S TIME FOR SUPEROVER $==========$")
                    print("\n\n")
                    print("$==========$ COMPURTER WILL BAT FIRST $==========$")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0

                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")

                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:
                            if tg == th:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ YOUR SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED {tj} $==========$")
                                print("\n\n")
                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")
                    print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                    print("\n\n")
                    print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                    print("\n\n")
                    ta = 0
                    td = 0
                    te = 0

                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")

                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:

                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"YOUR SCORE IS {td} RUNS")
                                print("\n\n")
                                te += 1
                                print(f" BALLS PLAYED {te}")
                                print("\n\n")

                                if td > ti:
                                    break
                        ta += 1
                        print(f"YOUR FINAL SCORE IS {td}")
                        print("\n\n")

                        if ti > td:
                            print("$==========$ COMPUTER WON THE MATCH $==========$")
                            print("\n\n")

                        elif ti < td:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")


                        elif td == ti:
                            tk = input("PRESS [1] FOR HEADS  OR PRESS [2] FOR TAILS : ")
                            print("\n\n")
                            tl = thy(tk)
                            print(f"YOUR CHOICE IS {tl}")
                            print("\n\n")
                            tm = random.choice(k)

                            print("calculating", end=" ")
                            for i in range(0, 5):
                                print(".", end=" ")
                                time.sleep(1)

                            print("")
                            print("\n\n")

                            if tm == tl:
                                print("$==========$ YOU WON THE MATCH $==========$")
                                print("\n\n")


                            else:
                                print("$==========$ COMPUTER WINS THE MATCH $==========$")
                                print("\n\n")

            if ab == "bw":
                print("$==========$ COMPUTER CHOOSES TO BOWL $==========$")
                print("\n\n")
                d = 0
                r = 0

                while True:
                    n = random.choice(w)
                    s = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if s > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR'S NUMBER $==========$\n$==========$ {n} | {s} $==========$")
                        print("\n\n")

                        if n == s:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            d += s
                            print(f"$==========$ YOUR SCORE IS {d} $==========$")
                            print("\n\n")

                            if d == 50:
                                print("$==========$ YOU MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif d == 100:
                                print("$==========$ YOU MADE A CENTURY $==========$")
                                print("\n\n")


                            elif d == 0:
                                print("$==========$ BAD LUCK $==========$")
                                print("\n\n")

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)

                print("")
                print("\n\n")
                print(f"$==========$ YOU SCORED {d} RUNS $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER NEEDS TO SCORE {d} RUNS $==========$")
                print("\n\n")
                time.sleep(2)
                print("$==========$ NOW IT'S COMPUTER'S BATTING $==========$")
                print("\n\n")

                while True:
                    o = random.choice(w)
                    q = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if q > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {o} | {q}$==========$")
                        print("\n\n")

                        if o == q:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")
                            break


                        else:
                            r += o
                            print(f"$==========$ COMPUTER'S SCORE IS {r} $==========$")
                            print("\n\n")

                            if r == 50:
                                print("$==========$ COMPUTER MADE A HALF CENTURY $==========$")
                                print("\n\n")


                            elif r == 100:
                                print("$==========$ COMPUTER MADE A CENTRUY $==========$")
                                print("\n\n")


                            elif r == 0:
                                print("$==========$ BAD LUCK OF COMPUTER $==========$")
                                print("\n\n")

                            if r > d:
                                break

                print("Calculating", end=" ")
                for i in range(0, 5):
                    print(".", end=" ")
                    time.sleep(1)

                print("")
                print("\n\n")
                print(f"$==========$ COMPUTER SCORED {r} RUNS $==========$")
                print("\n\n")

                if d > r:
                    print("$==========$ YOU WON THE GAME $==========$")
                    print("\n\n")


                elif d < r:
                    print("$==========$ COMPUTER WON THE MATCH $==========$")
                    print("\n\n")

                elif d == r:
                    print("$==========$ MATCH TIED $==========$")
                    print("\n\n")
                    print("$==========$ IT'S TIME FOR SUPER OVER $==========$")
                    print("\n\n")
                    print("$==========$ YOU WILL BAT FIRST $==========$")
                    print("\n\n")
                    ta = 0
                    td = 0
                    te = 0

                    while ta < 6:
                        tb = random.choice(w)
                        tc = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")

                        if tc > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:

                            if tb == tc:
                                print("$==========$ YOU ARE OUT $==========$")
                                print("\n\n")


                            else:
                                td += tc
                                print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                                print("\n\n")
                                te += 1
                                print(f"$==========$ BALLS PLAYED {te} $==========$")
                                print("\n\n")
                        ta += 1
                    print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                    print("\n\n")
                    print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                    print("\n\n")
                    print("NOW IT'S COMPUTER'S TURN TO BAT")
                    print("\n\n")
                    tf = 0
                    ti = 0
                    tj = 0

                    while tf < 6:
                        tg = random.choice(w)
                        th = int(input("ENTER YOUR NUMBER : "))
                        print("\n\n")

                        if th > 10:
                            print("$==========$ NOT ALLOWED $==========$")


                        else:

                            if tg == th:
                                print("$==========$ COMPUTER ARE OUT $==========$")
                                print("\n\n")


                            else:
                                ti += tg
                                print(f"$==========$ COMUTER'S SCORE IS {ti} RUNS $==========$")
                                print("\n\n")
                                tj += 1
                                print(f"$==========$ BALLS PLAYED {tj} $==========$")
                                print("\n\n")

                            if ti > td:
                                break

                        tf += 1
                    print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                    print("\n\n")

                    if ti > td:
                        print("$==========$ COMPUTER WON THIS MATCH $==========$")
                        print("\n\n")


                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")


                    elif td == ti:
                        tk = input("PRESS [1] FOR HEADS OR PRESS [2] FOR TAILS : ")
                        print("\n\n")
                        tl = thy(tk)
                        print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                        print("\n\n")
                        tm = random.choice(k)

                        print("calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)

                        print("")
                        print("\n\n")

                        if tm == tl:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")


                        else:
                            print("$==========$ COMPUTER WINS THE MATCH $==========$")
                            print("\n\n")
    except:
        print("YOU MADE A MISTAKE")



def small_logingame(name):
    mydb1 = msqc.connect(user="root", password="123456", database="oddeve_game")
    erp1 = mydb1.cursor()
    try:
        # list of items for choosing randomly
        k = ["Tails", "Heads"]
        w = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


        # function to make the user's input t or h in tails or head
        def thy(f):
            if f == "2":
                return "Tails"
            elif f == "1":
                return "Heads"
            else:
                return "Abe Saaley!"


        a = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
        b = thy(a)
        print(f"$==========$ YOU CHOOSE {b} $==========$")
        print("\n\n")

        # to show loading......
        print("Tossing", end=" ")
        for i in range(0, 5):
            print(".", end=" ")
            time.sleep(1)
        m = random.choice(k)
        print(" ")
        print(f" $$$ {m} $$$")
        print("\n\n")
        if m == b:
            print("$==========$ YOU WON THE TOSS $==========$")
            print("\n\n")
            c = input("PRESS [1] FOR BATTING OR PRESS [2] FOR BOWLING : ")
            print("\n\n")
            if c == "1":
                ta = 0
                # this is used to record the runs of user
                td = 0
                # this is used to record the number of balls played
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tb} | {tc} $==========$")
                        print("\n\n")

                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                            print("\n\n")
                            te += 1
                            print(f"BALLS PLAYED : {te}")
                            print("\n\n")
                    ta += 1
                print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                print("\n\n")
                print("$==========$NOW COMPUTER WILL BAT $==========$")
                print("\n\n")
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tg} | {th} $==========$")
                        print("\n\n")

                        if tg == th:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED : {tj} $==========$")
                            print("\n\n")

                        if ti > td:
                            break

                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")

                if ti > td:
                    print("$==========$ COMPUTER WON THE MATCH $==========$")
                    print("\n\n")
                    wc = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                    if wc == "1":
                        erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                        mydb1.commit()


                    else:
                        pass


                elif ti < td:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("\n\n")
                    wd = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SVE GAME : ")

                    if wd == "1":
                        erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                        mydb1.commit()


                    else:
                        pass


                elif td == ti:
                    # if match even ties at this point then it will be decided by toss
                    tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                    print("\n\n")
                    tl = thy(tk)
                    print(f"YOUR CHOICE IS {tl}")
                    print("\n\n")
                    tm = random.choice(k)

                    print("calculating", end=" ")
                    for i in range(0, 5):
                        print(".", end=" ")
                        time.sleep(1)
                    print("")
                    print("\n\n")

                    if tm == tl:
                        print("YOU WON THE MATCH")
                        print("\n\n")
                        we = input("PRESS [1] TO SAVE OR PRESS [2] NOT TO SAVE : ")

                        if we == "1":
                            erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                            mydb1.commit()


                        else:
                            pass


                    else:
                        print("COMPUTER WON THE MATCH")
                        print("\n\n")
                        wf = input("PRESS [1] TO SAVE OR PRESS [2] NOT TO SAVE : ")

                        if wf == "1":
                            erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                            mydb1.commit()


                        else:
                            pass
            elif c == "2":
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        if tg == th:
                            print("YOU ARE OUT")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED {tj} $==========$")
                            print("\n\n")
                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")
                print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                print("\n\n")
                print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                print("\n\n")
                ta = 0
                td = 0
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                            print("\n\n")
                            te += 1
                            print(f"$==========$ BALLS PLAYED {te} $==========$")
                            print("\n\n")

                            if td > ti:
                                break
                    ta += 1
                    print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                    print("\n\n")

                    if ti > td:
                        print("$==========$ COMPUTER WON THIS MATCH $==========$")
                        print("\n\n")
                        wC = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                        if wC == "1":
                            erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                            mydb1.commit()
                        else:
                            pass



                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")
                        wd = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                        if wd == "1":
                            erp1.execute(f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                            mydb1.commit()
                        else:
                            pass


                    elif td == ti:
                        tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                        print("\n\n")

                        tl = thy(tk)
                        print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                        print("\n\n")
                        tm = random.choice(k)

                        print("Calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)

                        print("")
                        print("\n\n")

                        if tm == tl:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")
                            we = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                            if we == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                                mydb1.commit()
                            else:
                                pass


                        else:
                            print("$==========$ COMPUTER WON THE MATCH $==========$")
                            print("\n\n")
                            wf = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")

                            if wf == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                                mydb1.commit()
                            else:
                                pass
        else:

            print("$==========$ COMPUTER WINS THE TOSS $==========$")
            print("\n\n")
            aa = ["bt", "bw"]
            ab = random.choice(aa)

            if ab == "bt":
                print("$==========$ COMPUTER CHOOSES TO BAT $==========$")
                print("\n\n")
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        if tg == th:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ YOUR SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED {tj} $==========$")
                            print("\n\n")
                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")
                print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                print("\n\n")
                print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                print("\n\n")
                ta = 0
                td = 0
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:

                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"YOUR SCORE IS {td} RUNS")
                            print("\n\n")
                            te += 1
                            print(f" BALLS PLAYED {te}")
                            print("\n\n")

                            if td > ti:
                                break
                    ta += 1
                    print(f"YOUR FINAL SCORE IS {td}")
                    print("\n\n")

                    if ti > td:
                        print("$==========$ COMPUTER WON THE MATCH $==========$")
                        print("\n\n")
                        wc = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                        if wc == "1":
                            erp1.execute(
                                f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                            mydb1.commit()
                        else:
                            pass


                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")
                        wd = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                        if wd == "1":
                            erp1.execute(
                                f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                            mydb1.commit()
                        else:
                            pass


                    elif td == ti:
                        tk = input("PRESS [1] FOR HEADS  OR PRESS [2] FOR TAILS : ")
                        print("\n\n")
                        tl = thy(tk)
                        print(f"YOUR CHOICE IS {tl}")
                        print("\n\n")
                        tm = random.choice(k)

                        print("calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)

                        print("")
                        print("\n\n")

                        if tm == tl:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")
                            we = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                            if we == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                                mydb1.commit()
                            else:
                                pass


                        else:
                            print("$==========$ COMPUTER WINS THE MATCH $==========$")
                            print("\n\n")
                            wf = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                            if wf == "1":
                                erp1.execute(
                                    f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                                mydb1.commit()
                            else:
                                pass
            elif ab == "bw":
                ta = 0
                td = 0
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:

                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                            print("\n\n")
                            te += 1
                            print(f"$==========$ BALLS PLAYED {te} $==========$")
                            print("\n\n")
                    ta += 1
                print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                print("\n\n")
                print("NOW IT'S COMPUTER'S TURN TO BAT")
                print("\n\n")
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:

                        if tg == th:
                            print("$==========$ COMPUTER ARE OUT $==========$")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ COMUTER'S SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED {tj} $==========$")
                            print("\n\n")

                        if ti > td:
                            break

                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")

                if ti > td:
                    print("$==========$ COMPUTER WON THIS MATCH $==========$")
                    print("\n\n")
                    wc = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                    if wc == "1":
                        erp1.execute(
                            f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                        mydb1.commit()
                    else:
                        pass



                elif ti < td:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("\n\n")
                    wd = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                    if wd == "1":
                        erp1.execute(
                            f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                        mydb1.commit()
                    else:
                        pass


                elif td == ti:
                    tk = input("PRESS [1] FOR HEADS OR PRESS [2] FOR TAILS : ")
                    print("\n\n")
                    tl = thy(tk)
                    print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                    print("\n\n")
                    tm = random.choice(k)

                    print("calculating", end=" ")
                    for i in range(0, 5):
                        print(".", end=" ")
                        time.sleep(1)

                    print("")
                    print("\n\n")

                    if tm == tl:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")
                        we = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                        if we == "1":
                            erp1.execute(
                                f"insert into score_table values('{name}', '{date.today()}', '{td}', 'VICTORY')")
                            mydb1.commit()
                        else:
                            pass


                    else:
                        print("$==========$ COMPUTER WINS THE MATCH $==========$")
                        print("\n\n")
                        wf = input("PRESS [1] TO SAVE GAME OR PRESS [2] NOT TO SAVE GAME : ")
                        if wf == "1":
                            erp1.execute(
                                f"insert into score_table values('{name}', '{date.today()}', '{td}', 'LOSE')")
                            mydb1.commit()
                        else:
                            pass
    except:
        print("YOU MADE A MISTAKE")



def small_guestgame():
    try:
        # list of items for choosing randomly
        k = ["Tails", "Heads"]
        w = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        # function to make the user's input t or h in tails or head
        def thy(f):
            if f == "2":
                return "Tails"
            elif f == "1":
                return "Heads"
            else:
                return "Abe Saaley!"

        a = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
        b = thy(a)
        print(f"$==========$ YOU CHOOSE {b} $==========$")
        print("\n\n")

        # to show loading......
        print("Tossing", end=" ")
        for i in range(0, 5):
            print(".", end=" ")
            time.sleep(1)
        m = random.choice(k)
        print(" ")
        print(f" $$$ {m} $$$")
        print("\n\n")
        if m == b:
            print("$==========$ YOU WON THE TOSS $==========$")
            print("\n\n")
            c = input("PRESS [1] FOR BATTING OR PRESS [2] FOR BOWLING : ")
            print("\n\n")
            if c == "1":
                ta = 0
                # this is used to record the runs of user
                td = 0
                # this is used to record the number of balls played
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tb} | {tc} $==========$")
                        print("\n\n")

                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                            print("\n\n")
                            te += 1
                            print(f"BALLS PLAYED : {te}")
                            print("\n\n")
                    ta += 1
                print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                print("\n\n")
                print("$==========$NOW COMPUTER WILL BAT $==========$")
                print("\n\n")
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tg} | {th} $==========$")
                        print("\n\n")

                        if tg == th:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED : {tj} $==========$")
                            print("\n\n")

                        if ti > td:
                            break

                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")

                if ti > td:
                    print("$==========$ COMPUTER WON THE MATCH $==========$")
                    print("\n\n")


                elif ti < td:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("\n\n")


                elif td == ti:
                    # if match even ties at this point then it will be decided by toss
                    tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                    print("\n\n")
                    tl = thy(tk)
                    print(f"YOUR CHOICE IS {tl}")
                    print("\n\n")
                    tm = random.choice(k)

                    print("calculating", end=" ")
                    for i in range(0, 5):
                        print(".", end=" ")
                        time.sleep(1)
                    print("")
                    print("\n\n")

                    if tm == tl:
                        print("YOU WON THE MATCH")
                        print("\n\n")

                    else:
                        print("COMPUTER WON THE MATCH")
                        print("\n\n")

            elif c == "2":
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tg} | {th} $==========$")
                        if tg == th:
                            print("YOU ARE OUT")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED {tj} $==========$")
                            print("\n\n")
                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")
                print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                print("\n\n")
                print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                print("\n\n")
                ta = 0
                td = 0
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tb} | {tc} $==========$")
                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                            print("\n\n")
                            te += 1
                            print(f"$==========$ BALLS PLAYED {te} $==========$")
                            print("\n\n")

                            if td > ti:
                                break
                    ta += 1
                    print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                    print("\n\n")

                    if ti > td:
                        print("$==========$ COMPUTER WON THIS MATCH $==========$")
                        print("\n\n")


                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")

                    elif td == ti:
                        tk = input("PRESS [1] FOR HEADS PRESS [2] FOR TAILS : ")
                        print("\n\n")

                        tl = thy(tk)
                        print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                        print("\n\n")
                        tm = random.choice(k)

                        print("Calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)

                        print("")
                        print("\n\n")

                        if tm == tl:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")


                        else:
                            print("$==========$ COMPUTER WON THE MATCH $==========$")
                            print("\n\n")
        else:

            print("$==========$ COMPUTER WINS THE TOSS $==========$")
            print("\n\n")
            aa = ["bt", "bw"]
            ab = random.choice(aa)

            if ab == "bt":
                print("$==========$ COMPUTER CHOOSES TO BAT $==========$")
                print("\n\n")
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tg} | {th} $==========$")
                        if tg == th:
                            print("$==========$ COMPUTER IS OUT $==========$")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ COMPUTER'S SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED {tj} $==========$")
                            print("\n\n")
                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")
                print(f"$==========$ YOU HAVE TO SCORE {ti} RUNS $==========$")
                print("\n\n")
                print("$==========$ NOW IT'S YOUR TURN TO BAT $==========$")
                print("\n\n")
                ta = 0
                td = 0
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:
                        print(
                            f"$==========$ COMPUTER'S NUMBER | YOUR NUMBER $==========$\n$==========$ {tb} | {tc} $==========$")
                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                            print("\n\n")
                            te += 1
                            print(f" BALLS PLAYED {te}")
                            print("\n\n")

                            if td > ti:
                                break
                    ta += 1
                    print(f"YOUR FINAL SCORE IS {td}")
                    print("\n\n")

                    if ti > td:
                        print("$==========$ COMPUTER WON THE MATCH $==========$")
                        print("\n\n")

                    elif ti < td:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")


                    elif td == ti:
                        tk = input("PRESS [1] FOR HEADS  OR PRESS [2] FOR TAILS : ")
                        print("\n\n")
                        tl = thy(tk)
                        print(f"YOUR CHOICE IS {tl}")
                        print("\n\n")
                        tm = random.choice(k)

                        print("calculating", end=" ")
                        for i in range(0, 5):
                            print(".", end=" ")
                            time.sleep(1)

                        print("")
                        print("\n\n")

                        if tm == tl:
                            print("$==========$ YOU WON THE MATCH $==========$")
                            print("\n\n")


                        else:
                            print("$==========$ COMPUTER WINS THE MATCH $==========$")
                            print("\n\n")

            elif ab == "bw":
                ta = 0
                td = 0
                te = 0

                while ta < 6:
                    tb = random.choice(w)
                    tc = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if tc > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:

                        if tb == tc:
                            print("$==========$ YOU ARE OUT $==========$")
                            print("\n\n")


                        else:
                            td += tc
                            print(f"$==========$ YOUR SCORE IS {td} RUNS $==========$")
                            print("\n\n")
                            te += 1
                            print(f"$==========$ BALLS PLAYED {te} $==========$")
                            print("\n\n")
                    ta += 1
                print(f"$==========$ YOUR FINAL SCORE IS {td} $==========$")
                print("\n\n")
                print(f"$==========$ COMPUTER HAS TO SCORE {td} RUNS $==========$")
                print("\n\n")
                print("NOW IT'S COMPUTER'S TURN TO BAT")
                print("\n\n")
                tf = 0
                ti = 0
                tj = 0

                while tf < 6:
                    tg = random.choice(w)
                    th = int(input("ENTER YOUR NUMBER : "))
                    print("\n\n")

                    if th > 10:
                        print("$==========$ NOT ALLOWED $==========$")


                    else:

                        if tg == th:
                            print("$==========$ COMPUTER ARE OUT $==========$")
                            print("\n\n")


                        else:
                            ti += tg
                            print(f"$==========$ COMUTER'S SCORE IS {ti} RUNS $==========$")
                            print("\n\n")
                            tj += 1
                            print(f"$==========$ BALLS PLAYED {tj} $==========$")
                            print("\n\n")

                        if ti > td:
                            break

                    tf += 1
                print(f"$==========$ COMPUTER'S SCORE IS {ti} $==========$")
                print("\n\n")

                if ti > td:
                    print("$==========$ COMPUTER WON THIS MATCH $==========$")
                    print("\n\n")



                elif ti < td:
                    print("$==========$ YOU WON THE MATCH $==========$")
                    print("\n\n")

                elif td == ti:
                    tk = input("PRESS [1] FOR HEADS OR PRESS [2] FOR TAILS : ")
                    print("\n\n")
                    tl = thy(tk)
                    print(f"$==========$ YOUR CHOICE IS {tl} $==========$")
                    print("\n\n")
                    tm = random.choice(k)

                    print("calculating", end=" ")
                    for i in range(0, 5):
                        print(".", end=" ")
                        time.sleep(1)

                    print("")
                    print("\n\n")

                    if tm == tl:
                        print("$==========$ YOU WON THE MATCH $==========$")
                        print("\n\n")


                    else:
                        print("$==========$ COMPUTER WINS THE MATCH $==========$")
                        print("\n\n")
    except:
        print("YOU MADE A MISTAKE")



def table_show():
    try:
        mydb1 = msqc.connect(user="root", password="123456", database="oddeve_game")
        erp1 = mydb1.cursor()
        a=input("ENTER YOUR USERNAME : ")
        b=input("ENTER YOUR PASSWORD : ")
        crypt=hashlib.md5()
        crypt.update(bytes(b, "utf-8"))
        m=crypt.hexdigest()
        # f=str(m.decode("utf-8"))
        erp1.execute(f"select username, password from login_details where username='{a}' and password='{m}'")
        p=erp1.fetchall()
        if len(p)==0:
            print("YOU ENTERED A WRONG USERNAME OR PASSWORD")
        else:
            erp1.execute(f"select *from score_table where name='{a}'")
            for i in erp1:
                print(i)
            erp1.execute(f"select sum(score) from score_table where name='{a}'")
            for i in erp1:
                print(f"total runs scored are : {i}")
            # erp1.execute("select count(match_status) where/ from score_table ")

            # t = 0
            # u = 0
            # erp1.execute(f"select count(match_status) from score_table where name='{a}' and match_status='VICTORY'")
            # for i in erp1:
            #     t += i
            #     for j in str(t):
            #         u += int(j)
            #
            # y = 0
            # p = 0
            # erp1.execute(f"select count(match_status) from score_table where name='{a}'")
            # for i in erp1:
            #     y += i
            #     for j in str(y):
            #         p += int(j)
            #
            # print(f"YOUR WIN PERCENTAGE = {round(u / p * 100, 2)}%")
    except:
        print("YOU MADE A MISTAKE")



def new_user():
    mydb1 = msqc.connect(user="root", password="123456", database="oddeve_game")
    erp1 = mydb1.cursor()
    try:
        print("REGISTER YOURSELF TO RECORD YOUR GAME SCORE AND SHOW IT TO YOUR FRIENDS")
        usr=input("ENTER YOUR USERNAME : ")
        psr=input("ENTER YOUR PASSWORD : ")
        p2sr=input("CONFIRM YOUR PASSWORD : ")
        erp1.execute(f"select username from login_details where username='{usr}'")
        p=erp1.fetchall()
        if psr!=p2sr:
            print("SEEMS LIKE YOUR PASSWORD DOESN'T MATCH")
            return
        elif psr in p:
            print("SAME USERNAME IS THERE IN OUR DATABASE CHANGE YOUR USERNAME")
            return

        else:
            crypt=hashlib.md5()
            crypt.update(bytes(psr, "utf-8"))
            m = crypt.hexdigest()
            # f = str(m.decode("utf-8"))
            erp1.execute(f"insert into login_details(username, password) values('{usr}', '{m}')")
            mydb1.commit()
            print("YOUR ACCOUNT MADE")
    except:
        print("mistake made")



# def masteracess():
#     mydb1 = msqc.connect(user="root", password="123456", database="oddeve_game")
#     erp1 = mydb1.cursor()
#     try:
#         username=input("ENTER YOUR USERNAME : ")
#         password=input("ENTER YOUR PASSWORD : ")
#         pass2opt=input("ENTER YOUR SECOND PASSWORD : ")
#         crypt=hashlib.md5()
#         crypt.update(bytes(password, "utf-8"))
#         m=crypt.hexdigest()
#         # f=str(m.decode("utf-8"))
#
#         crypt.update(bytes(pass2opt, "utf-8"))
#         y=crypt.hexdigest()
#         # g=str(y.decode("utf-8"))
#
#         erp1.execute(f"select *from login_details where username={username} and password={m} and pass2opt={y}")
#         pv=erp1.fetchall()
#         if len(pv)==0:
#             print("WRONG USERNAME, PASSWORD OR SECOND PASSWORD")
#         else:
#             erp1.execute("select *from score_table")
#
#     except:
#         print("MADE A MISTAKE")



if __name__ == '__main__':
    ch=0
    while ch<=4:
        try:
            a=("PRESS [1] TO LOGIN", "PRESS [2] TO PLAY AS GUEST", "PRESS [3] TO MAKE NEW USER",  "PRESS [4] TO EXIT GAME")
            for i in a:
                print(i)
            ch=int(input("ENTER YOUR CHOICE : "))
            if ch==1:
                name=input("ENTER YOUR USERNAME : ")
                erp1.execute(f"select name from score_table where name='{name}'")
                if erp1:
                    cg=0
                    while cg<=4:
                        c=("PRESS [1] TO PLAY FULL GAME", "PRESS [2] TO PLAY 6 BALL GAME", "PRESS [3] TO GET YOUR STATS", "PRESS [4] TO GET BACK TO MAIN MENU")
                        for j in c:
                            print(j)
                        cg=int(input("ENTER YOUR CHOICE : "))
                        if cg==1:
                            full_logingame(name)
                        elif cg==2:
                            small_logingame(name)
                        elif cg==3:
                            table_show()
                        elif cg==4:
                            break
                        else:
                            print("TRY AGAIN")
            elif ch==2:
                cj=0
                while cj<=3:
                    d=("PRESS [1] TO PLAY FULL GAME", "PRESS [2] TO PLAY 6 BALL GAME", "PRESS [3] TO GO BACK TO MAIN MENU")
                    for k in d:
                        print(k)
                    cj=int(input("ENTER YOUR CHOICE :"))
                    if cj==1:
                        full_guestgame()
                    elif cj==2:
                        small_guestgame()
                    elif cj==3:
                        break
                    else:
                        print("TRY AGAIN")
            # elif ch==3:
                # masteracess()
            elif ch==3:
                new_user()
            elif ch==4:
                break
            else:
                print("TRY AGAIN")
        except:
            print("WRONG, TRY AGAIN")



'''
admin password=456@admin
pass2opt=admin@123

anirudh password=abs1729
'''