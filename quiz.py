import tkinter
import random
from tkinter import*
questions=[
"How many keywords are there in c Programming language ?",
"Which of the following functions take a console input in python ?",
"In a relational schema, each tuple is divided into fields called ?",
"DFD stands for ?",
"How structures and classes in C++ differ ?",
"What does polymorphism in OOPs mean ?",
"Which concept allows you to reuse the written code?",
"How access specifiers in Class helps in Abstraction?",
" C++ is ______________?",
" What does modularity mean?",


]
answer_choice=[
["32","23","33","43",],
["input()","get()","gets()","scan()",],
["Relationless","Domian","Quieries","Alll of the above",],
["(A)DataFlowDocument","(B)DataFileDiagram","(C)DataFlowDiagram","(D) Non of the above",],
["(a) In Structures, members are public by default whereas, in Classes, they are private by default","(b) In Structures, members are private by default whereas, in Classes, they are public by default","(c) Structures by default hide every member whereas classes do not","(d) Structures cannot have private members whereas classes can have"],
["(a) Concept of allowing overiding of functions","(b) Concept of hiding data","(c) Concept of keeping things in differnt modules/files","(d) Concept of wrapping things into a single unit"],
["(a) Encapsulation","(b) Abstraction","(c) Inheritance","(d) Polymorphism",],
["(a) They does not helps in any way","(b) They allows us to show only required things to outer world","(c) They help in keeping things together","(d) Abstraction concept is not used in classes"],
["(a) procedural programming language","(b) object oriented programming language","(c) functional programming language","(d) both procedural and object oriented programming language",],
["(a) Hiding part of program","(b) Subdividing program into small independent parts","(c)Overriding parts of program","(d) Wrapping things into single unit"],

]
answers=[0,0,2,0,0,0,2,1,3,1]
user_ans=[]

indexex=[]
def gen():
    global indexex
    while(len(indexex)<5):
        x = random.randint(0,9)
        if x in indexex:
            continue
        else:
            indexex.append(x)
    print(indexex)
def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage=Label(
        root,
        background="#ffffff",
        border=0
    )
    labelimage.pack(pady=(50,30))
    labelresulttext=Label(
        root,
        font=("Consolas",20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img=PhotoImage(file="exee.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="Excellent!!")
    elif(score>=10 and score< 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You can be Good!!")
    else:
        img = PhotoImage(file="sad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You should work Hard!!")


def calc():
    global indexex,answer_choice,answers
    x=0
    score=0
    for i in indexex:
        if user_ans[x]==answers[i]:
            score=score+5
        x+=1
    print(score)
    showresult(score)



ques=1
def selected():
    global radiovar,user_ans
    global lblquestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_ans.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblquestion.config(text=questions[indexex[ques]])
        r1['text']=answer_choice[indexex[ques]][0]
        r2['text'] = answer_choice[indexex[ques]][1]
        r3['text'] = answer_choice[indexex[ques]][2]
        r4['text'] = answer_choice[indexex[ques]][3]
        ques+=1
    else:
        print(indexex)
        print(user_ans)
        calc()


def stratquiz():
    global lblquestion,r1,r2,r3,r4
    lblquestion = Label(
        root,
        text=questions[indexex[0]],
        font=("Consols",16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff"

    )
    lblquestion.pack(pady=(100,30))
    global radiovar
    radiovar=IntVar()
    radiovar.set(-1)
    r1=Radiobutton(
       root,
        text=answer_choice[indexex[0]][0],
        font=("Times",12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r1.pack(pady=5)
    r2 = Radiobutton(
        root,
        text=answer_choice[indexex[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r2.pack(pady=5)
    r3 = Radiobutton(
        root,
        text=answer_choice[indexex[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
    )
    r3.pack(pady=5)
    r4 = Radiobutton(
        root,
        text=answer_choice[indexex[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"
    )
    r4.pack(pady=5)
def start():
    l1.destroy()
    l2.destroy()
    lb3.destroy()
    lbrules.destroy()
    btn.destroy()
    gen()
    stratquiz()
root=tkinter.Tk()
root.title("Quizzess")
root.geometry("900x600")
root.config(background="#ffffff")
root.resizable(0,0)

img1=PhotoImage(file="qui.png",)
l1=Label(
    root,
    image=img1,
    background="#ffffff",
)
l1.pack(pady=(40,0))
l2=Label(
    root,
    text="Quizzess",
    font=("Comic sans MS",24,"bold"),
    background="#ffffff",

)
l2.pack(pady=(0,50))
img2=PhotoImage(file="st1.png")
btn=Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=start,
)
btn.pack()
lb3=Label(
    root,
    text="Read The Instruction Carefully And\nClick start to Continue",
    background="#ffffff",
    font=("consolas",8),
    justify="center",

)
lb3.pack(pady=(0,170))
lbrules=Label(
    root,
    text= "The quizzes consists of questions carefully designed to help you self-assess your comprehension of the information presented on the topics\nNo data will be collected on the website regarding your responses or how many times you take the quiz.\nEach question in the quiz is of multiple-choice or true or false format.\nOnce u select a final button that will be a final choice.\nHence think befotre you select",
    width=200,
    font=("Times",12),
    background="#000000",
    foreground="#FACA2F",
)
lbrules.pack()


root.mainloop()