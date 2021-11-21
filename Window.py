# -*- codding:utf-8 -*-
from tkinter import *
from tkinter import StringVar

from Logic import Search_engine

class Window(Tk):
    search_text: StringVar

    def __init__(self):
        super().__init__()
        self.db_Search = Search_engine()
        Label(self, text="Введіть пошуковий запит:").grid(
            row=0, column=0, columnspan=2)

        #Frame and insides:
        self.f1 = Frame(self,height=300,width = 200,bg='#81d4fa')


        #StringVars
        self.var_name = StringVar()
        self.var_author= StringVar()
        self.var_album= StringVar()
        self.var_long= StringVar()
        self.var_rBut=IntVar()
        self.var_name.set("Назва обраної пісні")
        self.var_author.set("Автор")
        self.var_album.set("Назва альбому")
        self.var_long.set("Тривалість")
        self.var_rBut.set(0)

        self.numberOfScreenUnits = 190

        #Labels
        self.name_lable = Label(self.f1,textvariable = self.var_name,font = "Roboto 12",wraplength=self.numberOfScreenUnits)
        self.author = Label(self.f1,textvariable = self.var_author,font = "Roboto 12",wraplength=self.numberOfScreenUnits)
        self.album_name = Label(self.f1,textvariable = self.var_album,font = "Roboto 12",wraplength=self.numberOfScreenUnits)
        self.long = Label(self.f1, textvariable = self.var_long,font = "Roboto 12")
        #Main entry and button:
        self.search_text = StringVar()
        self.entry_search = Entry(self,width=60,
                                  textvariable=self.search_text)
        self.search_but = Button(self,text='Search',
                                 command=self.change)
        #ListBox
        self.list = Listbox(self,width = 50,heigh = 20)
        self.list.bind("<Button-1>",self.list_select)
        #Scrollbsrs
        self.scroll_y = Scrollbar(command=self.list.yview)
        self.scroll_x = Scrollbar(command=self.list.xview,orient = HORIZONTAL)
        #scrollBars_set
        self.list.config(yscrollcommand=self.scroll_y.set,
                         xscrollcommand=self.scroll_x.set)
        #Radiobuttons
        self.rbut_name= Radiobutton(text="By name",variable=self.var_rBut, value=0)
        self.rbut_author = Radiobutton(text="By author",variable=self.var_rBut, value=1)
        self.rbut_ganre = Radiobutton(text="By genre",variable=self.var_rBut, value=2)

        #GRIDS
        self.entry_search.grid(row = 1,column = 0,columnspan=2)
        self.search_but.grid(row = 1,column = 2,sticky ="W")
        self.list.grid(row = 2,column=0,sticky="WE")
        self.scroll_y.grid(row = 2,column=1,sticky="WSN")
        self.scroll_x.grid(row = 3,column=0,sticky="WE")
        self.f1.grid(row=2,column=2,columnspan = 2,sticky = "SNWE")
        self.f1.grid_propagate(False)
        self.name_lable.grid(row = 0,rowspan = 2,padx = 5,pady = 5,sticky=W)
        self.author.grid(row = 3,padx = 5,pady = 5,sticky=W)
        self.album_name.grid(row = 4,padx = 5,pady = 5,sticky=W)
        self.long.grid(row = 5,padx = 5,pady = 5,sticky=W)
        self.rbut_name.grid(row=0,column=1,sticky=W)
        self.rbut_author.grid(row=0, column=2, sticky=W)
        self.rbut_ganre.grid(row=0, column=3, sticky=W)

    def change(self):
        if self.var_rBut.get() == 0:
            size = self.list.size()
            self.list.delete(0, size)
            text = self.search_text.get()
            self.result = self.db_Search.search_track(text)
            # insert to listbox:
            for i in self.result:
                self.list.insert(0, i[0])
        elif self.var_rBut.get() == 1:
            size = self.list.size()
            self.list.delete(0, size)
            text = self.search_text.get()
            self.result = self.db_Search.search_track_by_author(text)
            # insert to listbox:
            for i in self.result:
                self.list.insert(0, i[0])
        elif self.var_rBut.get() == 2:
            size = self.list.size()
            self.list.delete(0, size)
            text = self.search_text.get()
            self.result = self.db_Search.search_track_by_ganre(text)
            # insert to listbox:
            for i in self.result:
                self.list.insert(0, i[0])




#    def search(self):
#        size = self.list.size()
#        self.list.delete(0,size)
#        text = self.search_text.get()
#        self.result = self.db_Search.search_track(text)
##insert to listbox:
#        for i in self.result:
#            self.list.insert(0,i)

    def list_select(self,event=None):
        #Track Name
        select_num = self.list.curselection()
        try:
            self.select_info = self.list.get(select_num)
        except AttributeError:
            pass
        self.var_name.set(self.select_info)
        #Album
        text = self.select_info
        res_alb = self.db_Search.seearch_album(text)
        self.var_album.set(res_alb[0])
        #Author
        text = self.select_info
        res_auth = self.db_Search.search_artist(text)
        self.var_author.set(res_auth[0])
        #long
        text=self.select_info
        res_long = self.db_Search.search_long(text)
        self.var_long.set(res_long)

    #def search_author(self):
    #    text=self.select_info
    #    print(text)
    #    self.res_auth = self.db_Search.seearch_album(text)



if __name__ == "__main__":
    root = Window()
    root.geometry("600x400")
    root.mainloop()
