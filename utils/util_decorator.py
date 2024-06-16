import json
from functools import wraps

'''
Une fonction de décoration ou décorateur est une fonction qui modifie le comportement d'une autre fonction.
Elle prend une fonction en argument puis retourne une nouvelle fonction avec le comportement modifié.

Par exemple, et de manière très simplifiée :
Imaginons la fonction de décoration "do_twice(func)" qui prends une fonction et qui l'a fais deux fois.

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


et une fonction basique print_frite() avec le décorateur do_twice:
@do_twice
def print_frite():
    print("frite")

résultat :
>>> print_frite()
frite
frite

Cela permet d'avoir des petites fonctions "utilitaires" pour le développement (save_to_json, timer, etc)
'''


#Nom de la fonction de décoration avec l'argument 'file_path'
def save_to_json(file_path):
    #Fonction decorator avec en argument une fonction
    def decorator(func):
        #fonction de décoration @wraps permettant de garder les méta-données sur la fonction
        @wraps(func)
        def wrapper(*args, **kwargs):
            #appel de la fonction décoré et sauvegarde du résultat
            result = func(*args, **kwargs)
            #sauvegarde du résultat dans un fichier json avec comme file_path un chemin donné
            with open(file_path, 'w') as json_file:
                json.dump(result, json_file, indent=4)
            return result
        return wrapper
    return decorator
