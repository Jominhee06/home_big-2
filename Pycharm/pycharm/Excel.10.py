import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

def pdf_to_txt(filepath):

    fp = open(filepath, 'rb')
    fp_f = PyPDF2.PdfReader(fp)
    total_pages = len(fp_f.pages)

    page_text = {}
    for page_no in range(total_pages):

        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr,laparams=laparams)
        fp = open(filepath, 'rb')
        password = None
        maxpages = 0
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        caching = True
        pagenos = [page_no]

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            interpreter.process_page(page)

        page_text[page_no] = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()

    return page_text


folder_path = os.path.join(os.getcwd(), "data", "pdf")
file_list = os.listdir(folder_path)

for file_name in file_list:

    pdf_text = pdf_to_txt(folder_path + "\\" + file_name)
    text_file = os.path.join(folder_path, file_name.split('.')[0]+".hwp")
    f = open(text_file, "w", -1, "utf-8")

    for v in pdf_text.values():
        f.write(v)

    f.close()

    print("%s.hwp 파일이 저장되었습니다. \n" % file_name.split('.')[0])
