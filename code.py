from PyPDF2 import PdfFileReader
import csv

def extract_information(li):
    with open("books_info.csv",'w',encoding='utf-8',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=["Path","Title",'Author',"Creator","Producer","Number of Pages"])
        writer.writeheader()
       

        for i in li:
            with open(i, 'rb') as f:
                pdf = PdfFileReader(f)
                information = pdf.getDocumentInfo()
                number_of_pages = pdf.getNumPages()

    
                writer.writerow({"Path":str(i),"Title":information.title,"Author":str(information.author),"Creator":str(information.creator),"Producer":str(information.producer),"Number of Pages":str(number_of_pages)})

    
    print("Done")

if __name__ == '__main__':
    path = ['C:\\Users\\Azmain\\Downloads\\mindset.pdf','C:\\Users\\Azmain\\Downloads\\Tff.pdf','C:\\Users\\Azmain\\Downloads\\prejudice.pdf','C:\\Users\\Azmain\\Downloads\\False.pdf','C:\\Users\\Azmain\\Downloads\\crime.pdf']
    extract_information(path)
