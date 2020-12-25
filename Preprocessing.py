from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from nltk.stem.porter import PorterStemmer
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
import csv
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle

lsh_dict_abst = {}
Conf_title = []

def convert_pdf_to_txt(path, index):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open("C:\\Users\\Parineeta\\Desktop\\MS\\256\\Project\\CVPR2019\\papers\\"+path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 1
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=1, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    #print("Before Pre-processing:",'\n',my_string)
    
    '''
    with open('C:\\Users\\steff\\Data.csv','w', newline='') as newFile:
        newFileWriter = csv.writer(newFile, lineterminator='\n')
        newFileWriter.writerow([text])
        newFileWriter.writerow([])
    '''

    # Preprocessing
    text = text.lower()
    text = re.sub(r'\w*\d\w*', '', text)
    text = re.sub(r'\[.*\]*', '', text)
    text = re.sub(r'/\[].,()?', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text_words = text.split()
    ps = PorterStemmer()
    #print(index)
    text_words = [ps.stem(word) for word in text_words 
                if not word in set(stopwords.words('english'))]
    final_text = ' '.join(text_words)
    #print("After Pre-processing", '\n', final_text)
    #print(final_text)
    lsh_dict_abst[index] = final_text
    Conf_title.append(path)
    fp.close()
    device.close()
    retstr.close()
    return text


files = []
for i in os.listdir("C:\\Users\\Parineeta\\Desktop\\MS\\256\\Project\\CVPR2019\\papers"):
    files.append(i)

index = 0
for file in files:
    if index == 1:
        break
    else:
        my_text = convert_pdf_to_txt(file, index)
    index += 1

print(lsh_dict_abst)
print("\n")
print(Conf_title)

pickle_out = open("Abstract_Data_Prep.pickle", "wb")
pickle.dump(lsh_dict_abst, pickle_out)
pickle_out.close()
