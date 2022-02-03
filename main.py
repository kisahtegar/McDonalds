import tkinter as tk
import datetime as dt
from PIL import Image
from PIL import ImageTk
from time import strftime

class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.top_bar_options()
        self.food_options()
        self.drink_options()
        self.bills_log_options()
        self.right_bar_options()

    def top_bar_options(self):
        pathdesign_img = "image/design/"
        # RED BARS
        self.bar_Tbar = tk.Label(self.master, bg="#DA291C", height=7)
        self.bar_Tbar.pack(side=tk.TOP, fill=tk.BOTH)
        self.bar_Tbar.pack_propagate(0)

        # M LOGO
        self.logo_Tbar_img = ImageTk.PhotoImage(Image.open(pathdesign_img+'Mlogo.jpg'))
        self.logo_Tbar = tk.Label(self.bar_Tbar, image=self.logo_Tbar_img, bg="#DA291C")
        self.logo_Tbar.pack(side=tk.LEFT, fill=tk.BOTH)

        # TITLE 
        self.title_Tbar = tk.Label(self.bar_Tbar, text="McDonald's System Management", font=('verdana',25,'bold'), bg="#DA291C", fg="black")
        self.title_Tbar.pack(side=tk.LEFT, fill=tk.BOTH)

        # DATE
        self.date_Tbar = tk.Label(self.bar_Tbar, text=f"{dt.datetime.now():%a, %b %d %Y}", font=("calibri", 13, "bold"), bg="#DA291C", fg="white")
        self.date_Tbar.pack(side=tk.TOP, anchor=tk.E)
        
        # TIME
        def time():
            self.string = strftime('%H:%M:%S %p') 
            self.time_Tbar.config(text=self.string) 
            self.time_Tbar.after(1000, time)
        self.time_Tbar = tk.Label(self.bar_Tbar, bg="#DA291C", font=("calibri", 13, "bold"), foreground="white")
        self.time_Tbar.pack(side=tk.TOP, anchor=tk.E)
        time()
    
    def food_options(self):
        # </> FOOD LABEL FRAME </>
        self.food_frame = tk.LabelFrame(self.master)
        self.food_frame.config(
            text = "All Food", 
            font = ('calibri',12,'bold'),
            borderwidth = 3, 
            relief = "ridge", 
            highlightthickness = 2,
            highlightcolor = "white",
            highlightbackground = "white",
            background = "white",
            foreground = "#DA291C"
        )
        self.food_frame.place(x=20, y=113)
        pathfood_img = "image/food/"

        # </> FOOD </>
        # (1) </> Big Mac </>
        self.bigmac_img = Image.open(pathfood_img+"bigmac.png")
        self.bigmac_img = self.bigmac_img.resize((100,100), Image.ANTIALIAS)
        self.bigmac_photoImg = ImageTk.PhotoImage(self.bigmac_img)
        self.bigmac = tk.Label(self.food_frame, image=self.bigmac_photoImg, text="Big Mac\nRp. 35,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white")
        self.bigmac.grid(row=0, column=0,padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_1(val):
            self.bigmac_entry.config(state=tk.NORMAL)
            value = int(self.bigmac_entry.get())
            value += val
            self.bigmac_entry.delete(0,"end")
            self.bigmac_entry.insert(0, value)
            self.bigmac_entry.config(state=tk.DISABLED)
        def minus_1(val):
            self.bigmac_entry.config(state=tk.NORMAL)
            if self.bigmac_entry.get() == '0':
                pass
            else:
                value = int(self.bigmac_entry.get())
                value -= val
                self.bigmac_entry.delete(0,"end")
                self.bigmac_entry.insert(0, value)
            self.bigmac_entry.config(state=tk.DISABLED)
        # Plus (-)
        self.bigmac_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_1(1))
        self.bigmac_minus.place(x=22, y=144)
        # Entry []
        self.bigmac_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.bigmac_entry.config(state=tk.NORMAL)
        self.bigmac_entry.insert(0, 0)
        self.bigmac_entry.config(state=tk.DISABLED)
        self.bigmac_entry.place(x=47, y=158)
        # Plus (+)
        self.bigmac_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_1(1))
        self.bigmac_plus.place(x=97, y=144)

        # (2) </> PaNas1 </>
        self.panas1_img = Image.open(pathfood_img+"PaNas1.png")
        self.panas1_img = self.panas1_img.resize((100,100), Image.ANTIALIAS)
        self.panas1_photoImg = ImageTk.PhotoImage(self.panas1_img)
        self.panas1 = tk.Label(self.food_frame, image=self.panas1_photoImg, text="PaNas1\nRp. 32,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.panas1.grid(row=0, column=1, padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_2(val):
            self.panas1_entry.config(state=tk.NORMAL)
            value = int(self.panas1_entry.get())
            value += val
            self.panas1_entry.delete(0,"end")
            self.panas1_entry.insert(0, value)
            self.panas1_entry.config(state=tk.DISABLED)
        def minus_2(val):
            self.panas1_entry.config(state=tk.NORMAL)
            if self.panas1_entry.get() == '0':
                pass
            else:
                value = int(self.panas1_entry.get())
                value -= val
                self.panas1_entry.delete(0,"end")
                self.panas1_entry.insert(0, value)
            self.panas1_entry.config(state=tk.DISABLED)
        # Minus (-)
        self.panas1_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_2(1))
        self.panas1_minus.place(x=172, y=144)
        # Entry []
        self.panas1_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.panas1_entry.config(state=tk.NORMAL)
        self.panas1_entry.insert(0,0)
        self.panas1_entry.config(state=tk.DISABLED)
        self.panas1_entry.place(x=197, y=158)
        # Plus (+)
        self.panas1_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_2(1))
        self.panas1_plus.place(x=247, y=144)

        # (3) </> PaNas Spesial </>
        self.panas_s_img = Image.open(pathfood_img+"PaNas Spesial.png")
        self.panas_s_img = self.panas_s_img.resize((100,100), Image.ANTIALIAS)
        self.panas_s_photoImg = ImageTk.PhotoImage(self.panas_s_img)
        self.panas_s = tk.Label(self.food_frame, image=self.panas_s_photoImg, text="PaNas Spesial\nRp. 38,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.panas_s.grid(row=0,column=2, padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_3(val):
            self.panas_s_entry.config(state=tk.NORMAL)
            value = int(self.panas_s_entry.get())
            value += val
            self.panas_s_entry.delete(0,"end")
            self.panas_s_entry.insert(0, value)
            self.panas_s_entry.config(state=tk.DISABLED)
        def minus_3(val):
            self.panas_s_entry.config(state=tk.NORMAL)
            if self.panas_s_entry.get() == '0':
                pass
            else:
                value = int(self.panas_s_entry.get())
                value -= val
                self.panas_s_entry.delete(0,"end")
                self.panas_s_entry.insert(0, value)
            self.panas_s_entry.config(state=tk.DISABLED)
        # Minus (-)
        self.panas_s_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_3(1))
        self.panas_s_minus.place(x=320, y=144)
        # Entry []
        self.panas_s_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.panas_s_entry.config(state=tk.NORMAL)
        self.panas_s_entry.insert(0, 0)
        self.panas_s_entry.config(state=tk.DISABLED)
        self.panas_s_entry.place(x=344, y=158)
        # Plus (+)
        self.panas_s_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_3(1))
        self.panas_s_plus.place(x=394, y=144)

        # (4) </> McChicken </>
        self.mcchicken_img = Image.open(pathfood_img+"McChicken.png")
        self.mcchicken_img = self.mcchicken_img.resize((100,100), Image.ANTIALIAS)
        self.mcchicken_photoImg = ImageTk.PhotoImage(self.mcchicken_img)
        self.mcchicken = tk.Label(self.food_frame, image=self.mcchicken_photoImg, text="McChicken\nRp. 28,500", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.mcchicken.grid(row=0,column=3, padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_4(val):
            self.mcchicken_entry.config(state=tk.NORMAL)
            value = int(self.mcchicken_entry.get())
            value += val
            self.mcchicken_entry.delete(0, "end")
            self.mcchicken_entry.insert(0, value)
            self.mcchicken_entry.config(state=tk.DISABLED)
        def minus_4(val):
            self.mcchicken_entry.config(state=tk.NORMAL)
            if self.mcchicken_entry.get() == "0":
                pass
            else:
                value = int(self.mcchicken_entry.get())
                value -= val
                self.mcchicken_entry.delete(0, "end")
                self.mcchicken_entry.insert(0, value)
            self.mcchicken_entry.config(state=tk.DISABLED)
        # Minus (-)
        self.mcchicken_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_4(1))
        self.mcchicken_minus.place(x=470, y=144)
        # Entry []
        self.mcchicken_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.mcchicken_entry.config(state=tk.NORMAL)
        self.mcchicken_entry.insert(0,0)
        self.mcchicken_entry.config(state=tk.DISABLED)
        self.mcchicken_entry.place(x=495, y=158)
        # Plus (+)
        self.mcchicken_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_4(1))
        self.mcchicken_plus.place(x=545, y=144)

        # (5) </> McNuggets </>
        self.mcnuggets_img = Image.open(pathfood_img+"McNuggets.png")
        self.mcnuggets_img = self.mcnuggets_img.resize((100,100), Image.ANTIALIAS)
        self.mcnuggets_photoImg = ImageTk.PhotoImage(self.mcnuggets_img)
        self.mcnuggets = tk.Label(self.food_frame, image=self.mcnuggets_photoImg, text="McNuggets\nRp. 27,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.mcnuggets.grid(row=0,column=4, padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_5(val):
            self.mcnuggets_entry.config(state=tk.NORMAL)
            value = int(self.mcnuggets_entry.get())
            value += val
            self.mcnuggets_entry.delete(0, "end")
            self.mcnuggets_entry.insert(0, value)
            self.mcnuggets_entry.config(state=tk.DISABLED)
        def minus_5(val):
            self.mcnuggets_entry.config(state=tk.NORMAL)
            if self.mcnuggets_entry.get() == "0":
                pass
            else:
                value = int(self.mcnuggets_entry.get())
                value -= val
                self.mcnuggets_entry.delete(0, "end")
                self.mcnuggets_entry.insert(0, value)
            self.mcnuggets_entry.config(state=tk.DISABLED)
        # Minus (-)
        self.mcnuggets_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_5(1))
        self.mcnuggets_minus.place(x=618, y=144)
        # Entry []
        self.mcnuggets_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.mcnuggets_entry.config(state=tk.NORMAL)
        self.mcnuggets_entry.insert(0,0)
        self.mcnuggets_entry.config(state=tk.DISABLED)
        self.mcnuggets_entry.place(x=642, y=158)
        # Plus (+)
        self.mcnuggets_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'), width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_5(1))
        self.mcnuggets_plus.place(x=692, y=144)

        #--------------------------------------------------------------------------------------------------------------------------------------------------
        
        # (6) </> Chicken Fingers </>
        self.chicken_f_img = Image.open(pathfood_img+"Chicken Fingers.png")
        self.chicken_f_img = self.chicken_f_img.resize((100,100), Image.ANTIALIAS)
        self.chicken_f_photoImg = ImageTk.PhotoImage(self.chicken_f_img)
        self.chicken_f = tk.Label(self.food_frame, image=self.chicken_f_photoImg, text="Chicken Fingers\nRp. 13,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.chicken_f.grid(row=1, column=0,padx=1, pady=(0,41))
        # </> Amount Button </>
        def plus_6(val):
            self.chicken_f_entry.config(state=tk.NORMAL)
            value = int(self.chicken_f_entry.get())
            value += val
            self.chicken_f_entry.delete(0, "end")
            self.chicken_f_entry.insert(0, value)
            self.chicken_f_entry.config(state=tk.DISABLED)
        def minus_6(val):
            self.chicken_f_entry.config(state=tk.NORMAL)
            if self.chicken_f_entry.get() == "0":
                pass
            else:
                value = int(self.chicken_f_entry.get())
                value -= val
                self.chicken_f_entry.delete(0, "end")
                self.chicken_f_entry.insert(0, value)
            self.chicken_f_entry.config(state=tk.DISABLED)
        # Minus (-)
        self.chicken_f_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_6(1))
        self.chicken_f_minus.place(x=22, y=330)
        # Entry []
        self.chicken_f_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.chicken_f_entry.config(state=tk.NORMAL)
        self.chicken_f_entry.insert(0,0)
        self.chicken_f_entry.config(state=tk.DISABLED)
        self.chicken_f_entry.place(x=47, y=343)
        # Plus (+)
        self.chicken_f_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_6(1))
        self.chicken_f_plus.place(x=97, y=330)

        # (7) </> McSpicy </>
        self.mcspicy_img = Image.open(pathfood_img+"McSpicy.png")
        self.mcspicy_img = self.mcspicy_img.resize((100,100), Image.ANTIALIAS)
        self.mcspicy_photoImg = ImageTk.PhotoImage(self.mcspicy_img)
        self.mcspicy = tk.Label(self.food_frame, image=self.mcspicy_photoImg, text="McSpicy\nRp. 36,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.mcspicy.grid(row=1, column=1,padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_7(val):
            self.mcspicy_entry.config(state=tk.NORMAL)
            value = int(self.mcspicy_entry.get())
            value += val
            self.mcspicy_entry.delete(0, "end")
            self.mcspicy_entry.insert(0, value)
            self.mcspicy_entry.config(state=tk.DISABLED)
        def minus_7(val):
            self.mcspicy_entry.config(state=tk.NORMAL)
            if self.mcspicy_entry.get() == "0":
                pass
            else:
                value = int(self.mcspicy_entry.get())
                value -= val
                self.mcspicy_entry.delete(0, "end")
                self.mcspicy_entry.insert(0, value)
            self.mcspicy_entry.config(state=tk.DISABLED)
        # Minus (-)
        self.mcspicy_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_7(1))
        self.mcspicy_minus.place(x=172, y=330)
        # Entry []
        self.mcspicy_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.mcspicy_entry.config(state=tk.NORMAL)
        self.mcspicy_entry.insert(0,0)
        self.mcspicy_entry.config(state=tk.DISABLED)
        self.mcspicy_entry.place(x=197, y=343)
        # Plus (+)
        self.mcspicy_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_7(1))
        self.mcspicy_plus.place(x=247, y=330)

        # (8) </> Beef Burger </>
        self.beefburger_img = Image.open(pathfood_img+"Beef Burger.png")
        self.beefburger_img = self.beefburger_img.resize((100,100), Image.ANTIALIAS)
        self.beefburger_photoImg = ImageTk.PhotoImage(self.beefburger_img)
        self.beefburger = tk.Label(self.food_frame, image=self.beefburger_photoImg, text="Beef Burger\nRp. 22,500", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.beefburger.grid(row=1, column=2,padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_8(val):
            self.beefburger_entry.config(state=tk.NORMAL)
            value = int(self.beefburger_entry.get())
            value += val
            self.beefburger_entry.delete(0, "end")
            self.beefburger_entry.insert(0, value)
            self.beefburger_entry.config(state=tk.DISABLED)
        def minus_8(val):
            self.beefburger_entry.config(state=tk.NORMAL)
            if self.beefburger_entry.get() == "0":
                pass
            else:
                value = int(self.beefburger_entry.get())
                value -= val
                self.beefburger_entry.delete(0, "end")
                self.beefburger_entry.insert(0, value)
            self.beefburger_entry.config(state=tk.DISABLED)
        # Minus (-)
        self.beefburger_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_8(1))
        self.beefburger_minus.place(x=320, y=330)
        # Entry []
        self.beefburger_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.beefburger_entry.config(state=tk.NORMAL)
        self.beefburger_entry.insert(0,0)
        self.beefburger_entry.config(state=tk.DISABLED)
        self.beefburger_entry.place(x=344, y=343)
        # Plus (+)
        self.beefburger_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_8(1))
        self.beefburger_plus.place(x=394, y=330)


        # (9) </> PaMer5 </>
        self.pamer5_img = Image.open(pathfood_img+"PaMer5.png")
        self.pamer5_img = self.pamer5_img.resize((100,100), Image.ANTIALIAS)
        self.pamer5_photoImg = ImageTk.PhotoImage(self.pamer5_img)
        self.pamer5 = tk.Label(self.food_frame, image=self.pamer5_photoImg, text="PaMer5\nRp. 108,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.pamer5.grid(row=1, column=3,padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_9(val):
            self.pamer5_entry.config(state=tk.NORMAL)
            value = int(self.pamer5_entry.get())
            value += val
            self.pamer5_entry.delete(0, "end")
            self.pamer5_entry.insert(0, value)
            self.pamer5_entry.config(state=tk.DISABLED)
        def minus_9(val):
            self.pamer5_entry.config(state=tk.NORMAL)
            if self.pamer5_entry.get() == "0":
                pass
            else:
                value = int(self.pamer5_entry.get())
                value -= val
                self.pamer5_entry.delete(0, "end")
                self.pamer5_entry.insert(0, value)
            self.pamer5_entry.config(state=tk.DISABLED)
        # Plus (-)
        self.pamer5_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_9(1))
        self.pamer5_minus.place(x=470, y=330)
        # Entry []
        self.pamer5_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.pamer5_entry.config(state=tk.NORMAL)
        self.pamer5_entry.insert(0,0)
        self.pamer5_entry.config(state=tk.DISABLED)
        self.pamer5_entry.place(x=495, y=343)
        # Plus (+)
        self.pamer5_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_9(1))
        self.pamer5_plus.place(x=545, y=330)

        # (10) </> PaMer7 </>
        self.pamer7_img = Image.open(pathfood_img+"PaMer7.png")
        self.pamer7_img = self.pamer7_img.resize((100,100), Image.ANTIALIAS)
        self.pamer7_photoImg = ImageTk.PhotoImage(self.pamer7_img)
        self.pamer7 = tk.Label(self.food_frame, image=self.pamer7_photoImg, text="PaMer7\nRp. 157,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.pamer7.grid(row=1, column=4,padx=1, pady=(0,40))
        # </> Amount Button </>
        def plus_10(val):
            self.pamer7_entry.config(state=tk.NORMAL)
            value = int(self.pamer7_entry.get())
            value += val
            self.pamer7_entry.delete(0, "end")
            self.pamer7_entry.insert(0, value)
            self.pamer7_entry.config(state=tk.DISABLED)
        def minus_10(val):
            self.pamer7_entry.config(state=tk.NORMAL)
            if self.pamer7_entry.get() == "0":
                pass
            else:
                value = int(self.pamer7_entry.get())
                value -= val
                self.pamer7_entry.delete(0, "end")
                self.pamer7_entry.insert(0, value)
            self.pamer7_entry.config(state=tk.DISABLED)
        # Plus (-)
        self.pamer7_minus = tk.Button(self.food_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_10(1))
        self.pamer7_minus.place(x=618, y=330)
        # Entry []
        self.pamer7_entry = tk.Entry(self.food_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.pamer7_entry.config(state=tk.NORMAL)
        self.pamer7_entry.insert(0,0)
        self.pamer7_entry.config(state=tk.DISABLED)
        self.pamer7_entry.place(x=642, y=343)
        # Plus (+)
        self.pamer7_plus = tk.Button(self.food_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_10(1))
        self.pamer7_plus.place(x=692, y=330)

    def drink_options(self):
        # </> DRINK LABEL FRAME </>
        self.drink_frame = tk.LabelFrame(self.master)
        self.drink_frame.config(
            text = "All Drink", 
            font = ('calibri',12,'bold'), 
            width = 560, 
            height = 160, 
            borderwidth = 3, 
            relief = "ridge", 
            highlightthickness = 2,
            highlightcolor = "white",
            highlightbackground = "white",
            background = "white",
            foreground = "#DA291C"
        )
        self.drink_frame.place(x=20, y=518)
        pathdrink_img = "image/drink/"

        # </> DRINK </>
        # (1) </> Fanta McFloat </>
        self.fanta_f_img = Image.open(pathdrink_img+"Fanta McFloat.png")
        self.fanta_f_img = self.fanta_f_img.resize((100,100), Image.ANTIALIAS)
        self.fanta_f_photoImg = ImageTk.PhotoImage(self.fanta_f_img)
        self.fanta_f = tk.Label(self.drink_frame, image=self.fanta_f_photoImg, text="Fanta McFloat\nRp. 12,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.fanta_f.grid(row=0, column=0, padx=1, pady=(0,41))
        # </> Amount Button </>
        def plus_1(val):
            self.fanta_f_entry.config(state=tk.NORMAL)
            value = int(self.fanta_f_entry.get())
            value += val
            self.fanta_f_entry.delete(0,"end")
            self.fanta_f_entry.insert(0, value)
            self.fanta_f_entry.config(state=tk.DISABLED)
        def minus_1(val):
            self.fanta_f_entry.config(state=tk.NORMAL)
            if self.fanta_f_entry.get() == "0":
                pass
            else:
                value = int(self.fanta_f_entry.get())
                value -= val
                self.fanta_f_entry.delete(0,"end")
                self.fanta_f_entry.insert(0, value)
            self.fanta_f_entry.config(state=tk.DISABLED)
        # Plus (-)
        self.fanta_f_minus = tk.Button(self.drink_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_1(1))
        self.fanta_f_minus.place(x=22, y=144)
        # Entry []
        self.fanta_f_entry = tk.Entry(self.drink_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.fanta_f_entry.config(state=tk.NORMAL)
        self.fanta_f_entry.insert(0,0)
        self.fanta_f_entry.config(state=tk.DISABLED)
        self.fanta_f_entry.place(x=47, y=158)
        # Plus (+)
        self.fanta_f_plus = tk.Button(self.drink_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_1(1))
        self.fanta_f_plus.place(x=97, y=144)

        # (2) </> Iced Milo </>
        self.icedmilo_img = Image.open(pathdrink_img+"Iced Milo.png")
        self.icedmilo_img = self.icedmilo_img.resize((100,100), Image.ANTIALIAS)
        self.icedmilo_photoImg = ImageTk.PhotoImage(self.icedmilo_img)
        self.icedmilo = tk.Label(self.drink_frame, image=self.icedmilo_photoImg, text="Iced Milo\nRp. 12,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.icedmilo.grid(row=0, column=1, padx=1, pady=(0,41))
        # </> Amount Button </>
        def plus_2(val):
            self.icedmilo_entry.config(state=tk.NORMAL)
            value = int(self.icedmilo_entry.get())
            value += val
            self.icedmilo_entry.delete(0,"end")
            self.icedmilo_entry.insert(0, value)
            self.icedmilo_entry.config(state=tk.DISABLED)
        def minus_2(val):
            if self.icedmilo_entry.get() == "0":
                pass
            else:
                value = int(self.icedmilo_entry.get())
                value -= val
                self.icedmilo_entry.delete(0,"end")
                self.icedmilo_entry.insert(0, value)
        # Plus (-)
        self.icedmilo_minus = tk.Button(self.drink_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_2(1))
        self.icedmilo_minus.place(x=172, y=144)
        # Entry []
        self.icedmilo_entry = tk.Entry(self.drink_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.icedmilo_entry.config(state=tk.NORMAL)
        self.icedmilo_entry.insert(0,0)
        self.icedmilo_entry.config(state=tk.DISABLED)
        self.icedmilo_entry.place(x=197, y=158)
        # Plus (+)
        self.icedmilo_plus = tk.Button(self.drink_frame ,text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_2(1))
        self.icedmilo_plus.place(x=247, y=144)

        # (3) </> Hot Coffee </>
        self.hotcoffee_img = Image.open(pathdrink_img+"Hot Coffee.png")
        self.hotcoffee_img = self.hotcoffee_img.resize((100,100), Image.ANTIALIAS)
        self.hotcoffee_photoImg = ImageTk.PhotoImage(self.hotcoffee_img)
        self.hotcoffee = tk.Label(self.drink_frame, image=self.hotcoffee_photoImg, text="Hot Coffee\nRp. 11,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.hotcoffee.grid(row=0, column=2, padx=1, pady=(0,41))
        # </> Amount Button </>
        def plus_3(val):
            self.hotcoffee_entry.config(state=tk.NORMAL)
            value = int(self.hotcoffee_entry.get())
            value += val
            self.hotcoffee_entry.delete(0,"end")
            self.hotcoffee_entry.insert(0, value)
            self.hotcoffee_entry.config(state=tk.DISABLED)
        def minus_3(val):
            self.hotcoffee_entry.config(state=tk.NORMAL)
            if self.hotcoffee_entry.get() == "0":
                pass
            else:
                value = int(self.hotcoffee_entry.get())
                value -= val
                self.hotcoffee_entry.delete(0,"end")
                self.hotcoffee_entry.insert(0, value)
            self.hotcoffee_entry.config(state=tk.DISABLED)
        # Plus (-)
        self.hotcoffee_minus = tk.Button(self.drink_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_3(1))
        self.hotcoffee_minus.place(x=320, y=144)
        # Entry []
        self.hotcoffee_entry = tk.Entry(self.drink_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.hotcoffee_entry.config(state=tk.NORMAL)
        self.hotcoffee_entry.insert(0,0)
        self.hotcoffee_entry.config(state=tk.DISABLED)
        self.hotcoffee_entry.place(x=344, y=158)
        # Plus (+)
        self.hotcoffee_plus = tk.Button(self.drink_frame, text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_3(1))
        self.hotcoffee_plus.place(x=394, y=144)

        # (4) </> Sprite </>
        self.sprite_img = Image.open(pathdrink_img+"Sprite.png")
        self.sprite_img = self.sprite_img.resize((100,100), Image.ANTIALIAS)
        self.sprite_photoImg = ImageTk.PhotoImage(self.sprite_img)
        self.sprite = tk.Label(self.drink_frame, image=self.sprite_photoImg, text="Sprite\nRp. 8,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.sprite.grid(row=0, column=3, padx=1, pady=(0,41))
        # </> Amount Button </>
        def plus_4(val):
            self.sprite_entry.config(state=tk.NORMAL)
            value = int(self.sprite_entry.get())
            value += val
            self.sprite_entry.delete(0,"end")
            self.sprite_entry.insert(0, value)
            self.sprite_entry.config(state=tk.DISABLED)
        def minus_4(val):
            self.sprite_entry.config(state=tk.NORMAL)
            if self.sprite_entry.get() == "0":
                pass
            else:
                value = int(self.sprite_entry.get())
                value -= val
                self.sprite_entry.delete(0,"end")
                self.sprite_entry.insert(0, value)
            self.sprite_entry.config(state=tk.DISABLED)
        # Plus (-)
        self.sprite_minus = tk.Button(self.drink_frame)
        self.sprite_minus.config(text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_4(1))
        self.sprite_minus.place(x=470, y=144)
        # Entry []
        self.sprite_entry = tk.Entry(self.drink_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.sprite_entry.config(state=tk.NORMAL)
        self.sprite_entry.insert(0,0)
        self.sprite_entry.config(state=tk.DISABLED)
        self.sprite_entry.place(x=495, y=158)
        # Plus (+)
        self.sprite_plus = tk.Button(self.drink_frame)
        self.sprite_plus.config(text="+", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_4(1))
        self.sprite_plus.place(x=545, y=144)

        # (5) </> Hot Tea </>
        self.hottea_img = Image.open(pathdrink_img+"Hot Tea.png")
        self.hottea_img = self.hottea_img.resize((100,100), Image.ANTIALIAS)
        self.hottea_photoImg = ImageTk.PhotoImage(self.hottea_img)
        self.hottea = tk.Label(self.drink_frame, image=self.hottea_photoImg, text="Hot Tea\nRp. 11,000", width=140, height=140, font=('verdana',13,'bold'), compound=tk.TOP, bg="white", relief="flat")
        self.hottea.grid(row=0, column=4, padx=1, pady=(0,41))
        # </> Amount Button </>
        def plus_5(val):
            self.hottea_entry.config(state=tk.NORMAL)
            value = int(self.hottea_entry.get())
            value += val
            self.hottea_entry.delete(0,"end")
            self.hottea_entry.insert(0, value)
            self.hottea_entry.config(state=tk.DISABLED)
        def minus_5(val):
            self.hottea_entry.config(state=tk.NORMAL)
            if self.hottea_entry.get() == "0":
                pass
            else:
                value = int(self.hottea_entry.get())
                value -= val
                self.hottea_entry.delete(0,"end")
                self.hottea_entry.insert(0, value)
            self.hottea_entry.config(state=tk.DISABLED)
        # Plus (-)
        self.hottea_minus = tk.Button(self.drink_frame, text="-", font=('verdana',16,'bold'),width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:minus_5(1))
        self.hottea_minus.place(x=618, y=144)
        # Entry []
        self.hottea_entry = tk.Entry(self.drink_frame, state=tk.DISABLED, font=('verdana',10,'bold'), justify=tk.CENTER, width=5, disabledbackground="white", disabledforeground="black", relief="flat")
        self.hottea_entry.config(state=tk.NORMAL)
        self.hottea_entry.insert(0,0)
        self.hottea_entry.config(state=tk.DISABLED)
        self.hottea_entry.place(x=642, y=158)
        # Plus (+)
        self.hottea_plus = tk.Button(self.drink_frame, text="+", font=('verdana',16,'bold'), width=1 , height=1, bg="white", fg="blue", relief="flat", command=lambda:plus_5(1))
        self.hottea_plus.place(x=692, y=144)

    def bills_log_options(self):
        # </> BILLS LABEL FRAME </>
        self.bills_frame = tk.LabelFrame(self.master)
        self.bills_frame.config(
            text = "Biils Log", 
            font = ('calibri',12,'bold'), 
            borderwidth = 3, 
            relief = "ridge",
            width = 500,
            height =500, 
            highlightthickness = 2,
            highlightcolor = "white",
            highlightbackground = "white",
            background = "white",
            foreground = "#DA291C"
        )
        self.bills_frame.place(x=800, y=113)

        # </> WELCOME TEXT </>
        self.welcome_lb = tk.Label(self.bills_frame, text="BILL DETAIL", font=('verdana',20,'bold'), bg="white", fg="black")
        self.welcome_lb.grid(row=0, column=0,pady=(2,10))

        # </> TEXT BILLS DETAIL </>
        self.bill_detail = tk.Text(self.bills_frame, state=tk.DISABLED, height=25, width=56, relief="flat")
        self.bill_detail.grid(row=1, column=0, padx=20)

        # </> TOTAL </>
        # TOTAL LABEL
        tk.Label(self.master, text="TOTAL: Rp. ", font=('verdana',18,'bold'), bg="white", fg="black").place(x=800, y=607)
        self.total = 0
        self.total_price_lbl = tk.Label(self.master, text=self.total, font=('verdana',18,'bold'), bg="white", fg="black")
        self.total_price_lbl.place(x=955, y=607)
        # TOTAL BUTTON 
        self.total_btn = tk.Button(self.master, text=" TOTAL ", width=7, font=('verdana',17,'bold'), bg="#DA291C", fg="black", command=self.total_bills_script)
        self.total_btn.place(x=1178, y=600)

        # </> MONEY CHANGE </>
        # MONEY CHANGE LABEL
        tk.Label(self.master, text="CHANGE: Rp. ", font=('verdana',18,'bold'), bg="white", fg="black").place(x=800, y=662)
        self.money_change = 0
        self.money_change_lbl = tk.Label(self.master, text=self.money_change, font=('verdana',18,'bold'), bg="white", fg="black")
        self.money_change_lbl.place(x=979, y=662)
        # MONEY CHANGE BUTTON
        self.money_change_btn = tk.Button(self.master, text="CHANGE", width=7, font=('verdana',17,'bold'), bg="#DA291C", fg="black", command=self.change_window)
        self.money_change_btn.place(x=1178, y=660)

    def right_bar_options(self):
        # </> RIGHT BAR </>
        self.right_bar = tk.Label(self.master, width=6, bg="#DA291C")
        self.right_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.right_bar.pack_propagate(0)
        
        # </> CLEAR BUTTON </>
        self.clear_btn = tk.Button(self.right_bar, text="C", font=("verdana",17,"bold"), bg="#DA291C", fg="yellow", relief="flat", command=self.clearall_script)
        self.clear_btn.pack(side=tk.TOP, fill=tk.Y)

        # </> EXIT BUTTON </>
        self.exit_btn = tk.Button(self.right_bar, text="X", font=("verdana",17,"bold"), bg="#DA291C", fg="yellow", relief="flat", command=root.quit)
        self.exit_btn.pack(side=tk.BOTTOM, fill=tk.Y)

        # </> ABOUT BUTTON </>
        self.about_btn = tk.Button(self.right_bar, text="?", font=("verdana",17,"bold"), bg="#DA291C", fg="yellow", relief="flat", command=self.aboutapp_window)
        self.about_btn.pack(side=tk.BOTTOM,fill=tk.Y)

    def total_bills_script(self):
        # FOOD PRICE
        self.bigmac_price = 35000
        self.panas1_price = 32000
        self.panas_s_price = 38000
        self.mcchicken_price = 28500
        self.mcnuggets_price = 27000
        self.chicken_f_price = 13000
        self.mcspicy_price = 36000
        self.beefburger_price = 22500
        self.pamer5_price = 108000
        self.pamer7_price = 157000
        # DRINK PRICE
        self.fanta_f_price = 12000
        self.icedmilo_price = 12000
        self.hotcoffee_price = 11000
        self.sprite_price = 8000
        self.hottea_price = 11000

        # </> SCRIPT CALCULATE </>
        # ==> FOOD <==
        # BARRIER
        self.bill_detail.config(state=tk.NORMAL)
        self.bill_detail.insert(tk.END, "========================================================\n=======================> (FOOD) <=======================\n")
        # BIG MAC
        if self.bigmac_entry.get() != "0":
            self.bigmac_cost = self.bigmac_price * int(self.bigmac_entry.get())
            self.bill_detail.insert(tk.END, (" Big Mac           x {}   = Rp. {}\n".format(self.bigmac_entry.get(), self.bigmac_cost)))
        else:
            self.bigmac_cost = 0
        # PANAS 1
        if self.panas1_entry.get() != "0":
            self.panas1_cost = self.panas1_price * int(self.panas1_entry.get())
            self.bill_detail.insert(tk.END, (" PaNas1            x {}   = Rp. {}\n".format(self.panas1_entry.get(), self.panas1_cost)))
        else:
            self.panas1_cost = 0
        # PANAS SPECIAL
        if self.panas_s_entry.get() != "0":
            self.panas_s_cost = self.panas_s_price * int(self.panas_s_entry.get())
            self.bill_detail.insert(tk.END, (" Panas Spesial     x {}   = Rp. {}\n".format(self.panas_s_entry.get(), self.panas_s_cost)))
        else:
            self.panas_s_cost = 0       
        # MC CHICKEN
        if self.mcchicken_entry.get() != "0":
            self.mcchicken_cost = self.mcchicken_price * int(self.mcchicken_entry.get())
            self.bill_detail.insert(tk.END, (" McChicken         x {}   = Rp. {}\n".format(self.mcchicken_entry.get(), self.mcchicken_cost)))
        else:
            self.mcchicken_cost = 0
        #  MC NUGGETS
        if self.mcnuggets_entry.get() != "0":
            self.mcnuggets_cost = self.mcnuggets_price * int(self.mcnuggets_entry.get())
            self.bill_detail.insert(tk.END, (" McNuggets         x {}   = Rp. {}\n".format(self.mcnuggets_entry.get(), self.mcnuggets_cost)))
        else:
            self.mcnuggets_cost = 0
        # CHICKEN FINGERS
        if self.chicken_f_entry.get() != "0":
            self.chicken_f_cost = self.chicken_f_price * int(self.chicken_f_entry.get())
            self.bill_detail.insert(tk.END, (" Chicken Fingers   x {}   = Rp. {}\n".format(self.chicken_f_entry.get(), self.chicken_f_cost)))
        else:
            self.chicken_f_cost = 0       
        # MC SPICY
        if self.mcspicy_entry.get() != "0":
            self.mcspicy_cost = self.mcspicy_price * int(self.mcspicy_entry.get())
            self.bill_detail.insert(tk.END, (" McSpicy           x {}   = Rp. {}\n".format(self.mcspicy_entry.get(), self.mcspicy_cost)))
        else:
            self.mcspicy_cost = 0       
        # BEEF BURGER
        if self.beefburger_entry.get() != "0":
            self.beefburger_cost = self.beefburger_price * int(self.beefburger_entry.get())
            self.bill_detail.insert(tk.END, (" Beef Burger       x {}   = Rp. {}\n".format(self.beefburger_entry.get(), self.beefburger_cost)))
        else:
            self.beefburger_cost = 0      
        # PAMER 5
        if self.pamer5_entry.get() != "0":
            self.pamer5_cost = self.pamer5_price * int(self.pamer5_entry.get())
            self.bill_detail.insert(tk.END, (" PaMer5            x {}   = Rp. {}\n".format(self.pamer5_entry.get(), self.pamer5_cost)))
        else:
            self.pamer5_cost = 0 
        # PAMER 7
        if self.pamer7_entry.get() != "0":
            self.pamer7_cost = self.pamer7_price * int(self.pamer7_entry.get())
            self.bill_detail.insert(tk.END, (" PaMer7            x {}   = Rp. {}\n".format(self.pamer7_entry.get(), self.pamer7_cost)))
        else:
            self.pamer7_cost = 0

        # ==> DRINK <==
        # BARRIER
        self.bill_detail.insert(tk.END, "========================================================\n=======================> (DRINK) <======================\n")
        # FANTA MCFLOAT
        if self.fanta_f_entry.get() != "0":
            self.fanta_f_cost = self.fanta_f_price * int(self.fanta_f_entry.get())
            self.bill_detail.insert(tk.END, (" Fanta McFloat     x {}   = Rp. {}\n".format(self.fanta_f_entry.get(), self.fanta_f_cost)))
        else:
            self.fanta_f_cost = 0
        # ICED MILO
        if self.icedmilo_entry.get() != "0":
            self.icedmilo_cost = self.icedmilo_price * int(self.icedmilo_entry.get())
            self.bill_detail.insert(tk.END, (" Iced Milo         x {}   = Rp. {}\n".format(self.icedmilo_entry.get(), self.icedmilo_cost)))
        else:
            self.icedmilo_cost = 0
        # HOT COFFEE
        if self.hotcoffee_entry.get() != "0":
            self.hotcoffee_cost = self.hotcoffee_price * int(self.hotcoffee_entry.get())
            self.bill_detail.insert(tk.END, (" Hot Coffee        x {}   = Rp. {}\n".format(self.hotcoffee_entry.get(), self.hotcoffee_cost)))
        else:
            self.hotcoffee_cost = 0
        # SPRITE
        if self.sprite_entry.get() != "0":
            self.sprite_cost = self.sprite_price * int(self.sprite_entry.get())
            self.bill_detail.insert(tk.END, (" Sprite            x {}   = Rp. {}\n".format(self.sprite_entry.get(), self.sprite_cost)))
        else:
            self.sprite_cost = 0
        # HOT TEA
        if self.hottea_entry.get() != "0":
            self.hottea_cost = self.hottea_price * int(self.hottea_entry.get())
            self.bill_detail.insert(tk.END, (" Hot Tea           x {}   = Rp. {}\n".format(self.hottea_entry.get(), self.hottea_cost)))
        else:
            self.hottea_cost = 0

        # BARRIER
        self.bill_detail.insert(tk.END, "========================================================\n")
        self.bill_detail.insert(tk.END, "========================================================\n\n")
        # TOTAL ALL BILLS 
        self.total_all_bills = self.bigmac_cost + self.panas1_cost + self.panas_s_cost + self.mcchicken_cost + self.mcnuggets_cost + self.chicken_f_cost + self.mcspicy_cost + self.beefburger_cost + self.pamer5_cost + self.pamer7_cost + self.fanta_f_cost + self.icedmilo_cost + self.hotcoffee_cost + self.sprite_cost + self.hottea_cost
        # TOTAL PRICE
        self.price = self.total_all_bills
        self.bill_detail.insert(tk.END, (" TOTAL: Rp. {}\n".format(self.price)))
        #self.bill_detail.insert(tk.END, "========================================================")
        self.total_price_lbl.config(text=self.price)
        self.bill_detail.config(state=tk.DISABLED)

    def clearall_script(self):
        # </> MAKE ALL STATE NORMAL </>
        self.bill_detail.config(state=tk.NORMAL)
        # FOOD
        self.bigmac_entry.config(state=tk.NORMAL)
        self.panas1_entry.config(state=tk.NORMAL)
        self.panas_s_entry.config(state=tk.NORMAL)
        self.mcchicken_entry.config(state=tk.NORMAL)
        self.mcnuggets_entry.config(state=tk.NORMAL)
        self.chicken_f_entry.config(state=tk.NORMAL)
        self.mcspicy_entry.config(state=tk.NORMAL)
        self.beefburger_entry.config(state=tk.NORMAL)
        self.pamer5_entry.config(state=tk.NORMAL)
        self.pamer7_entry.config(state=tk.NORMAL)
        # DRINK
        self.fanta_f_entry.config(state=tk.NORMAL)
        self.icedmilo_entry.config(state=tk.NORMAL)
        self.hotcoffee_entry.config(state=tk.NORMAL)
        self.sprite_entry.config(state=tk.NORMAL)
        self.hottea_entry.config(state=tk.NORMAL)
        # </> CLEAR ALL </>
        self.bill_detail.delete(1.0, tk.END) # </> BILL DETAIL </>
        # </> FOOD </>
        self.bigmac_entry.delete(0, tk.END)
        self.bigmac_entry.insert(0, 0)
        self.panas1_entry.delete(0, tk.END)
        self.panas1_entry.insert(0, 0)
        self.panas_s_entry.delete(0, tk.END)
        self.panas_s_entry.insert(0, 0)
        self.mcchicken_entry.delete(0, tk.END)
        self.mcchicken_entry.insert(0, 0)
        self.mcnuggets_entry.delete(0, tk.END)
        self.mcnuggets_entry.insert(0, 0)
        self.chicken_f_entry.delete(0, tk.END)
        self.chicken_f_entry.insert(0, 0)
        self.mcspicy_entry.delete(0, tk.END)
        self.mcspicy_entry.insert(0, 0)
        self.beefburger_entry.delete(0, tk.END)
        self.beefburger_entry.insert(0, 0)
        self.pamer5_entry.delete(0, tk.END)
        self.pamer5_entry.insert(0, 0)
        self.pamer7_entry.delete(0, tk.END)
        self.pamer7_entry.insert(0, 0)
        # </> DRINK </>
        self.fanta_f_entry.delete(0, tk.END)
        self.fanta_f_entry.insert(0, 0)
        self.icedmilo_entry.delete(0, tk.END)
        self.icedmilo_entry.insert(0, 0)
        self.hotcoffee_entry.delete(0, tk.END)
        self.hotcoffee_entry.insert(0, 0)
        self.sprite_entry.delete(0, tk.END)
        self.sprite_entry.insert(0, 0)
        self.hottea_entry.delete(0, tk.END)
        self.hottea_entry.insert(0, 0)
        # </> CLEAR TOTAL and CHANGE</>
        self.total_price_lbl.config(text=self.total)
        self.money_change_lbl.config(text=self.money_change)
        
        # </> MAKE ALL STATE DISABLED </>
        self.bill_detail.config(state=tk.DISABLED)
        # FOOD
        self.bigmac_entry.config(state=tk.DISABLED)
        self.panas1_entry.config(state=tk.DISABLED)
        self.panas_s_entry.config(state=tk.DISABLED)
        self.mcchicken_entry.config(state=tk.DISABLED)
        self.mcnuggets_entry.config(state=tk.DISABLED)
        self.chicken_f_entry.config(state=tk.DISABLED)
        self.mcspicy_entry.config(state=tk.DISABLED)
        self.beefburger_entry.config(state=tk.DISABLED)
        self.pamer5_entry.config(state=tk.DISABLED)
        self.pamer7_entry.config(state=tk.DISABLED)
        # DRINK
        self.fanta_f_entry.config(state=tk.DISABLED)
        self.icedmilo_entry.config(state=tk.DISABLED)
        self.hotcoffee_entry.config(state=tk.DISABLED)
        self.sprite_entry.config(state=tk.DISABLED)
        self.hottea_entry.config(state=tk.DISABLED)

    def change_window(self):
        self.changewindow = tk.Toplevel(root)
        self.changewindow.title("Money Change")
        self.changewindow.config(bg="#DA291C")
        self.changewindow.lift()
        self.changewindow.focus_force()
        self.changewindow.attributes("-topmost", True)
        self.changewindow.grab_set()
        self.changewindow.overrideredirect(True)
        # </> CENTER WINDOW SCRIPT </>
        windowc_w = 380
        windowc_h = 392
        screenc_w = root.winfo_screenwidth()
        screenc_h = root.winfo_screenheight()
        positionc_top = int(screenc_h/2 - windowc_h/2)
        positionc_right = int(screenc_w/2 - windowc_w/2)
        self.changewindow.geometry(f"{windowc_w}x{windowc_h}+{positionc_right}+{positionc_top}")
        # </> END </>
        # </> CHANGE DISPLAY SCRIPT </>
        def press(num):
            self.entry_c.insert(tk.END, num)
        def change_enter():
            try:
                self.bill_detail.config(state=tk.NORMAL)
                self.money_c = int(self.entry_c.get())
                self.calculate_change = self.price - self.money_c
                self.total_change = abs(self.calculate_change)
                self.bill_detail.insert(tk.END,(" CHANGE: Rp. {}".format(self.total_change)))
                #self.bill_detail.insert(tk.END, (" TOTAL: Rp. {}\n".format(self.price)))
                self.money_change_lbl.config(text=self.total_change)
                self.bill_detail.config(state=tk.DISABLED)
                self.changewindow.destroy()
            except:
                pass

        # ENTRY AND BUTTON 
        tk.Label(self.changewindow, text="Money Change", font=("verdana",15,"bold"), fg="white", bg="#DA291C").grid(row=0, column=0, pady=11, columnspan=4)
        self.entry_c = tk.Entry(self.changewindow, font=("verdana",20,"bold"), fg='yellow', bg='black', width=19, borderwidth=5)
        self.entry_c.grid(row=1, column=0, columnspan=4, padx=5, pady=(0,15))
        tk.Button(self.changewindow, text='1', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(1), height=1, width=5).grid(row=2, column=0, sticky='nesw') 
        tk.Button(self.changewindow, text='2', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(2), height=1, width=5).grid(row=2, column=1, sticky='nesw') 
        tk.Button(self.changewindow, text='3', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(3), height=1, width=5).grid(row=2, column=2, sticky='nesw') 
        tk.Button(self.changewindow, text='4', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(4), height=1, width=5).grid(row=3, column=0, sticky='nesw') 
        tk.Button(self.changewindow, text='5', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(5), height=1, width=5).grid(row=3, column=1, sticky='nesw') 
        tk.Button(self.changewindow, text='6', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(6), height=1, width=5).grid(row=3, column=2, sticky='nesw') 
        tk.Button(self.changewindow, text='7', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(7), height=1, width=5).grid(row=4, column=0, sticky='nesw') 
        tk.Button(self.changewindow, text='8', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(8), height=1, width=5).grid(row=4, column=1, sticky='nesw') 
        tk.Button(self.changewindow, text='9', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(9), height=1, width=5).grid(row=4, column=2, sticky='nesw') 
        tk.Button(self.changewindow, text='0', font=("verdana",25,"bold"), fg='yellow', bg='#DA291C', command=lambda:press(0), height=1, width=5).grid(row=5, column=1, sticky='nesw')
        tk.Button(self.changewindow, text='Back', font=("verdana",15,"bold"), fg='yellow', bg='#DA291C', command=self.changewindow.destroy, height=1, width=5).grid(row=5, column=0, sticky='nesw')
        tk.Button(self.changewindow, text='Enter', font=("verdana",15,"bold"), fg='yellow', bg='#DA291C', command=change_enter, height=1, width=5).grid(row=5, column=2, sticky='nesw')

    def aboutapp_window(self):
        self.aboutwindow = tk.Toplevel(root)
        self.aboutwindow.title("McDonald's")
        self.aboutwindow.config(bg="black")
        self.aboutwindow.focus_force() # FOCUS WINDOW
        self.aboutwindow.lift()
        self.aboutwindow.attributes("-topmost", True)
        self.aboutwindow.grab_set() # MAKE WINDOW FOCUS CANT ACCSES OTHER WINDOW
        self.aboutwindow.overrideredirect(True) # REMOVE WINDOW TOP BAR
        #</> CENTER WINDOW SCRIPT </>
        window_w = 350
        window_h = 200
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        position_top = int(screen_h/2 -window_h/2)
        position_right = int(screen_w / 2 - window_w/2)
        self.aboutwindow.geometry(f"{window_w}x{window_h}+{position_right}+{position_top}")
        # </> END </>

        # </> LABEL TEXT </>
        tk.Label(self.aboutwindow, text="McDonald's", font=('Berlin Sans FB',20), bg="black", fg="white").pack(side=tk.TOP, pady=(10,0))
        tk.Label(self.aboutwindow, text="Author : Kisah Tegar\nversion 2021.01.01", font=('Berlin Sans FB',10,"bold"), bg="black", fg="white").pack(pady=(80,0))
        # </> EXIT BUTTON </>
        tk.Button(self.aboutwindow, text="Exit", width=7, font=('verdana',10,'bold'), bg="#DA291C", fg="white", command=self.aboutwindow.destroy).pack(side=tk.BOTTOM, padx=10, pady=10)

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master.attributes("-fullscreen", True)
        self.master.title("McDonald's")
        self.master.configure(bg='white')
        # </> All classes </>
        MainPage(self).pack() # MAIN PAGE

if __name__ == '__main__':
    root = tk.Tk()
    MainApplication(root).pack()
    root.mainloop()