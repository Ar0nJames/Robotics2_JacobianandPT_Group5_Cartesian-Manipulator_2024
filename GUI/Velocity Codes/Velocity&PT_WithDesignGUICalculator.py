from tkinter import * 
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib
matplotlib.use('TkAgg')
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/yuel/Desktop/CARTESIAN/GUI/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1100x700")
window.configure(bg = "#005B8F")

canvas = Canvas(
    window,
    bg="#005B8F",
    height=700,
    width=1100,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    580.0,
    528.0,
    image=image_image_1
)

canvas.create_rectangle(
    8.0,
    8.0,
    1090.0,
    124.0,
    fill="#001B63",
    outline="")

canvas.create_text(
    466.0,
    147.0,
    anchor="nw",
    text="Link lengths",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_rectangle(
    438.0,
    204.0,
    481.0,
    232.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    438.0,
    309.0,
    481.0,
    337.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    438.0,
    274.0,
    481.0,
    302.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    438.0,
    239.0,
    481.0,
    267.0,
    fill="#0047FF",
    outline="")

canvas.create_text(
    495.0,
    199.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)

)


tbox1 = canvas.create_text(
    495.0,
    304.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    495.0,
    269.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    495.0,
    234.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    587.0,
    218.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=527.0,
    y=204.0,
    width=120.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    587.0,
    323.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=527.0,
    y=239.0,
    width=120.0,
    height=26.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    587.0,
    288.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=527.0,
    y=274.0,
    width=120.0,
    height=26.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    587.0,
    253.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=527.0,
    y=309.0,
    width=120.0,
    height=26.0
)

canvas.create_rectangle(
    747.0,
    433.0,
    790.0,
    461.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    747.0,
    503.0,
    790.0,
    531.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    747.0,
    468.0,
    790.0,
    496.0,
    fill="#0047FF",
    outline="")

canvas.create_text(
    805.0,
    428.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    805.0,
    498.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    805.0,
    463.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    896.0,
    447.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=836.0,
    y=433.0,
    width=120.0,
    height=26.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    896.0,
    517.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=836.0,
    y=503.0,
    width=120.0,
    height=26.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    896.0,
    482.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=836.0,
    y=468.0,
    width=120.0,
    height=26.0
)

canvas.create_rectangle(
    137.0,
    437.0,
    180.0,
    465.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    137.0,
    507.0,
    180.0,
    535.0,
    fill="#0047FF",
    outline="")

canvas.create_rectangle(
    137.0,
    472.0,
    180.0,
    500.0,
    fill="#0047FF",
    outline="")

canvas.create_text(
    195.0,
    432.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    195.0,
    502.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    195.0,
    467.0,
    anchor="nw",
    text="=",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    286.0,
    451.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=226.0,
    y=507.0,
    width=120.0,
    height=26.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    286.0,
    521.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=226.0,
    y=437.0,
    width=120.0,
    height=26.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    286.0,
    486.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=226.0,
    y=472.0,
    width=120.0,
    height=26.0
)

