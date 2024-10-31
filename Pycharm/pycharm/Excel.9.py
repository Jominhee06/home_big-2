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
        device = TextConverter(rsrcmgr,retstr,laparams=laparams)
        fp = open(filepath, 'rb')
        password = None
        maxpages=0
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        caching =True
        pagenos=[page_no]

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            interpreter.process_page(page)

        page_text[page_no] = retstr.getvalue()

        fp.close()
        device.close()
        retstr.close()

    return page_text


if __name__ == "__main__":
    filename = "D:\\HT_24050211003_조민희\\pycharm\\north_korea_economic_growth.pdf"
    filepath = os.path.join(os.getcwd(), "data", filename)
    pdf_text = pdf_to_txt(filepath)

    text_file = os.path.join(os.getcwd(), "output", filename.split('.')[0]+".txt")
    f = open(text_file, 'w', -1, "utf-8")

    for k, v in pdf_text.items():
        first_row = "---------------------%s 페이지의 내용입니다---------------------\n" % k
        f.write(first_row + v)

    f.close()