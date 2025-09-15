
def odnos(ob):
    return ob.get("br_pozitivni")/ob.get("br_negativni")

def najgori_odnos(li):
    najgori=li[0]
    for item in li:
        if odnos(item)<odnos(najgori):
            najgori=item
    return najgori
# a=[{"naziv":"Español para principiantes", "br_pozitivni":1000,"br_negativni":10},
# {"naziv":"Philophize This!", "br_pozitivni":500,"br_negativni": 30}, {"naziv":"Science VS. ",
# "br_pozitivni":600,"br_negativni": 45}]

# print(najgori_odnos(a))


"""
Potrebno je implementirati jednostavnu biblioteku za upravljanje knjigama u programskom jeziku
Python. Biblioteka treba omogućiti dodavanje, pregled, uređivanje i brisanje knjiga iz inventara.
Potrebno je kreirati klasu Book i klasu Library.
● Svaka knjiga ima sledeće atribute: naslov, autor, godina izdanja i broj kopija u inventaru.
● Implementirati konstruktor klase Book koji će inicijalizovati atribute knjige. Implementirati
metode za dohvatanje i postavljanje svakog atributa knjige (geteri i seteri).
● Biblioteka (Library) treba da sadrži listu knjiga koje su dostupne u inventaru.
Implementirati metode za dodavanje knjige u inventar (Book objekat), brisanje knjige iz
inventara (po naslovu), pretragu knjiga po naslovu ili autoru i prikaz svih knjiga koje su
trenutno dostupne (naslov, autor i godina izdanja).
● Napisati glavni program koji koristi klasu Library za upravljanje inventarom knjiga.
Korisnik treba da može da izabere opcije za dodavanje, pregled, uređivanje i brisanje
knjiga iz biblioteke. Prilikom dodavanja knjige, program treba da omogući unos svih
potrebnih informacija o knjizi. Prilikom uređivanja knjige, korisnik treba da može da
izmeni bilo koji atribut knjige (naslov, autor, godina izdanja, broj kopija). Prilikom brisanja
knjige, program treba da ukloni knjigu iz inventara na osnovu naslova knjige. Prilikom
pretrage po naslovu ili autoru, program treba da prikaže sve knjige koje zadovoljavaju
kriterijum pretrage.
"""
class Book:
    def __init__(self, title,author,year,copy_number):
        self.title=title
        self.author=author
        self.year=year
        self.copy_number=copy_number
    


        


"""Potrebno je da kreirate klasu Company koja ima 5 atributa: name (ime kompanije, string), area
(oblast djelovanja, string), employees (lista zaposlenih, svaki zaposleni je dictionary oblika
{“name”: “some_string”, “surname”:”some_string”, “salary”:”num” }) i balance (trenutni finansijskih
balans kompanije, float number), max_num_of_employees (prirodan broj koji predstavlja koliko
zaposlenih kompanija može maksimalno da ima).
● Potrebno je kreirati konstruktor kojim se definišu vrijednosti svih atributa na zadate
vrijednosti. Pretpostavlja se da korisnik unosi ispravno informacije (ne treba raditi
validaciju). Vrijednost atributa employees je prazna lista []. Svi atributi su privatni.
● Potrebno je kreirati odgovarajuće getere i setere za sve atribute osim za atribut
employees. Pri postavljanju vrijednosti atributa balance i max_num_of_employees
onemogućiti postavljanje na vrijednosti koje su manje od 0.
● Kreirati metod add_employee sa jednim parametrom employee koji dodaje novog
zaposlenog u kompaniju. Zaposleni se upisuje u atribut employees kao dictionary gore
navedenog oblika (pomoć: samo je potrebno odraditi dodavanje employee argumenta,
koji je dictionary, u listu employees). Zaposlenog je moguće dodati u kompaniju jedino
ako se njegovim dodavanjem neće prekoračiti vrijednost atribura
max_num_of_employees.
● Kreirati metod remove_employee sa dva parametra employee_name i
employee_surname koji uklanja zaposlenog iz kompanije. Brisanje se radi na osnovu
kombinacije imena i prezimena zaposlenog. Pretpostaviti da u kompaniji ne postoje dva
zaposlena sa istom kombinacijom imena i prezimena.
Potrebno je implementirati funkciju __str__ koja vraća format stringa u kome se štampaju
informacije o kompaniji. “name”: “company_name”, “area”: “company_area”, “balance”:
“company_balance”
● Kreirati metod can_pay_employees koji vraća True ili False u zavisnosti od toga da li
kompanija ima dovoljno novca na računu (atribut balance) da isplati sve zaposlene.
● Potrebno je implementirati funkciju __gt__ koja vraća True ili False. Za kompaniju A se
kaže da je veća od kompanije B ako kompanija A ima više zaposlenih nego kompanija B.
● Potrebno je kreirati bar dvije instance klase Company i testirati sve metode koje ste
implementirali."""

class Company:
    def __init__(self,name,area,employees,balance, max_num_of_employees):
        self.name=name
        self.area=area
        self.employees=employees
        self.balance=balance
        self.max_num_of_employees=max_num_of_employees

    def add_employee(self, employee):
        if self.max_num_of_employees>len(self.employees):
            self.employees.append(employee)
            return "Employee added!"
        else:
            return "You cannot add more employees"
   
