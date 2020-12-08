import json
from pyspark import SparkConf, SparkContext 
from pyspark.streaming import StreamingContext
from pyspark.sql.functions import lit
from pyspark.sql import SQLContext
import sys
from pyspark.sql.types import Row
from datetime import datetime




def f(x):
    d = {}
    for i in range(len(x)):
        d[str(i)] = x[i]
    return d

def calculate_Time(df2,time_played):
    for i in (df2.collect()[0].teamsData[0].formation.substitutions):
        playerId1 = i.playerOut
        time_played1 = i.minute
        playerId2 = i.playerIn
        time_played2 = 90 - i.minute
        list = [[playerId1,time_played1],[playerId2,time_played2]]
       # print(list)
        temp = spark.createDataFrame(list)
        time_played = time_played.union(temp)
    return time_played


'''
{"status": "Played", "roundId": 4405654, "gameweek": 2, "teamsData": 
    {"1610": 
        {"scoreET": 0, "coachId": 272869, "side": "away", "teamId": 1610, "score": 2, "scoreP": 0, "hasFormation": 1, 
        "formation": 
            {"bench": 
                [{"playerId": 3551, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 212651, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 291591, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 291594, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 254898, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 3360, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 38093, "ownGoals": "1", "redCards": "0", "goals": "0", "yellowCards": "0"}], 
            "lineup": 
                [{"playerId": 105333, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 3324, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 8625, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 8032, "ownGoals": "0", "redCards": "0", "goals": "2", "yellowCards": "87"}, 
                {"playerId": 135103, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 25553, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 14748, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "30"}, 
                {"playerId": 7892, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "38"}, 
                {"playerId": 31528, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 28291, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 3429, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}], 
            "substitutions": 
                [{"playerIn": 3360, "playerOut": 105333, "minute": 78}, 
                {"playerIn": 38093, "playerOut": 3324, "minute": 79}]}, 
        "scoreHT": 1}, 
    "1624": 
        {"scoreET": 0, "coachId": 292863, "side": "home", "teamId": 1624, "score": 1, "scoreP": 0, "hasFormation": 1, 
        "formation": 
            {"bench": 
                [{"playerId": 240070, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 402884, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 77536, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 65254, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 25804, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 14911, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 269676, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}], 
            "lineup": 
                [{"playerId": 210044, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "31"}, 
                {"playerId": 136441, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 8945, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 36, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "83"}, 
                {"playerId": 8717, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "88"}, 
                {"playerId": 54, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 13484, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 48, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "51"}, 
                {"playerId": 11152, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 61967, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}, 
                {"playerId": 25381, "ownGoals": "0", "redCards": "0", "goals": "0", "yellowCards": "0"}], 
            "substitutions": 
                [{"playerIn": 14911, "playerOut": 210044, "minute": 68}, 
                {"playerIn": 25804, "playerOut": 136441, "minute": 80}, 
                {"playerIn": 269676, "playerOut": 8945, "minute": 90}]}, 
        "scoreHT": 0}}, 
    "seasonId": 181150, "dateutc": "2017-08-20 15:00:00", "winner": 1610, "venue": "Wembley Stadium", "wyId": 2499737, 
    "label": "Tottenham Hotspur - Chelsea, 1 - 2", "date": "August 20, 2017 at 5:00:00 PM GMT+2", 
    "referees": 
        [{"refereeId": 378952, "role": "referee"}, 
        {"refereeId": 385005, "role": "firstAssistant"},
         {"refereeId": 386718, "role": "secondAssistant"},
          {"refereeId": 385909, "role": "fourthOfficial"}], 
          "duration": "Regular", "competitionId": 364}
'''
def calculate_Time_1(df2,time_played):
    for i in (df2.collect()[0].teamsData[0].formation.substitutions):
        playerId1 = i.playerOut
        time_played1 = i.minute
        playerId2 = i.playerIn
        time_played2 = 90 - i.minute
        list = [[playerId1,time_played1],[playerId2,time_played2]]
       # print(list)
        temp = spark.createDataFrame(list)
        time_played = time_played.union(temp)
    return time_played
##########################################################################################################################################

def filter_by_Match(rdd):

    record_file  = json.loads(rdd)
    a=True
    b=False
    try:
        temp =record_file["wyId"]
        #print(record)
        '''
        print("##################################")
        date = record["date"]
        date_obj = datetime.strptime(date, '%b %d %y, at %H:%M:%S %p ')
        print("##################################")
        return (match_Id , (date_obj))
        '''

        return a
    except:
        return b
