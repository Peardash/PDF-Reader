from PyPDF2 import PdfFileReader, PdfFileWriter
import os

# making text file from pdf and printing all contents on it in the same folder under the name Lorem.txt
# we need pdffilereader and pdffilewriter functions from PyPDF2 library
file_path = 'Lorem.pdf'
pdf = PdfFileReader(file_path)

with open('Lorem Note.txt', 'w') as f:
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
    f.close()

file_path = input("Enter the file path: ")
while not os.path.exists(file_path):
    file_path = input("The path does not exist, try entering the file path again: ")

with open(file_path, mode='rt', encoding='utf-8') as f:
    text = f.read()

search_word = input("Enter the word you want to search: ")

if search_word in text:
    print()
    print(text.replace(search_word, '\033[44;33m{}\033[m'.format(search_word)))
else:
    print("Word not found")
