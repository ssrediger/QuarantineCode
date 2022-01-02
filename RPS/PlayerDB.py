class PlayerRecord:
    def __init__(self,name):
        self.name = name
        self.current_game = None
        self.game_queue = None



class PlayerDB:
    
    def __init__(self):
        self.new_id = 123456789
        self.player_db = {}

    def addPlayer(self,name):
        self.new_id += 1
        self.player_db.update({self.new_id:PlayerRecord(name)})
        return self.new_id
        
    def getPlayer(self, id):
        return self.player_db[id]

    def addPlayerToQueue(self,id,game):
        self.player_db[id].game_queue = game

    def removePlayerFromQueue(self,id):
        self.player_db[id].game_queue = None

    def addPlayerToGame(self,id,game):
        self.player_db[id].current_game = game

    def removePlayerFromGame(self,id):
        self.player_db[id].current_game = None

