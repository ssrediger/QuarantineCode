class PlayerRecord:
    def __init__(self,name):
        self.name = name
        self.current_game = None
        self.game_queue = None



class PlayerDB:
    
    def __init__(self):
        self.new_id = 0
        self.player_db = {}

    def addPlayer(self,name):
        self.player_db.update({self.new_id:PlayerRecord(name)})
        self.new_id += 1

    def getPlayer(self, id):
        return self.player_db[id]

    def addPlayerToQueue(self,id,game):
        self.player_db[id].game_queue = game

    def removePlayerFromQueue(self,id):
        self.player_db[id].game_queue = None


test = PlayerDB()