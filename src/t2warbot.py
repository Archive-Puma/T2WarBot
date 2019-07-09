import io
import sys
import random
import tweepy

alumnos = list()

def processline(line):
    global alumnos
    # Format the line
    alumno = line.replace('\n','').strip()
    # Append the student
    if alumno != '':
        alumnos.append(alumno)

def rewritedoc(filename, loser):
    global alumnos
    
    alumnos.remove(loser)
    with io.open(filename, "w", encoding="utf-8") as alumnos_file:
        for alumno in alumnos:
            alumnos_file.write(alumno + '\n')

def deletesomeone():
    global alumnos
    # Select two random students
    p1 = random.randint(0, len(alumnos) - 1)
    p2 = random.randint(0, len(alumnos) - 1)
    while p1 == p2:
        p2 = random.randint(0, len(alumnos) - 1)
    
    winner = alumnos[p1]
    loser = alumnos[p2]

    return winner,loser

def interaction(winner, loser):
    interactions = [
        " ha neutralizado a ",
        " parecía que iba a perder, pero al final ha derrotado a ",
        " ha sacado pechito y ha conseguido que se retire ",
        ", tras una ardua batalla, ha conseguido derrotar a ",
        " ha hecho que se retire ",
        " parecía que no tenía mucho interés en esta batalla, pero ha conseguido ganarle a ",
        " puede que no destaque mucho en esta guerra, pero a conseguido ganarle a ",
        ", sin comerlo ni beberlo, ha derrotado a ",
        " ha derrotado, no sin previa fanfarronería, a ",
        " ha dicho que iba a ganar su próxima batalla y así ha sido. Otra vez será, ",
        ", quien vió peligrar su puesto de 'Promesa Revelación', derrotó a su competencia: una personilla llamada ",
        ", sin que nadie se diera cuenta, ha eliminado de la competición a ",
        ", con complejo de Khaleesi, no ha dudado en enviar a sus dragones contra ",
        " ha hackeado el @t2_war para eliminar de la lista a ",
        " se ha tropezado corriendo por los pasillos y ha eliminado a ",
        " ha eliminado, obligándole a recoger el aula, a ",
        " ha derrotado, usando esferificaciones en mal estado, a ",
        " no se ha cortado un pelo y ha tirado a la piscina a "
    ]
    interaction_number = random.randint(0,len(interactions) - 1)
    
    dialog = winner + interactions[interaction_number] + loser
    return dialog

def tweet(tweet_msg):
    CONSUMER_KEY = " == CENSORED == "
    CONSUMER_SECRET = " == CENSORED == "   
    ACCESS_KEY = " == CENSORED == "    
    ACCESS_SECRET = " == CENSORED == "

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    api.update_status(tweet_msg)


if __name__ == "__main__":
    # Specify the filename
    filename = str()
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "alumnos.txt"
    # Process the file
    with io.open(filename, "r", encoding="utf-8") as alumnos_file:
        for alumno in alumnos_file.readlines():
            processline(alumno)
    if len(alumnos) == 1:
        sys.exit(0)
    # Define the match
    winner, loser = deletesomeone()
    rewritedoc(filename, loser)
    dialog = interaction(winner, loser)
    tweet(dialog)
        