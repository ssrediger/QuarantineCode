import grpc
from lobby_pb2_grpc import LobbyServicer
import lobby_pb2_grpc
import lobby_pb2
'''
if __name__ == '__main__':
    with grpc.insecure_channel("localhost:12345") as channel:
        stub = lobby_pb2_grpc.LobbyStub(channel)
        req = lobby_pb2.ConnectRequest(name='Gid')
        resp = stub.ConnectToLobby(req)
        if resp.accepted == True:
            print("{0}".format(resp.idToken))
        else:
            print("L")
'''

if __name__ == '__main__':
    with grpc.insecure_channel("localhost:12345") as channel:
        stub = lobby_pb2_grpc.LobbyStub(channel)
        req = lobby_pb2.ConnectRequest(name=input("What's your name?"))
        resp = stub.ConnectToLobby(req)
        idToken = resp.idToken
        print(str(idToken))
        gameQueued = None
        while True:
            inp = "" 
            while inp.lower() != "l" and inp.lower() != "j" and inp.lower() != "e":
                inp = input("What do you want to do? 'L','J','E'")
                if inp.lower() == "l":
                    glreq = lobby_pb2.GameListRequest()
                    glresp = stub.GetGameList(glreq)
                    print(glresp.gameList)
                elif inp.lower() == "j":
                    ginp = ""
                    while ginp != '1':
                        ginp = input("What game do you want to play? ('1' for RPS)")
                    gameQueued = int(ginp)
                    jqreq = lobby_pb2.JoinGameQueueRequest(idToken=idToken,game=int(ginp))
                    jqresp = stub.JoinGameQueue(jqreq)
                    print(jqresp.accepted)
                    
                elif inp.lower() == "e":
                    lqreq = lobby_pb2.ExitGameQueueRequest(idToken=idToken,gameIdToken=gameQueued) 
                    lqresp = stub.ExitGameQueue(lqreq)
                    gameQueued = None
                    print("dun")
                else:
                    pass