while True:
    box = list(map(int,input().split()))
    if box==[0,0,0,0,0,0]:
        break
    else:
        n=box[5]
        n+=box[5-1]
        n+=box[4-1]
        n+=box[3-1] // 4
        box3=box[3-1] % 4

        if box[1-1]-box[5-1]*11 <= 0:
            box1=0
        else:
            box1=box[1-1]-box[5-1]*11

        if box[2-1]-box[4-1]*5 <= 0:
            box2=0
            if box1-(box[4-1]*5-box[2-1])*4 >= 0:
                box1 -= (box[4-1]*5-box[2-1])*4
            else:
                box1=0
        else:
            box2=box[2-1]-box[4-1]*5

        if box3 >0 :
            n+=1
            box2used = 0
            if box2 >0 :
                if box2-5*(box3==1)+3*(box3==2)+1*(box3==3) <= 0:
                    box2used=box2
                    box2=0
                else:
                    box2used=5*(box3==1)+3*(box3==2)+1*(box3==3)
                    box2 -= 5*(box3==1)+3*(box3==2)+1*(box3==3)
            if box1 >0 :
                if box1-(36-9*box3-4*box2used) <= 0:
                    box1=0
                else:
                    box1 -= (36-9*box3-4*box2used)

        if box2 >0 :
            n+=box2//9+(box2%9!=0)
            if box1 >0 :
                if box1-(36-4*(box2%9)) <= 0:
                    box1=0
                else:
                    box1 -= (36-4*(box2%9))
                    n+=box1//36+(box1%36!=0)
        else:
            if box1 >0 :
                n+=box1//36+(box1%36!=0)
        print(n)





