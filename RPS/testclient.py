import grpc
import lobby_pb2_grpc
import lobby_pb2

if __name__ == '__main__':
    with grpc.insecure_channel("localhost:12345") as channel:
        stub = lobby_pb2_grpc.LobbyStub(channel)
        req = lobby_pb2.ConnectRequest(name='Gid')
        resp = stub.ConnectToLobby(req)
        if resp.accepted == True:
            print("{0}".format(resp.idToken))
        else:
            print("L")