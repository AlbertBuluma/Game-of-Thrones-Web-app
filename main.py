import server
from config import PORT
import characters

if __name__ == '__main__':
    
    characters = characters.prepare_data()
    
    y = []
    for character in characters:
        y.append(character.write())
        
    server.chars = y
    server.run(PORT)