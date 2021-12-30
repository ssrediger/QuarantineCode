from concurrent import futures

import grpc

import lobby_pb2
import lobby_pb2_grpc

class Lobby(lobby_pb2_grpc.LobbyServicer):
    def ConnectToLobby(self, request, context):
        print(request.name)
        resp = lobby_pb2.ConnectResponse(accepted=False,idToken=45)
        return resp
    def GetGameList(self, request, context):
        return super().GetGameList(request, context)

    def JoinGameQueue(self, request, context):
        return super().JoinGameQueue(request, context)

    def ExitGameQueue(self, request, context):
        return super().ExitGameQueue(request, context)

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lobby_pb2_grpc.add_LobbyServicer_to_server(Lobby(),server)
    server.add_insecure_port("[::]:12345")
    server.start()
    server.wait_for_termination()