##########################################################################################################################################
def filter_by_Event(rdd):

    record_file = json.loads(rdd)
    a=True
    b=False
    try:
        temp = record_file["eventId"]
        return a

    except:
        return b
##########################################################################################################################################
'''
{"eventId": 8, "subEventName": "Simple pass", 
    "tags": 
        [{"id": 1801}], "playerId": 8325, 
            "positions": [{"y": 53, "x": 49}, {"y": 51, "x": 36}], 
            "matchId": 2499720, "eventName": "Pass", "teamId": 1625, "matchPeriod": "1H", 
            "eventSec": 3.3586760000000027, "subEventId": 85, "id": 178147292}
'''
##########################################################################################################################################

def calculate_Events(rdd):
    record = json.loads(rdd)
    player_Id = record["playerId"]
    match_Id = record["matchId"]
    event_Id = record["eventId"]
    team_Id = record["teamId"]
    subevent=record["subEventId"]
    #Tags = record["tags"]
    tags = [i["id"] for i in record["tags"]]
    #print(Tags)
    acc_pass=0
    in_acc_pass=0
    key_acc_pass=0
    key_inacc_pass=0
    dual_lost=0
    dual_nuetral=0
    dual_won=0
    fk_acc=0
    fk_unacc=0
    penalty = 0
    on_target=0
    not_on_target=0
    goal=0
    fouls = 0
    own_goal = 0

    if(event_Id == 8):
        flag = 0
        if (1801 in tags):
            flag=1
            acc_pass=acc_pass+1
        if (1802 in tags):
            flag=2
            in_acc_pass=in_acc_pass+1
        if (302 in tags):
            if(flag==1):
                key_acc_pass=key_acc_pass+1
            elif(flag==2):
                key_inacc_pass=key_inacc_pass+1
           
    elif(event_Id == 1):
        if(701 in tags):
            dual_lost +=1
        if(702 in tags):
            dual_nuetral +=1
        if(703 in tags):
            dual_won +=1


    elif (event_Id == 3):
        if(101 in tags):
            if subevent==35:
                penalty += 1
        if(1801 in tags):
            fk_acc=fk_acc+1
        if(1802 in tags):
            fk_unacc=fk_unacc+1

    elif(event_Id == 10):
        if(101 in tags):
            goal +=1
        if(1801 in tags):
            on_target +=1
        if(1802 in tags):
            not_on_target +=1


    elif(event_Id == 2):
        fouls+=1

    if(102 in tags):
        own_goal +=1

    return (player_Id, ((player_Id, match_Id, team_Id), (acc_pass, in_acc_pass, key_acc_pass, key_inacc_pass), (dual_lost ,dual_won, dual_nuetral) ,
             (fk_acc, fk_unacc, penalty), (on_target, not_on_target, goal), (fouls) , (own_goal) ))

    #return (player_Id, (player_Id, match_Id, team_Id) , (acc_pass, in_acc_pass, key_acc_pass, key_inacc_pass, dual_lost ,dual_won, dual_nuetral
    #        , fk_acc, fk_unacc, penalty , on_target, not_on_target, goal ,fouls , own_goal))

##########################################################################################################################################


# (8285, ((8285, 2499728, 1627), (1, 0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), 0, 0))

