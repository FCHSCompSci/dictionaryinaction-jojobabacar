dbfz={
    'display_name': 'zawarudo',
    'total_matches':164,
    'ranked_match_wins': 32,
    'party_match_wins': 14,
    'clan': 'fuzed_zamasu',
    'bp':130000,
    'header': 'fuzed_zamasu',
    'followers':0,
    'ring_match_wins':57,
    'team': 'hit_bluevegeta_rosegokublack',
    }
        
def play_dbfz_match():
    while True:
        match=input("ring,rank, or party")
        while match == "rank":
            question=input("did you win the game?")
            if question=="yes":
                dbfz['bp']+=30000
                dbfz['ranked_match_wins']+=1
            if question=="no":
                dbfz['bp']-=30000
                dbfz['ranked_match_wins']-=1
            if question=="stop":
                break
            for key, value in dbfz.items():
                print("%s:%s"%(key,value))
        while match=="ring":
            question=input("did you lose the game?")
            if question=="no":
                dbfz['ring_match_wins']+=1
            if question=="yes":
                dbfz['ring_match_wins']+=0
            if question=="stop":
                break
            for key, value in dbfz.items():
                print("%s:%s"%(key,value))
        while match=="party":
            question=input("did ya'll win the game?")
            if question=="yes":
                dbfz['party_match_wins']+=1
            if question=="no":
                dbfz['party_match_wins']-=1
            if question=="stop":
                break
        if match=='x':
            break
play_dbfz_match()
for key, value in dbfz.items():
    print("%s:%s"%(key,value))


            
        
        


        

