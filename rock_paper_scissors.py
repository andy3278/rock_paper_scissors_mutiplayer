import random
players = input("how many players?: ")
orgin_players = players
winners = input("how many winners?: ")
orgin_winners = winners
t = ["R", "P", "S"]
count_total = 0
count_winners = 0

condition = True

def win_con(list_player):
    num_winners = 0
    num_R = list_player.count("R")
    num_P = list_player.count("P")
    num_S = list_player.count("S")
    if num_R >0 and num_P >0 and num_S >0:
        return num_winners
    elif num_R == len(list_player) or num_P == len(list_player) or num_S == len(list_player):
        return num_winners
    elif num_R == 0 and num_S != 0 and num_P != 0:
        num_winners = num_S
    elif num_P == 0 and num_S != 0 and num_R != 0:
        num_winners = num_R
    elif num_S == 0 and num_P != 0 and num_R != 0:
        num_winners = num_P
    return num_winners


def ran_choice(players):
    list = random.choices(t, k =players)
    return list

avg_list = []

N = 10
for i in range(N):
    condition = True
    players = int(orgin_players)
    winners = int(orgin_winners)
    count_total = 0
    count_winners = 0
    while condition:
        list_player = ran_choice(players)
        result = win_con(list_player)
        count_total +=1
        if count_winners == winners:
            condition = False
        if players <= 0:
            condition = False
        if result != 0:
            if result < (winners - count_winners):
                count_winners += result
                players -= result
            elif result > (winners - count_winners):
                players = result
            elif result == (winners - count_winners):
                condition = False
            if count_winners == winners:
                condition = False
    avg_list.append(count_total)

avg = sum(avg_list)/float(len(avg_list))
#print(avg_list)
print("average number of games with " + str(orgin_winners) +" winners from " + str(orgin_players) +
    " players, \nin "+ str(N) + " repeated simulations is: "+ str(round(avg, 2)))
# print("Total number of RPS rounds played to get " + 
#     str(orgin_winners) +" winners from " + str(orgin_players) +
#     " players, is: "+ str(count_total))
