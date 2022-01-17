#Meta exercice
import os


def test_air00():
    fichier=os.popen('python air00.py "je vais bien"', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "je\nvais\nbien\n":
        print("air00 (1/1) : success")
    else: 
        print("air00 (1/1) : failure")

def test_air01():
    fichier=os.popen('python air01.py "Crevette magique dans la mer des étoiles" "la"', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "Crevette magique dans \nmer des étoiles ":
        print("air01 (1/1) : success")
    else: 
        print("air01 (1/1) : failure")

def test_air02():
    fichier=os.popen('python air02.py "je" "teste" "des" "trucs" " "', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "je teste des trucs ":
        print("air02 (1/1) : success")
    else: 
        print("air02 (1/1) : failure")

def test_air03():
    fichier=os.popen('python air03.py bonjour monsieur bonjour', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "monsieur\n" :
        print("air03 (1/1) : success")
    else: 
        print("air03 (1/1) : failure")

def test_air04():
    fichier=os.popen('python air04.py "Hello milady,   bien ou quoi ??"', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "Helo milady, bien ou quoi ?" :
        print("air04 (1/1) : success")
    else: 
        print("air04 (1/1) : failure")

def test_air05():
    fichier=os.popen('python air05.py 1 2 3 4 5 "+2"', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "3 4 5 6 7 " :
        print("air05 (1/1) : success")
    else: 
        print("air05 (1/1) : failure")

def test_air06():
    fichier=os.popen('python air06.py "Michel" "Albert" "Thérèse" "Benoit" "t"', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "Michel " :
        print("air06 (1/1) : success")
    else: 
        print("air06 (1/1) : failure")

def test_air07():
    fichier=os.popen('python air07.py  1 3 4 2', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "1 2 3 4 " :
        print("air07 (1/1) : success")
    else: 
        print("air07 (1/1) : failure")

def test_air08():
    fichier=os.popen('python air08.py  10 20 30 fusion 15 25 35', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "10 15 20 25 30 35 " :
        print("air08 (1/1) : success")
    else: 
        print("air08 (1/1) : failure")

def test_air09():
    fichier=os.popen('python air09.py "Michel" "Albert" "Thérèse" "Benoit"', "r")
    sortie = fichier.read()
    fichier.close()
    if sortie == "Albert, Thérèse, Benoit, Michel." :
        print("air09 (1/1) : success")
    else: 
        print("air09 (1/1) : failure")

def test_air10():
    fichier=os.popen('python air10.py air10.txt', "r")
    sortie = fichier.read()
    fichier.close()

    if sortie == "J'ai rÃ©ussi\n" :
        print("air10 (1/1) : success")
    else: 
        print("air10 (1/1) : failure")

def test_air11():
    fichier=os.popen('python air11.py o 2', "r")
    sortie = fichier.read()
    fichier.close()
    if sortie == "   o\n  ooo\n" :
        print("air11 (1/1) : success")
    else: 
        print("air11 (1/1) : failure")

def test_air12():
    fichier=os.popen('python air12.py 6 5 4 3 2 1', "r")
    sortie = fichier.read()
    fichier.close()
    if sortie == "1 2 3 4 5 6 " :
        print("air12 (1/1) : success")
    else: 
        print("air12 (1/1) : failure")

test_air00()
test_air01()
test_air02()
test_air03()
test_air04()
test_air05()
test_air06()
test_air07()
test_air08()
test_air09()
test_air10()
test_air11()
test_air12()
