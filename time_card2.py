from bluetooth.ble import BeaconService
import MySQLdb

class Beacon(object):
    
    def __init__(self, data, address):
        self._uuid = data[0] #uuidとはさっきのabみたいなやつ？そう！たぶんじっさいにはまあ、３２桁くらい
        self._major = data[1] #majorとは専門!?いやなんかデータだけど、気にせんでいいやつこんなかだとrssiくらいかな大事そうなんは
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]#信号強度（距離見たいなもん）
        self._address =address
        
    def __str__(self):
        ret = "Beacon: address:{ADDR} uuid:{UUID} major:{MAJOR}"\
                " minor:{MINOR} txpower:{POWER} rssi:{RSSI}"\
                .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                        MINOR=self._minor, POWER=self._power, RSSI=self._rssi)
        return ret　　　#この関数何言ってるんすか?たぶんretの中身がBeacon address:ここに今の白いとこが来るわけよ

if __name__ == "__main__":
  db = MySQLdb.connect(host="localhost",user="Takasan",passwd="9230",db="time_card"
  user_name = []
  leave_user = []
  enter_user = []
  cur = db.cursor() #カーソル　これはおまじないな気がする俺はわからん
  sql_str = "SELECT Name FROM Employee;" #なにこれ?EMployeeのテーブルから名前を引っ張ってきてる
  if cur.execute(sql_str):
    user_name.append(cur.fetchall[0][0])
  while(1):
    sleep(1)
    for n in user_name:
      cur.execute("SELECT state FROM time_card WHERE timestamp = (SELECT max(timestamp) FROM time_card and Name ="+n+";")
      tmp=cur.fetchall[0][0]
      if tmp=="leave":
        leave_user.append(tmp)
      else:
        enter_user.append(tmp)
    service = BeaconService()
    devices = service.scan(2)＃この辺の処理書き直す？　めちゃ汚いことになてる ちょっと待って、ねるのことでいっぱいで見逃したーー
    for address, data in list(devices.items()):
        flag = 0
        b = Beacon(data, address)
        print(b)
        for i in leave_user:
          if b._uuid==i:
            sql_str = "INSERT INTO time_card(Name,Time,State) VALUES(TEXT,TIME_STAMP,TEXT);"
        for i in enter_user:
          if b._uuid = i:
            flag= 1
        

    print("Done.")
  
  
