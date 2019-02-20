import socket;
import logging;
from emoji import demojize;

# init
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s — %(message)s", datefmt="%Y-%m-%d_%H:%M:%S",
                    handlers=[logging.FileHandler("chat.log", encoding="utf-8")]);


server = "irc.chat.twitch.tv";
port = 6667;
token = "oauth:jlebhpfnk8go5fjz4n3ns6r8mhkm82";
nickname = "wengreyfabio";
channel = "#beyondthesummit"

def main() :
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\r\n".encode('utf-8'))

    try:
        while True:
            msg = sock.recv(2048).decode('utf-8');

            if msg.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'));
            elif len(msg) > 0:
                logging.info(demojize(msg));
                print(msg);

    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == "__main__" :
    main();
