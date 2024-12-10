import os
from datetime import datetime

def log(message):
    """
    Écrit un message dans le fichier logger.log avec un horodatage.

    :param message = str 
    """
    log_file_path = os.path.join(os.getcwd(), "logger.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

def showlog(log_file='logger.log'):
    """
    Affiche le contenu du fichier de log.

    Param:
    log_file (str): Le chemin vers le fichier de log (par défaut 'logger.log').
    """
    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()
            if logs:
                print("=== Logs ===")
                for log in logs:
                    print(log.strip())
            else:
                print("Le fichier de log est vide.")
    except FileNotFoundError:
        print(f"Le fichier {log_file} n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def read_logs():
    """Lit le fichier des logs."""
    try:
        with open("logger.log", "r") as log_file:
            return log_file.readlines()
    except FileNotFoundError:
        return ["Aucun log disponible."]