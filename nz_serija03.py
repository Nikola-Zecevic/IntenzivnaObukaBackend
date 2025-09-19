from functools import reduce
from datetime import datetime

def filter_lists(student_list, avg_grade_list):
    merged=list(zip(student_list,avg_grade_list))
    print(merged)
    result={x for x in merged if x[1]>8.5}
    return result

# a=["m","a","f","t","r"]
# b=[8,7,9,9,8.6]
# print(filter_lists(a,b))

def average_grade_by_subject(li):
    subjects=set(map(lambda x: x[2], li))
    result={}
    for subject in subjects:
        grades=list(map(lambda x: x[1], filter(lambda x: x[2]==subject, li)))
        sum_of_grades=reduce(lambda a,b:a+b, grades)
        result[subject]=sum_of_grades/len(grades)
    return result

student_data = [
    ("Alice", 2, "Math"),
    ("Bob", 10, "Science"),
    ("Charlie", 10, "History"),
    ("Diana", 10, "Math"),
    ("Eve", 10, "English"),
    ("Frank", 10, "Science"),
    ("Grace", 2, "Art"),
    ("Harry", 10, "Math"),
    ("Ivy", 10, "English"),
    ("Jack", 10, "History"),
    ("Karen", 10, "Science"),
    ("Liam", 10, "Music"),
    ("Mia", 10, "Math"),
    ("Noah", 10, "English"),
    ("Olivia", 10, "Science")
]
#print(average_grade_by_subject(student_data))


def append_to_file(list_of_students, file_path):
    try:
        with open(file_path, 'a') as file: 
            for student in list_of_students:
                item=f"{student["ime"]},{student["prezime"]},{student["godina"]},{student["prosjek"]}"
                file.write(item + '\n')
        print(f"List successfully appended to {file_path}")
    except IOError as e:
        print(f"Error appending to file: {e}")

def get_grade(grade):
    if grade>=9.5 and grade <=10:
        return "A"
    elif grade>=8.5 and grade <9.5:
        return "B"
    elif grade>=7.5 and grade <8.5:
        return "C"
    elif grade>=6.5 and grade <7.5:
        return "D"
    elif grade>=7.5 and grade <8.5:
        return "E"
    else:
        return "Error"



def get_students_with_greater_grade(year,grade,file_path):
    result=[]
    with open (file_path ,"r") as file:
        for line in file:
            list_of_student_info=line.strip().split(",")
            if int(list_of_student_info[2])==year and get_grade(float(list_of_student_info[3]))<=grade:
                student={}
                student["ime"]=list_of_student_info[0]
                student["prezime"]=list_of_student_info[1]
                student["godina"]=list_of_student_info[2]
                student["prosjek"]=list_of_student_info[3]                
                result.append(student)
    return result
studenti1=[
    {"ime": "Marko",   "prezime": "Markovic",  "godina": 2, "prosjek": 8.6 },
    {"ime": "Boris",   "prezime": "Boricic",   "godina": 3, "prosjek": 7.9 }, 
    {"ime": "Novak",   "prezime": "Novovic",   "godina": 3, "prosjek": 6.9 }]
#append_to_file(l,"studenti.txt")
studenti2 = [
    {"ime": "Marko",   "prezime": "Markovic",  "godina": 1, "prosjek": 6.0},   
    {"ime": "Ana",     "prezime": "Anic",      "godina": 8, "prosjek": 10.0},  
    {"ime": "Jovan",   "prezime": "Jovic",     "godina": 2, "prosjek": 6.5},
    {"ime": "Milica",  "prezime": "Milic",     "godina": 3, "prosjek": 7.0},   
    {"ime": "Petar",   "prezime": "Petrovic",  "godina": 4, "prosjek": 7.5},   
    {"ime": "Ivana",   "prezime": "Ivanovic",  "godina": 5, "prosjek": 8.0},   
    {"ime": "Nikola",  "prezime": "Nikolic",   "godina": 6, "prosjek": 8.5},   
    {"ime": "Sara",    "prezime": "Saric",     "godina": 7, "prosjek": 9.0},   
    {"ime": "Luka",    "prezime": "Lukic",     "godina": 8, "prosjek": 9.5},   
    {"ime": "Elena",   "prezime": "Lenic",     "godina": 1, "prosjek": 9.7},   
    {"ime": "Milos",   "prezime": "Milosevic", "godina": 2, "prosjek": 6.2},   
    {"ime": "Tamara",  "prezime": "Tomic",     "godina": 3, "prosjek": 7.8},   
    {"ime": "Stefan",  "prezime": "Stefanovic","godina": 4, "prosjek": 8.9},   
    {"ime": "Jelena",  "prezime": "Jelic",     "godina": 5, "prosjek": 9.3},   
    {"ime": "Filip",   "prezime": "Filipovic", "godina": 6, "prosjek": 6.8},   
    {"ime": "Maja",    "prezime": "Majic",     "godina": 7, "prosjek": 7.4},   
    {"ime": "Andrej",  "prezime": "Andric",    "godina": 8, "prosjek": 7.6},   
    {"ime": "Kristina","prezime": "Kovacevic", "godina": 1, "prosjek": 8.4},   
    {"ime": "Ognjen",  "prezime": "Ognjenovic","godina": 2, "prosjek": 9.6},   
    {"ime": "Dunja",   "prezime": "Dunic",     "godina": 3, "prosjek": 6.9}   
]
# append_to_file(studenti,"studenti.txt")
# print(get_students_with_greater_grade(2,"A","studenti.txt"))


