from tkinter import Frame, Tk, Button, Label, Entry,messagebox
import datetime


class PowerCut():

    _CUT_TIME_:list = []

    def getPowerCutTime(self):
        window = Tk()
        window.title("Power Cut")
        window.geometry("280x70")

        time_label = Label(window, text="Power Cut Time:", font=("Arial",10,"bold"))
        time_label.grid(row=0, column=0, padx=5 , pady=20) 

        hour_entry = Entry(window, width=5)  
        hour_entry.grid(row=0, column=1)

        minute_entry = Entry(window, width=5)
        minute_entry.grid(row=0, column=2,padx=5)

        def close_dialog():
            try:
                self._CUT_TIME_ = [hour_entry.get(),minute_entry.get()]
                print("Power Cut Time: " + str(self._CUT_TIME_))
            except ValueError:
                messagebox.showinfo("PowerCut","Time is not entred")    
            window.destroy() 

        get_button = Button(window, text=" OK" ,foreground="blue" , borderwidth=0 , command=close_dialog)
        get_button.grid(row=0, column=3, pady=10)
        

        window.mainloop()
    def checkPowerCutTime(self):
        minute = datetime.datetime.now().minute
        hour = datetime.datetime.now().hour
        print(str(hour), str(minute) )
        while(True):
            if( hour == int(self._CUT_TIME_[0]) and minute == int(self._CUT_TIME_[1])):
                 print("\a")
                 messagebox.showwarning("Power Cut", "Power cut time , Save all files......" )
                 break
            minute = datetime.datetime.now().minute
            hour = datetime.datetime.now().hour





if __name__ == "__main__":
    powerCut = PowerCut()
    powerCut.getPowerCutTime()
    powerCut.checkPowerCutTime()