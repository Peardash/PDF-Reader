# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# if __name__ == '__main__':
# import PyPDF2
# pdfFileObj = open('c:\\Desktop\Pythontest.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
# pdfFileObj.close()
# create variable for ease of use'
# filename = 'C:/Users/Erazmo/Desktop/Scheduling.txt'
# opening the desired file'
# file = open(filename, 'r')
# reading and outputting the contents in a string'
# file_text = filename.__str__()
# some syntax from the video'
# print(file_text)

# alternative method below
# r = read, r+ = read & write, w = write, a = append
# create a variable associated with opening the file
file_current = open("Scheduling.txt", "r")

# checks if file is readable (if you put "r" in the brackets above).
# If you put "w" the boolean value from file.readable would be false
print(file_current.readable())

# prints all content from the text file which is the variable 'file'
print(file_current.read())

# reads and prints text file line but puts each line in an array
# print(file_current.readlines())

# using a for-loop to read each line using read.lines command
# for file in file_current.readlines():
#     print(file_current)

# close the variable named file
file_current.close()
