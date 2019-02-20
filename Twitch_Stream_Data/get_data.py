from datetime import datetime;
import re;
import pandas as pd;

def get_data(file) :
    data = [];
    with open(file, "r", encoding="utf-8") as fl :
        text = fl.read().split("\n");

        for line in text :

            try :

                time_logged = line.split()[0].strip()
                time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

                message = line.split('—')[1:];

                resp = '—'.join(message).strip();

                # ':spappygram!spappygram@spappygram.tmi.twitch.tv PRIVMSG #ninja :Chat, let Ninja play solos'
                username, chanel, msg = re.search( ":(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)", resp).groups();

                d = {
                    "Username" : username,
                    "Channel" : chanel,
                    "Message" : msg,
                    "Time" : time_logged
                };

                data.append(d);

            except Exception as e :
                print(e)
                pass;

    return pd.DataFrame().from_records(data);

