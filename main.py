from database import Database
from ZoologicoDAO import ZoologicoDAO
from ZoologicoCLI import ZoologicoCLI

db = Database(database="Atividade", collection="Animais")
zoologicoDAO = ZoologicoDAO(database=db)

zoologicoCLI = ZoologicoCLI(zoologicoDAO)
zoologicoCLI.menu()