def cummulate_Metrics(new, old):
    acc_pass=0
    in_acc_pass=0
    key_acc_pass=0
    key_inacc_pass=0

    dual_lost=0
    dual_nuetral=0
    dual_won=0

    fk_acc=0
    fk_unacc=0
    penalty = 0

    on_target=0
    not_on_target=0
    goal=0

    fouls = 0

    own_goal = 0
     
    player_Id = 0
    match_Id = 0
    team_Id = 0
    #print(new)
    #print("##############################################")
    
    for metric in new:
        player_Id = metric[0][0]
        match_Id = metric[0][1]
        team_Id = metric[0][2]
        acc_pass += metric[1][0]
        in_acc_pass += metric[1][1]
        key_acc_pass += metric[1][2]
        key_inacc_pass += metric[1][3]
        dual_lost += metric[2][0]
        dual_nuetral += metric[2][1]
        dual_won += metric[2][2]
        fk_acc += metric[3][0]
        fk_unacc += metric[3][1]
        penalty += metric[3][2]
        on_target += metric[4][0]
        not_on_target += metric[4][1]
        goal += metric[4][2]
        fouls += metric[5]
        own_goal += metric[6]
    
    if (old is None) or (old[0][1] != match_Id):
    
        return  ((player_Id, match_Id, team_Id), (acc_pass, in_acc_pass, key_acc_pass, key_inacc_pass), (dual_lost ,dual_won, dual_nuetral) ,
            (fk_acc, fk_unacc, penalty), (on_target, not_on_target, goal), (fouls) , (own_goal) )
    else:
        #player_Id = old[0][0]
        #match_Id = old[0][1]
        #team_Id = old[0][2]
        acc_pass += old[1][0]
        in_acc_pass += old[1][1]
        key_acc_pass += old[1][2]
        key_inacc_pass += old[1][3]
        dual_lost += old[2][0]
        dual_nuetral += old[2][1]
        dual_won += old[2][2]
        fk_acc += old[3][0]
        fk_unacc += old[3][1]
        penalty += old[3][2]
        on_target += old[4][0]
        not_on_target += old[4][1]
        goal += old[4][2]
        fouls += old[5]
        own_goal += old[6]
    
        return ( ((player_Id , match_Id, team_Id), (acc_pass, in_acc_pass, key_acc_pass, key_inacc_pass), (dual_lost ,dual_won, dual_nuetral) ,
            (fk_acc, fk_unacc, penalty), (on_target, not_on_target, goal), (fouls) , (own_goal) ))

def calculate_Metrics(new,old):
    metric = new[0]
    #print(metric)
    #print("################################################")
    
    player_Id = metric[0][0]
    match_Id = metric[0][1]
    team_Id = metric[0][2]
    acc_pass = metric[1][0]
    in_acc_pass = metric[1][1]
    key_acc_pass = metric[1][2]
    key_inacc_pass = metric[1][3]
    dual_lost = metric[2][0]
    dual_nuetral = metric[2][1]
    dual_won = metric[2][2]
    fk_acc = metric[3][0]
    fk_unacc = metric[3][1]
    penalty = metric[3][2]
    on_target = metric[4][0]
    not_on_target = metric[4][1]
    goal = metric[4][2]
    fouls = metric[5]
    own_goal = metric[6]

    try:
        pass_accuracy=float((acc_pass-key_acc_pass+(key_acc_pass*2)))/float((acc_pass+in_acc_pass-key_acc_pass-key_inacc_pass+(key_acc_pass+key_inacc_pass)*2))
    except:
        pass_accuracy = 0
    try:
        deul_effeciency=float((dual_won + (dual_nuetral*0.5)))/float((dual_won+dual_lost+dual_nuetral))
    except:
        deul_effeciency = 0
    try:
        fk_effectiveness=float(fk_acc+penalty)/float(fk_acc+fk_unacc)
    except:
        fk_effectiveness=0
    try:
        shots_target=float(goal+((on_target-goal)*0.5))/float(on_target+not_on_target+goal)
    except: 
        shots_target = 0
    
    #return ((0,0,0))
    return ((player_Id , match_Id, team_Id) , (pass_accuracy, deul_effeciency, fk_effectiveness, shots_target, fouls, own_goal,goal)  )

def player_list(rdd):
    player_json_data=json.loads(rdd)
    group_teams_data=player_json_data['teamsData']
    for i in group_teams_data:
        data_team=group_teams_data[i]
        substitution_data= group_teams_data[i]['formation']['substitutions']

        Players_inc=[]
        Players_out=[]
        st=[]
        final_data=[]
        for j in substitution_data:
            Players_inc.append(j["playerIn"])
            Players_out.append(j["playerOut"])
            st.append(j["minute"])
        playing_11=[]
        not_playing_11=[]
        for j in data_team['formation']['lineup']:
            playing_11.append(j['playerId'])
        for j in data_team['formation']['bench']:
            not_playing_11.append(j['playerId'])
        for j in playing_11:
            try:
                final_data.append((j,(0,st[Players_out.index(j)],(st[Players_out.index(j)]))))
            except:
                final_data.append((j,(0,90,90)))
        for j in not_playing_11:
            try:
                final_data.append((j,(st[Players_inc.index(j)],90,90-st[Players_inc.index(j)])))
            except:
                final_data.append((j,(-1,-1,-1)))
    return final_data

