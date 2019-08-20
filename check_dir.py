import os

def check_dir():
    try:
        os.mkdir('./data/')
        print("Error: keine Daten vorhanden")
        raise FileNotFoundError
    except OSError as e:
        pass
