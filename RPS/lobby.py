from concurrent import futures

import grpc
import PlayerDB
import lobby_pb2
import lobby_pb2_grpc
import socket
import gameServer

##############################################################
GAME_NONE = 0
GAME_RPS = 1
##############################################################


class Lobby(lobby_pb2_grpc.LobbyServicer):
    
    def __init__(self):
        self.playerDB = PlayerDB.PlayerDB()
        self.rps_queue = []
        self.port = 56789
        self.ip = socket.gethostbyname(socket.gethostname())
    def ConnectToLobby(self, request, context):
        print(request.name)
        temp_id = self.playerDB.addPlayer(request.name)
        resp = lobby_pb2.ConnectResponse(accepted=True,idToken=temp_id)
        return resp

    def GetGameList(self, request, context):
        self.gameList = "1. Rock Paper Scissors" 
        resp = lobby_pb2.GameListResponse(gameList=self.gameList)
#    resp.gameList.extend(lobby_pb2.ROCK_PAPER_SCISSORS)
        return resp

    def JoinGameQueue(self, request, context):
        #check game type
        # check queue not empty
        # if empty return success and add to quueue
        # if not empty, create game, update player records with connect string, zero out queue
        if request.game == 1:
            if len(self.rps_queue) == 0:
                self.rps_queue.append(request.idToken)
                self.playerDB.addPlayerToQueue(request.idToken,request.game)
                resp = lobby_pb2.JoinGameQueueResponse(True,request.game)
                return resp
            else:
                server_address = '{}:{}'.format(self.ip,str(self.port))
                gameServer(server_address)
                self.playerDB.addPlayerToGame(self.queue[0],request.game)
                self.playerDB.addPlayerToGame(request.idToken,request.game)
                self.ExitGameQueue(self.rps_queue[0])
                self.ExitGameQueue(request.idToken)
                self.rps_queue = []
                resp = lobby_pb2.JoinGameQueueResponse(True,request.game)
                return resp
        else:
            pass 

    def ExitGameQueue(self, request, context):
        self.playerDB.removePlayerFromQueue(request.idToken)
        resp = lobby_pb2.ExitGameQueueResponse(True,request.idToken)
        return resp
if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    lobby_pb2_grpc.add_LobbyServicer_to_server(Lobby(),server)
    server.add_insecure_port("[::]:12345")
    server.start()
    print("Server Running")
    server.wait_for_termination()
    print("Server Closed")




