class Item:
    def set(self):
        f=0
        f1=0
        v=0
        v1=0
        m=0
        m1=0
        s=0
        s1=0
        fo=0
        fo1=0
        i=eval(input("enter 1- fruit. 2-veggies. 3-Meds. 4-Sports wear. 5-food item"))
        while i==5:
            break
        else:
            set()
        if i==1:
            f=int(input('enter price '))
            f1=f-(f//5)
            print(f1)
        elif i==2:
            v=int(input('enter price '))
            v1=v-(v//5)
            print(v1)
        elif i==3: 
            m=int(input('enter price '))
            m1=m-(m//5)
            print(m1)
        elif i==4:
            s=int(input('enter price '))
            s1=s-(s//5)
            print(s1)
        elif i==5:
            fo=int(input('enter price '))
            f01=f0-(f0//5)
            print(f01)
        else:
            print('invailid ')
        t=0
        t=(f-f1)+(v-v1)+(m-m1)+(s-s1)+(fo-fo1)
        print('discount offered is')
        print(t)
a=Item()
a.set()
