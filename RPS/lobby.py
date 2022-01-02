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
        self.playerDB = PlayerDB()
        self.rps_queue = []
        self.port = 56789
        self.ip = socket.gethostbyname(socket.gethostname())
    def ConnectToLobby(self, request, context):
        print(request.name)
        temp_id = self.playerDB.addPlayer(request.name)
        resp = lobby_pb2.ConnectResponse(accepted=True,idToken=temp_id)
        return resp

    def GetGameList(self, request, context):
        resp = lobby_pb2.GameListResponse()
        resp.gameList.extend(lobby_pb2.ROCK_PAPER_SCISSORS)
        return resp

    def JoinGameQueue(self, request, context):
        #check game type
        # check queue not empty
        # if empty return success and add to quueue
        # if not empty, create game, update player records with connect string, zero out queue
        if request[1] == 1:
            if len(self.rps_queue) == 0:
                self.rps_queue.append(request[1])
                self.playerDB.addPlayerToQueue(request[0],request[1])
                return True
            else:
                server_address = '{}:{}'.format(self.ip,str(self.port))
                gameServer(server_address)
                self.playerDB.addPLayerToGame(self.queue[0],request[1])
                self.playerDB.addPLayerToGame(request[0],request[1])
                self.rps_queue = []






        else:
            pass 

    def ExitGameQueue(self, request, context):
        return super().ExitGameQueue(request, context)

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    lobby_pb2_grpc.add_LobbyServicer_to_server(Lobby(),server)
    server.add_insecure_port("[::]:12345")
    server.start()
    server.wait_for_termination()





