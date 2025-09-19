def odnos(ob):
    return ob.get("br_pozitivni")/ob.get("br_negativni")

def najgori_odnos(li):
    najgori=li[0]
    for item in li:
        if odnos(item)<odnos(najgori):
            najgori=item
    return najgori["naziv"]
# a=[{"naziv":"Español para principiantes", "br_pozitivni":1000,"br_negativni":10},
# {"naziv":"Philophize This!", "br_pozitivni":500,"br_negativni": 30}, {"naziv":"Science VS. ",
# "br_pozitivni":600,"br_negativni": 45}]

# print(najgori_odnos(a))


"""

● Napisati glavni program koji koristi klasu Library za upravljanje inventarom knjiga.
Korisnik treba da može da izabere opcije za dodavanje, pregled, uređivanje i brisanje
knjiga iz biblioteke. Prilikom dodavanja knjige, program treba da omogući unos svih
potrebnih informacija o knjizi. Prilikom uređivanja knjige, korisnik treba da može da
izmeni bilo koji atribut knjige (naslov, autor, godina izdanja, broj kopija).
"""
class Book:
    def __init__(self, title, author, year, number_of_copies):
        self._title=title
        self._author=author
        self._year=year
        self._number_of_copies=number_of_copies

    def __str__(self):
        return f"{self._title} | {self._author} | {self._year}"# | Kopija: {self._number_of_copies}"


    @property
    def title(self):
        return self._title
    

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not new_title:
            raise ValueError("Title must be a non-empty string.")
        self._title = new_title


    @property
    def author(self):
        return self._author


    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, str) or not new_author:
            raise ValueError("Title must be a non-empty string.")
        self._author = new_author 
    

    @property
    def year(self):
        return self._year
    

    @year.setter
    def year(self, new_year):
        if not isinstance(new_year, int) or not new_year:
            raise ValueError("Year must be integer.")
        self._year = new_year

    
    @property
    def number_of_copies(self):
        return self._number_of_copies
    

    @number_of_copies.setter
    def number_of_copies(self, new_number_of_copies):
        if not isinstance(new_number_of_copies, int) or not new_number_of_copies:
            raise ValueError("Number of copies must be integer.")
        self._number_of_copies=new_number_of_copies


class Library:
    def __init__(self, book_list=[]):
        self._book_list=book_list
    

    def add_book(self, book):
        if not isinstance(book, Book) or not book:
            raise ValueError("Only books can be added to the library!")
        self._book_list.append(book)

    def delete_book(self, title):
        self._book_list = [book for book in self._book_list if book.title != title]

    def find_book(self, title):
        found=[book for book in self._book_list if book.title == title]
        return found
        
    
    def find_by_author(self, author):
        found=[book for book in self._book_list if book.author == author]
        return found
    
    def display(self):
        if not self._book_list:
            print("Library empty")
        for book in self._book_list:
            print(book)


"""Potrebno je da kreirate klasu Company koja ima 5 atributa: name (ime kompanije, string), area
(oblast djelovanja, string), employees (lista zaposlenih, svaki zaposleni je dictionary oblika
{“name”: “some_string”, “surname”:”some_string”, “salary”:”num” }) i balance (trenutni finansijskih
balans kompanije, float number), max_num_of_employees (prirodan broj koji predstavlja koliko
zaposlenih kompanija može maksimalno da ima).


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
    def __init__(self, name, area, balance, max_num_of_employees):
        self._name=name
        self._area=area
        self._employees=[]
        self._balance=balance
        self._max_num_of_employees=max_num_of_employees


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        self._name=new_name

    @property
    def area(self):
        return self._area
    
    @name.setter
    def area(self,new_area):
        self._area=new_area

    @property
    def balance(self):
        return self.balance
    
    @name.setter
    def balance(self,new_balance):
        if new_balance<0:
            raise ValueError("Balance must be positive!")
        else:
            self._balance=new_balance
        

    @property
    def max_num_of_employees(self):
        return self._max_num_of_employees
    
    @name.setter
    def max_num_of_employees(self,new_max_num_of_employees):
        if new_max_num_of_employees<0:
            raise ValueError("Number of employees must be positive!")
        else :
            self._max_num_of_employees=new_max_num_of_employees  


    def add_employee(self, employee):
        if self.max_num_of_employees>len(self.employees):
            self.employees.append(employee)
            return "Employee added!"
        else:
            return "You cannot add more employees"
   
