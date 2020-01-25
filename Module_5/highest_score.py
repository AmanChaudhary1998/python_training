Indian_player = {'Batsman':{'Rohit Sharma':{'Matches':'250','Runs':'9080','Average':'62.5','Highest Score':'223'},
                            'Shikhar Dhawan':{'Matches':'110','Runs':'3050','Average':'40.5','Highest Score':'123'},
                            'Virat Kohli':{'Matches':'245','Runs':'10845','Average':'52.5','Highest Score':'233'},
                            'Yuvraj Singh':{'Matches':'330','Runs':'12500','Average':'72.5','Highest Score':'250'}},
                 'Wic_keeper':{'M.S.Dhoni':{'Matches':'300','Runs':'11000','Average':'42.5','Highest Score':'200'}}}
# print(Indian_player['Batsman']['Virat Kohli']['Highest Score'])
p1=[Indian_player['Batsman']['Rohit Sharma']['Highest Score'],
    Indian_player['Batsman']['Virat Kohli']['Highest Score'],
    Indian_player['Batsman']['Shikhar Dhawan']['Highest Score'],
    Indian_player['Batsman']['Yuvraj Singh']['Highest Score'],
    Indian_player['Wic_keeper']['M.S.Dhoni']['Highest Score']]
print(p1)
print(max(p1))



               
     
