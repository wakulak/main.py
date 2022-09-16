from xml.etree.ElementTree import parse, Element, SubElement
import re
# from .main import select_file



class Rachunek():
    def __init__(self, spr_sygn):
        self.spr_sygn = spr_sygn
        self.ident = None
        self.nazwa = None
        self.data_dok = None
        self.data_skan= None
        self.pages=None
        self.id_wlas=None
        self.typ=None
        self.format=None
        
def ReadRachunki():
    global rachunki
    file = r"XML.xml"
    rachunki = list()
    doc = parse(file)
    root = doc.getroot()
    for rachunekElement in root.iterfind("Lista_skanowanych_dokumentów_row"):
        spr_sygn = rachunekElement.findtext("spr_sygn")
        rachunek = Rachunek(spr_sygn)
        rachunek.ident = rachunekElement.iter("ident")
        rachunek.data_dok = rachunekElement.findtext('data_dok')
        rachunek.nazwa = rachunekElement.findtext('nazwa')
        rachunek.data_skan = rachunekElement.findtext("data_skan")
        rachunek.pages = rachunekElement.iterfind("pages")
        rachunek.id_wlas = rachunekElement.iterfind('id_wlas')
        rachunek.typ=rachunekElement.iterfind('typ')
        rachunek.format=rachunekElement.findtext('format')
        rachunki.append(rachunek)
    return rachunki

class ZUS():
    def __init__(self, miasto, konto):
        self.miasto=miasto
        self.konto=konto
    def lista_spraw(self):
        ReadRachunki()
        for i in rachunki:
            p = re.compile(self.konto)
            s= (i.nazwa)
            result = p.findall(s)
            if result:
                a=list.append(i)
            print (a)
        return a


ZUS0=ZUS('Bydgoszcz', 92102055900000030290400010)
ZUS.lista_spraw()