"""(Dodatni) Kreirati fajl igrice.txt u kome se svaki igra, pojedinačno, čuva u jednom redu, tj. ako
imate unos od 5 igara, fajl treba da sadrži 5 linija. Fajl treba da sadži bar 10 igara. Igre prvo
unosite ručno (ne pomoću koda).
Svaka igra je opisana:

Nakon filtriranja u terminalu prikazati igre, a osim toga omogućiti korisniku, tj. pitati korisnika da li
želi da unese nove igre ili ne. Ne dozvoliti neispravan unos da ne bi moralo da se radi novo
filtriranje fajla. Prikazati odgovarajuću grešku u slučaju pogrešnog unosa i tražiti od korisnika da
ponovo unese igre ili da prekine unos. Nove igre se upisuju u fajl obavezno u ispravnom formatu
sa validnim vrijednostima atributa.
Nakon filtriranja i eventualnog unosa novih igara iz novog fajla potrebno je da učitate sve igre (u
tom fajlu igre bi trebalo da su pravilno unesene). Svaku igru potrebno pročitati iz fajla i sačuvati je
kao dictionary u listi igara, tj. Kreirati listu igara gdje je svaka igra dictionary oblika:
{naziv:string,ocjena:float_broj, godina:int_broj, izdavac:string zanrovi:lista_stringova}

Korisniku pri unosu napomenuti da su ocjene od 1 do 10, a osim toga treba napomenuti i koje
žanrove može da odabere. Ako korisnik unese podatke pogrešno, treba da mu se prikaže greška
i da mu se napomene da opet unosi novi input. Nakon tog filtriranja treba prikazati rezultate/igre u
terminalu
"""
"""Napisati dekorator koji koristi funkcionalni pristup za mjerenje vremena izvršavanja funkcije i
primenite ga na nekoliko različitih funkcija.

"""
GENRES=["Action", "Adventure", "RPG", "Strategy", "Simulation", "Sports", "Crime", "MOBA"]
class Game:
    def __init__(self, name, rating, release_year,genre, publisher=""):
        self.name=name
        self.rating=rating
        self.release_year=release_year
        self.publisher=publisher
        self.genre=genre
        # self._name=name
        # self._rating=rating
        # self._release_year=release_year
        # self._publisher=publisher
        # self._genre=genre

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if len(new_name)<2 or len(new_name)>50:
            raise ValueError("Name must be between 2 and 50 characters long")
        self._name=new_name

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, new_rating):
        if not(1<=new_rating<=10):
            raise ValueError("Rating must be between 1 and 10")
        self._rating=round(new_rating,2)

    @property
    def release_year(self):
        return self._release_year
    @release_year.setter
    def release_year(self, new_release_year):
        current_date_time = datetime.now()
        current_year = current_date_time.year
        if new_release_year<1950 or new_release_year>current_year:
            raise ValueError("Year must be between 1950 and this year")
        self._release_year=new_release_year

    @property
    def publisher(self):
        return self._publisher
    @publisher.setter
    def publisher(self, new_publisher):
        if new_publisher and not(2 <= len(new_publisher)<=50):
            raise ValueError("Publisher must be between 2 and 40 characters long")
        self._publisher=new_publisher

    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, new_genre):
        if not isinstance(new_genre,list):
            raise ValueError("genre must be a list of strings")
        if len(new_genre)<1 or len(new_genre)>3:
            raise ValueError("Name must be between 2 and 0 characters long")
        for g in new_genre:
            if g not in GENRES:
                raise ValueError(f"Genre {g}not allowed. Allowed genres are: {GENRES}")
        self._genre=new_genre
    def __repr__(self):
        return f"{self.name};{self.rating};{self.release_year};{self.publisher};{' '.join(self.genre)}"
    def to_dict(self):
        return {
            "naziv": self.name,
            "ocjena": self.rating,
            "godina": self.release_year,
            "izdavac": self.publisher,
            "zanrovi": self.genre
        }
    def __str__(self):
        return f"{self.name};{self.rating};{self.release_year};{self.publisher};{' '.join(self.genre)}"
    
def load_games(file_path):
    games=[]
    with open(file_path, "r") as file:
        for line in file:
            data=line.strip().split(";")
            try:
                game=Game(
                    name=data[0],
                    rating=float(data[1]),
                    release_year=int(data[2]),
                    publisher=data[3],

                    genre=data[4].split(" ")
                    )
                games.append(game)
            except Exception as e:
                print(f"Error in line{line.strip().split(";")} and {e}")
    return games

def add_game(file_path, game):
    with open(file_path, "a") as file:
        #file.write("\n")
        file.write(repr(game)+"\n")

def filter_by_name(games, prefix):
    return [game for game in games if game.name.lower().startswith(prefix.lower())]
def filter_by_rating(games,rating):
    return [game for game in games if game.rating>=rating]
def filter_by_year(games, year, before=True):
    if before:
        return [game for game in games if game.release_year<year]
    else:
        return [game for game in games if game.release_year>=year]
    
def filter_by_publisher(games,prefix):
    return [game for game in games if game.publisher.lower().startswith(prefix.lower())]

def filter_by_genre(games, wanted_genres):
    return [game for game in games if all(ge in game.genre for ge in wanted_genres)]

igrice=load_games("igrice.txt")
# for i in igrice:
#     print(i)
#     print()

# print(igrice[2])
#mine=Game(name="Mine",rating=3,release_year=2020,publisher="Ea",genre=["Adventure","Simulation"] )
# add_game(file_path="igrice.txt",game=mine)
# print(filter_by_name(igrice,"gta"))
# print(filter_by_publisher(igrice,"moj"))
# print(filter_by_rating(igrice,8))
# print(filter_by_year(igrice,2020, before=False))
print(filter_by_genre(igrice,["Action","Crime"]))