def RateplayerUpdate(new_value,old_value):
    """
    (8032,(((8032, 2499721, 1610), (0.8974358974358975, 0.56, 1.0, 0.16666666666666666, 2, 0,goal)), (0, 90, 90)))
    ((player_Id , match_Id, team_Id) , (pass_accuracy, deul_effeciency, fk_effectiveness, shots_target, fouls, own_goal)  )
    new[1]=(((8032, 2499721, 1610), (0.8974358974358975, 0.56, 1.0, 0.16666666666666666, 2, 0)), (0, 90, 90))
    new[1][0]=((8032, 2499721, 1610), (0.8974358974358975, 0.56, 1.0, 0.16666666666666666, 2, 0))
    new[1][0][0]=(8032, 2499721, 1610)

    ((8032, 2499721, 1610), (0.8974358974358975, 0.56, 1.0, 0.16666666666666666, 2, 0)), (0, 90, 90)
    """
    # print(new_value)
    # print(old_value)
    try:
        team_id=new_value[0][0][0][2]
        match_id=new_value[0][0][0][1]
        player_id=new_value[0][0][0][0]

        time_spent=new_value[0][1][2]

        pass_accuracy=new_value[0][0][1][0]
        deul_effeciency=new_value[0][0][1][1]
        fk_effectiveness=new_value[0][0][1][2]
        shots_target=new_value[0][0][1][3]
        fouls=new_value[0][0][1][4]
        own_goal=new_value[0][0][1][5]

        goal=new_value[0][0][1][-1]

        #return (player_id)
        if (old_value is None):
            Old_Rating=0.5
        else:
            Old_Rating = old_value[1]
            #print(Old_Rating)
        #print(Old_Rating)
        print("###########################################")
        temp_value=pass_accuracy+deul_effeciency+shots_target+fk_effectiveness
        
        #print(temp_value)
        #print("###########################################")
        player_contribution=float(temp_value)/float(4)
        #print(player_contribution)
        #print("###########################################")
        
        if(time_spent == 90):
            player_contribution = float(player_contribution) * 1.05
        else:
            player_contribution = float(player_contribution) * float(time_spent)/float(90)

        #print(time_spent)
        #print("###########################################")
        Performance = player_contribution - ((0.005 * fouls) * player_contribution)
        Performance = player_contribution - ((0.05 * own_goal) * player_contribution)

        #print(Performance)
        #print("###########################################")
        New_Rating = float(Performance + Old_Rating) / float(2)

        Change_in_Rating = New_Rating - Old_Rating
        return (player_id, New_Rating , Change_in_Rating, team_id)

    except:
        return old_value

def profileplayerUpdate(new_value,old_value):
    try:
        #print(new_value)
        #print(old_value)
        
        if(old_value is None):
            player_Id = new_value[0][0][0]
            #new_value=[new_value]
            fouls = new_value[0][1][4]
            goals = new_value[0][1][6]
            own_goals = new_value[0][1][5]
            pass_accuracy = new_value[0][1][0]
            shots_target = new_value[0][1][3]
        else:
            #new_value=[new_value]
            #old_value=[old_value]
            #print("new------------",new_value[0][0][1])
            #print("new------------",old_value[0])
            player_Id = new_value[0][0][0]
            new_fouls=new_value[0][1][4] + old_value[0][0]
            new_goals=new_value[0][1][6] + old_value[0][1]
            new_own_goals=new_value[0][1][5] + old_value[0][2]
            new_pass_accuracy=new_value[0][1][0] + old_value[0][3] 
            new_shots_target= new_value[0][1][3] + old_value[0][4]
            fouls = new_fouls
            goals = new_goals
            own_goals = new_own_goals
            pass_accuracy =new_pass_accuracy
            shots_target = new_shots_target
        
        return (player_Id,fouls,goals,own_goals, pass_accuracy, shots_target)
    except:
        return old_value    

def convert_store(rdd):
     df=rdd.toDF(['id','metric'])
   #  df.show()
     df.coalesce(1).write.json("profile.json","overwrite")

