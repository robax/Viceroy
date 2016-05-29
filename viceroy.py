from xml.dom import minidom
from networking import net
from model import table

shit = """<endhand />
<table available=",,,,,,,," bb="50" bots=",,,,,,,," chips="6000,6550,13960,3147,6100,4639,31058,19230,6250" dealer="6" gold=",,,,,,,," max_bring="10000" nicks="i9iveup,lindaweaver,robax,Nino23killer,anihimi,tarnett,Drummer1946,26dealmein,Lorraine88" sb="25" spectators="2" states="p,p,p,p,p,p,p,p,p" user_ids="1002369,347098,1075655,1134695,773244,499282,368900,1050154,788799" />
<newhand hand="214009455" prev="214009253" /><pot pot="50" seat="5" total_pot="50" /><seat available="1" avatar_url="https://replaypoker.s3.amazonaws.com/assets/avatars/111296/medium/Picture_1178.jpg?1420709860" bot="" chips="4589" gold="" nick="tarnett" seat="5" state="p" /><playeraction action="post bb" amount="50" seat="5" /><noask /><table available=",,,,,,,," bb="50" bots=",,,,,,,," chips="6000,6550,13960,3147,6100,4589,31058,19230,6250" dealer="7" gold=",,,,,,,," max_bring="10000" nicks="i9iveup,lindaweaver,robax,Nino23killer,anihimi,tarnett,Drummer1946,26dealmein,Lorraine88" sb="25" spectators="2" states="p,p,p,p,p,p,p,p,p" user_ids="1002369,347098,1075655,1134695,773244,499282,368900,1050154,788799" />
<pretext pd1="Auto Post Blinds" pd2="Auto Muck Hands" pd3="Sit Out Next Hand" pd4="Fold To Any Bet" /><pre pre="pd1" show="true" state="1" /><pre pre="pd2" show="true" state="1" /><pre pre="pd3" show="true" state="0" /><pre pre="pd4" show="true" state="0" /><dealer seat="7" /><pot pot="25" seat="0" total_pot="75" /><seat available="1" avatar_url="https://replaypoker.s3.amazonaws.com/assets/avatars/222659/medium/296551_104926816277480_7462233_n.jpg?1455182001" bot="" chips="5975" gold="" nick="i9iveup" seat="0" state="p" /><playeraction action="post sb" amount="25" seat="0" /><pot pot="50" seat="1" total_pot="125" /><seat available="1" avatar_url="avatars/male.png" bot="" chips="6500" gold="" nick="lindaweaver" seat="1" state="p" /><playeraction action="post bb" amount="50" seat="1" /><chat from="" raw_text="" text="&lt;b&gt;Dealer&lt;/b&gt;: ** Hand [ 214009455 ] started **" type="dealer" /><pcard seat="0" /><pcard seat="1" />
<pcard card="jd" seat="2" /><pcard seat="3" /><pcard seat="4" /><pcard seat="5" /><pcard seat="6" /><pcard seat="7" /><pcard seat="0" /><pcard seat="1" /><pcard card="8c" seat="2" /><pcard seat="3" /><pcard seat="4" /><pcard seat="5" /><pcard seat="6" /><pcard seat="7" /><autopre end="1" /><endask /><endask /><ask allin="0" bb="50" display=",50,100" hand_id="214009455" maxraise="13960" quick_bet_labels="x2,x3,POT,ALL IN" quick_bet_values="100,150,225,13960" reply="fold,call,100" slide="1" text="FOLD,CALL,RAISE TO" /><timeout seat="2" seconds="19" />
"""

if __name__ == "__main__":
    print "Searching for port..."
    #port = net.findPort()
    #print "Port found! " , port
    #print "Searching for ip..."
    #ip = net.findIP()
    #print "ip found! " , ip
    table = table.Table()
    xmldoc = minidom.parse(shit)
    #while True:
    #    print net.getPacket(port, ip)

