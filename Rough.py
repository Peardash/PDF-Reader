from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from tkinter import *
from tkinter import self

# making text file from pdf and printing all contents on it in the same folder under the name Bro.txt
# we need pdffilereader and pdffilewriter functions from PyPDF2 library
file_path = 'Bro.pdf'
pdf = PdfFileReader(file_path)
yo = ""
with open('Bro.txt', 'w', encoding="utf-8") as f:
    for page_num in range(pdf.numPages):
        print('Page: {0}'.format(page_num))
        pageObj = pdf.getPage(page_num)


        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
            yo += txt
    f.close()

# file_path = input("Enter the file path: ")
# while not os.path.exists(file_path):
#     file_path = input("The path does not exist, try entering the file path again: ")
file_path = 'C:\\Users\\Erazmo\\Desktop\\Everything Python\\PDFReader\\Bro.txt'
with open(file_path, mode='rt', encoding='utf-8') as f:
    text = f.read()

root = Tk()
root.title('PDFReader')
# root.iconbitmap("C:\\Users\\Erazmo\\Desktop\\Code Projects\\PDFReader\\PDFReaderIcon.ico")
root.geometry("400x400")

# creating label widget

myLabel = Label(root, text= yo)

# shoving it to the screen

myLabel.pack()

# word highlighting
self.Btn1 = Button(self.mainFrame,
                                        text="Highlight 's'",
                                        command=lambda: self.highlight("s"))
self.Btn1.grid(row=3, column=0, sticky="ns")
 
def highlight(self, seq):
        if "highlight" in self.textWidget.tag_names():
            self.textWidget.tag_delete("highlight")
        i = len(seq)
        idx = "1.0"
        while True:
            idx = self.textWidget.search(seq, idx, nocase=1, stopindex='end')
            if idx:
                idx2 = self.textWidget.index("%s+%dc" % (idx, i))
                self.textWidget.tag_add("highlight", idx, idx2)
                self.textWidget.tag_config("highlight", background="yellow")
                idx = idx2
            else: return

# loop for the graphical user interface
root.mainloop()