canvas.create_text(
    712.0,
    382.0,
    anchor="nw",
    text="Joint Variable",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

canvas.create_text(
    150.0,
    382.0,
    anchor="nw",
    text="Position Vector",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    239.0,
    267.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    875.0,
    266.0,
    image=image_image_3
)

text = "CartesianManipulator"
font = ("Kodchasan Medium", 45)
x, y = 230.0, 20.0 
for char in text:
    if char in ['C', 'M']:
        color = 'red'
    else:
        color = '#FFFFFF'

    text_id = canvas.create_text(x, y, anchor="nw", text=char, fill=color, font=font)
    bbox = canvas.bbox(text_id)
    text_width = bbox[2] - bbox[0]
    x += text_width


canvas.create_text(
    447.0,
    205.0,
    anchor="nw",
    text="a1",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    447.0,
    274.0,
    anchor="nw",
    text="a3",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    447.0,
    308.0,
    anchor="nw",
    text="a4",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    447.0,
    240.0,
    anchor="nw",
    text="a2",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    206.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    352.0,
    440.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    352.0,
    510.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    352.0,
    475.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    960.0,
    439.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    960.0,
    509.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    960.0,
    474.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    314.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    278.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    650.0,
    242.0,
    anchor="nw",
    text="cm",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    146.0,
    438.0,
    anchor="nw",
    text="X",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    146.0,
    507.0,
    anchor="nw",
    text="Z",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    146.0,
    473.0,
    anchor="nw",
    text="Y",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    350.0,
    89.0,
    anchor="nw",
    text="Forward and Reverse Kinematics Calculator",
    fill="#FFFFFF",
    font=("Commissioner Regular", 20 * -1)
)

canvas.create_text(
    763.0,
    435.0,
    anchor="nw",
    text="d1",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    763.0,
    470.0,
    anchor="nw",
    text="d2",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)

canvas.create_text(
    763.0,
    504.0,
    anchor="nw",
    text="d3",
    fill="#FFFFFF",
    font=("LibreBodoniRoman Regular", 24 * -1)
)


def f_k():

    # link lengths in cm
    a1 = float(entry_1.get())
    a2 = float(entry_2.get())
    a3 = float(entry_3.get())
    a4 = float(entry_4.get())

    # joint variables: is mm if f, is degrees if theta
    d1 = float(entry_5.get())
    d2 = float(entry_6.get())
    d3 = float(entry_7.get())

    if a1 <0:
        messagebox.showerror(title="Invalid", message= " A1 is below 0.")
    if a2 <0:
        messagebox.showerror(title="Invalid", message= " A2 is below 0.")
    if a3 <0:
        messagebox.showerror(title="Invalid", message= " A3 is below 0.")
    if a4 <0:
        messagebox.showerror(title="Invalid", message= " A4 is below 0.")

    # Parametric Table (theta, alpha, r, d)
    PT = [[(0.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,a1],
         [(270.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,a2+d1],
         [(90.0/180.0)*np.pi,(270.0/180.0)*np.pi,0,a3+d2],
         [(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a4+d3]]
    
    # HTM formulae
    i = 0
    H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    i = 1
    H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    i = 2
    H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    i = 3
    H3_4 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        [0,0,0,1]]
    
    H0_1 = np.matrix(H0_1)
    H1_2 = np.matrix(H1_2)
    H2_3 = np.matrix(H2_3)
    H3_4 = np.matrix(H3_4)
    
    H0_2 = np.dot(H0_1,H1_2)
    H2_4 = np.dot(H2_3,H3_4)
    H0_4 = np.dot(H0_2,H2_4)
    
    X0_4 = H0_4[0,3]
    entry_10.delete(0,END)
    entry_10.insert(0,np.around(X0_4*100,3))
    
    Y0_4 = H0_4[1,3]
    entry_9.delete(0,END)
    entry_9.insert(0,np.around(Y0_4*100,3))
    
    Z0_4 = H0_4[2,3]
    entry_8.delete(0,END)
    entry_8.insert(0,np.around(Z0_4*100,3))

#jacobian matrix start
    J_sw = Toplevel()
    J_sw.title("Velocity Calculator")
    J_sw.resizable(False,False)
    J_sw.configure(bg='#000547')

    #Linear/ prismatic vectors 
    Z_1 = [[0],
           [0],
           [1]] # 001 vector

    # Row 1 - 3, column 1 
    J1 = [[1,0,0],
          [0,1,0],
          [0,0,1]] #R0_0
    J1 = np.dot(J1,Z_1)
    J1 = (np.matrix(J1))

    # Row 1 - 3, column 2 
    J2 = [[0,0,1],
          [-1,0,0],
          [0,-1,0]] #R0_1
    J2 = np.dot(J2,Z_1)
    J2 = (np.matrix(J2))

    # Row 1 - 3, column 3 
    J3 = [[0,-1,0],
          [0,0,-1],
          [1,0,0]] #R0_2
    J3 = np.dot(J3,Z_1)
    J3 = (np.matrix(J3))

    # Rotation / Orientation vectors

    #Row 4 - 6, column 1
    J4 =[[0],[0],[0]]
    J4 = (np.matrix(J4))

    #Row 4-6, column2

    J5 =[[0],[0],[0]]
    J5 = (np.matrix(J5))

    #Row 4-6, column 3 
    J6 =[[0],[0],[0]]
    J6 = (np.matrix(J6))


    #3 Concatenated jacobian matrix 
    JM1 = np.concatenate((J1,J2,J3),1)
    JM2 = np.concatenate((J4,J5,J6),1)

    J = np.concatenate((JM1,JM2),0)

    def update_velo():
        d1p = d1_slider.get()
        d2p = d2_slider.get()
        d3p = d3_slider.get()

        q = np.array([[d1p],[d2p],[d3p]])
        E = np.dot(J,q)
        E = np.array(E)

        xp_e =E[0,0]
        x_entry.delete(0,END)
        x_entry.insert(0,str(xp_e))
        yp_e =E[1,0]
        y_entry.delete(0,END)
        y_entry.insert(0,str(yp_e))
        zp_e =E[2,0]
        z_entry.delete(0,END)
        z_entry.insert(0,str(zp_e))
        ωx_e =E[3,0]
        ωx_entry.delete(0,END)
        ωx_entry.insert(0,str(ωx_e))
        ωy_e =E[4,0]
        ωy_entry.delete(0,END)
        ωy_entry.insert(0,str(ωy_e))
        ωz_e =E[5,0]
        ωz_entry.delete(0,END)
        ωz_entry.insert(0,str(ωz_e))

    d1_velo = Label(J_sw,text=("     d1 =     "),font=(5),bg="#0013FF")
    d1_slider = Scale(J_sw,from_=0, to_=30,orient=HORIZONTAL,length=100,bg='navy blue',fg='#0010D0')
    d1_unit = Label(J_sw,text=("cm/s"),font=(5),bg="#000547",fg='white')

    d2_velo = Label(J_sw,text=("     d2 =     "),font=(5),bg="#0013FF")
    d2_slider = Scale(J_sw,from_=0, to_=30,orient=HORIZONTAL,length=100,bg='navy blue',fg='#0010D0')
    d2_unit = Label(J_sw,text=("cm/s"),font=(5),bg="#000547",fg='white')

    d3_velo = Label(J_sw,text=("     d3 =     "),font=(5),bg="#0013FF")
    d3_slider = Scale(J_sw,from_=0, to_=30,orient=HORIZONTAL,length=100,bg='navy blue',fg='#0010D0')
    d3_unit = Label(J_sw,text=("cm/s"),font=(5),bg="#000547",fg='white')

    d1_velo.grid(row=0,column=0)
    d1_slider.grid(row=0,column=1)
    d1_unit.grid(row=0,column=2)

    d2_velo.grid(row=1,column=0)
    d2_slider.grid(row=1,column=1)
    d2_unit.grid(row=1,column=2)

    d3_velo.grid(row=2,column=0)
    d3_slider.grid(row=2,column=1)
    d3_unit.grid(row=2,column=2)

    #Jacobian Entry boxes
    x_velo = Label(J_sw,text=("      X =     "),font=(5),bg="#0013FF")
    x_entry = Entry(J_sw,width=10, font=10)
    x_unit = Label(J_sw,text=(" cm/s"),font=(5),bg="#000547",fg='white')
    x_velo.grid(row=3,column=0)
    x_entry.grid(row=3,column=1)
    x_unit.grid(row=3,column=2)

    y_velo = Label(J_sw,text=("      Y =      "),font=(5),bg="#0013FF")
    y_entry = Entry(J_sw,width=10, font=10)
    y_unit = Label(J_sw,text=(" cm/s"),font=(5),bg="#000547",fg='white')
    y_velo.grid(row=4,column=0)
    y_entry.grid(row=4,column=1)
    y_unit.grid(row=4,column=2)

    z_velo = Label(J_sw,text=("      Z =      "),font=(5),bg="#0013FF")
    z_entry = Entry(J_sw,width=10, font=10)
    z_unit = Label(J_sw,text=(" cm/s"),font=(5),bg="#000547",fg='white')
    z_velo.grid(row=5,column=0)
    z_entry.grid(row=5,column=1)
    z_unit.grid(row=5,column=2)

    ωx_velo = Label(J_sw,text=("    ωX =     "),font=(5),bg="#0013FF")
    ωx_entry = Entry(J_sw,width=10, font=10)
    ωx_unit = Label(J_sw,text=(" rad/s"),font=(5),bg="#000547",fg='white')
    ωx_velo.grid(row=6,column=0)
    ωx_entry.grid(row=6,column=1)
    ωx_unit.grid(row=6,column=2)

    ωy_velo = Label(J_sw,text=("    ωY =     "),font=(5),bg="#0013FF")
    ωy_entry = Entry(J_sw,width=10, font=10)
    ωy_unit = Label(J_sw,text=(" rad/s"),font=(5),bg="#000547",fg='white')
    ωy_velo.grid(row=7,column=0)
    ωy_entry.grid(row=7,column=1)
    ωy_unit.grid(row=7,column=2)

    ωz_velo = Label(J_sw,text=("    ωZ =     "),font=(5),bg="#0013FF")
    ωz_entry = Entry(J_sw,width=10, font=10)
    ωz_unit = Label(J_sw,text=(" rad/s"),font=(5),bg="#000547",fg='white')
    ωz_velo.grid(row=8,column=0)
    ωz_entry.grid(row=8,column=1)
    ωz_unit.grid(row=8,column=2)

    #buttons
    update_but = Button(J_sw,text="UPDATE",bg="#2AFF00", fg="black",command= update_velo)
    update_but.grid(row=9,column=1)
    #jacobianmatrix end 

    ## Singularity
    D_J = np.linalg.det(JM1)
    print("D_J = ",D_J)

    ## Inverse Velocity
    I_V = np.linalg.inv(JM1)
    print("I_V = ",I_V)
    
    CARTESIAN = DHRobot([
        PrismaticDH(0,0,(270.0/180.0)*np.pi,a1/100,qlim=[0,0]),
        PrismaticDH((270.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a2/100,qlim=[0,30/100]),
        PrismaticDH((90.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a3/100,qlim=[0,30/100]),
        PrismaticDH(0,0,(0.0/180.0)*np.pi,a4/100,qlim=[0,30/100]),
        ],name='Cartesian') 
    
    # q planned paths 
    q0 = np.array([0,0,0,0])
    q1 = np.array([0, d1/100, d2/100, d3/100,])

    #plot Scale
    x1 = -0.5
    x2 = 0.5
    y1 = -0.5
    y2 = 0.5
    z1 = 0
    z2 = 0.5

    # trajectory command
    traj1 = rtb.jtraj(q0,q1,30)

    #plot Scale
    x1 = -0.5
    x2 = 0.5
    y1 = -0.5
    y2 = 0.5
    z1 = 0
    z2 = 0.5

    #plot command  
    CARTESIAN.plot(traj1.q, limits=[x1,x2,y1,y2,z1,z2],block=True)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    text="Forward",
    compound="center",
    fg="white",
    font=("LibreBodoniRoman Regular", 24 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=f_k,
    relief="flat"
)
button_2.place(
    x=745.0,
    y=577.0,
    width=255.0,
    height=64.0
)



def i_k():
    #Inverse Kinematics Using Graphical Method

    #link lengths in cm
    a1 =float(entry_1.get())
    a2 =float(entry_2.get())
    a3 =float(entry_3.get())
    a4 =float(entry_4.get())

    #Position Vector in cm
    xe = float(entry_8.get())
    ye = float(entry_9.get())
    ze = float(entry_10.get())

    # To solve for D2
    d2 = xe-a3
    
    # To solve for D3
    d3 = a1-a4-ze
    
    # To solve for D1
    d1 = ye-a2


    entry_7.delete(0,END)
    entry_7.insert(0,np.around(d1,3))

    entry_6.delete(0,END)
    entry_6.insert(0,np.around(d2,3))

    entry_5.delete(0,END)
    entry_5.insert(0,np.around(d3,3))

    # Create Links (d,r,alpha,offset)
    
    
    CARTESIAN = DHRobot([
        PrismaticDH(0,0,(270.0/180.0)*np.pi,a1/100,qlim=[0,0]),
        PrismaticDH((270.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a2/100,qlim=[0,30/100]),
        PrismaticDH((90.0/180.0)*np.pi,0,(270.0/180.0)*np.pi,a3/100,qlim=[0,30/100]),
        PrismaticDH(0,0,(0.0/180.0)*np.pi,a4/100,qlim=[0,30/100]),
        ],name='Cartesian') 
    
    #plot joints
    q0 = np.array([0,0,0,0])
    q1 = np.array([0, d1/100, d2/100, d3/100])

    # trajectory command
    traj1 = rtb.jtraj(q0,q1,30)

    #plot Scale
    x1 = -0.5
    x2 = 0.5
    y1 = -0.5
    y2 = 0.5
    z1 = 0
    z2 = 0.5

    #plot command  
    CARTESIAN.plot(traj1.q, limits=[x1,x2,y1,y2,z1,z2],block=True)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    text="Inverse",
    compound="center",
    fg="white",
    font=("LibreBodoniRoman Regular", 24 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=i_k,
    relief="flat"
)
button_1.place(
    x=115.0,
    y=577.0,
    width=255.0,
    height=64.0
)



def reset():
    
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)
    entry_5.delete(0,END)
    entry_6.delete(0,END)
    entry_7.delete(0,END)
    entry_8.delete(0,END)
    entry_9.delete(0,END)
    entry_10.delete(0,END)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    text="Reset",
    compound="center",
    fg="white",
    font=("LibreBodoniRoman Regular", 24 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=reset,
    relief="flat"
)



button_3.place(
    x=429.0,
    y=464.0,
    width=255.0,
    height=64.0
)
window.resizable(False, False)
window.mainloop()