def chem_calculate(rdd):
    dictionary_val=rdd.collect()
    print(dictionary_val)
    print("################################################")
    for i in dictionary_val:
        for j in dictionary_val:
            if(i!=j and i[1][0]!=0 and j[1][0]!=0):
                new_rating=i[1][1]
                Change_in_chem=0
                #print(i)
                #print(j)
                #print("#####################################################")
                if (i[1][3]==j[1][3]):

                    Change_in_chem=float(abs((i[1][2]) + (j[1][2])))/float(2)
                    if ((i[1][2]<0 and j[1][2]<0) or (i[1][2]>0 and j[1][2]>0)):
                        Change_in_chem=Change_in_chem

                    else:
                        Change_in_chem=-(Change_in_chem)
                        print(i)
                        print(j)
                        print("#####################################################")
                else:
                    Change_in_chem=float(abs((i[1][2]) + (j[1][2])))/float(2)
                    if ((i[1][2]<0 and j[1][2]<0) or (i[1][2]>0 and j[1][2]>0)):
                        Change_in_chem=-Change_in_chem
                    else:
                         Change_in_chem=Change_in_chem
                try:
                    player_combi[str(str(i[0])+" "+str(j[0]))]=str(float(player_combi[str(str(i[0])+" "+str(j[0]))])+Change_in_chem)
                    print("UPDATED VALUES",player_combi[str(str(i[0])+" "+str(j[0]))])
                except:
                    player_combi[str(str(j[0])+" "+str(i[0]))]=str(float(player_combi[str(str(j[0])+" "+str(i[0]))])+Change_in_chem)
                    print("UPDATED VALUES",player_combi[str(str(j[0])+" "+str(i[0]))])

    


    """
    valid_data=dict()
    for i in dictionary_val:
        if(i[1][0]!=(0,0,0)):
            valid_data[i[0]]=i[1]
    print(valid_data)
    for i in valid_data:
        for j in valid_data:
            if (i!=j):
                valid_data[i]
                    
    """
    # df=rdd.toDF(['id','DETAILS'])
    # coloumn_det=df.select('DETAILS')
    # valid_df=df.filter(coloumn_det)


    # valid_df=df.filter(f.select('DETAILS')[0].isin([[0,0,0]]))
    # valid_df.show()
##########################################################################################################################################

conf = SparkConf()
conf.setAppName("FPL")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
ssc = StreamingContext(sc, 5)
ssc.checkpoint("Checkpointing_done")
lines = ssc.socketTextStream("localhost", 6100)

players_df = sqlContext.read.load("/user/arshgoyal/csv/players.csv", format="csv", header="true", inferSchema="true")
unique_players=players_df.select('Id').distinct().collect()
unique_list=[]
player_combi=dict()
for i in unique_players:
    unique_list.append(i.Id)
for i in range(len(unique_list)):
    for j in range(i,len(unique_list)):
        if(i!=j):
            player_combi[str(str(unique_list[i])+" "+str(unique_list[j]))]=str(0.5)


#print(player_combi)
#print("#######################################################")
"""
with open("data1.json", "w") as outfile:  
    json.dump(player_combi, outfile) 
    

with open('data2.json') as json_file: 
    new_player_combi = json.load(json_file) 
print(new_player_combi)
"""


#lines.pprint()
#event = lines.filter(checkEvent)
### Match
print("########################################################Filter By Match##########################################")
match_data = lines.filter(filter_by_Match)
#match_data.pprint()
### Events
print("########################################################Filter By Event##########################################")
event_data = lines.filter(filter_by_Event)
#event_data.pprint()
print("########################################################Calculate Events#########################################")
event_characteristics = event_data.map(calculate_Events)
#event_characteristics.pprint()
print("########################################################Cummulative Metrics##########################################")
metrics = event_characteristics.updateStateByKey(cummulate_Metrics)
#metrics.pprint(30)
print("########################################################FINAL METRICS##########################################")
final_metrics = metrics.updateStateByKey(calculate_Metrics)
#final_metrics.pprint()

player_details=match_data.flatMap(lambda y: player_list(y))
#player_details.pprint()
#player_details.pprint()
print("########################################################PLAYER DETAILS##########################################")
player_D=final_metrics.join(player_details)
#player_D.pprint()
player_rate=player_D.updateStateByKey(RateplayerUpdate)
# player_rate.pprint()
player_rate.pprint()
print("########################################################PLAYER Profile Update##########################################")
playerprofile=final_metrics.updateStateByKey(profileplayerUpdate)
playerprofile.pprint()
##playerprofile.pprint()
print("########################################################FLUSH DATA OF VARIABLES##########################################")
metrics = metrics.updateStateByKey(lambda x: None)
final_metrics = final_metrics.updateStateByKey(lambda x: None)

print("###############################AFTER STREAMING#################################")
store_playerprofile={}
store_player_rating={}
#playerprofile.foreachRDD(convert_store)
player_chem=player_rate.foreachRDD(chem_calculate)


##SPARK##
ssc.start()
ssc.awaitTermination(10)  
ssc.stop()
###writing chemistry of players onto a json filr
with open("/home/arshgoyal/Desktop/BD_Proj/chemistry.json", "w") as outfile:  
     json.dump(player_combi, outfile) 