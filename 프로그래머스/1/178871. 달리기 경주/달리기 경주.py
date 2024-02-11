
def solution(players, callings):
    players_positions = {player: idx for idx, player in enumerate(players)}
    for i in callings:
        
        idx = players_positions[i]
        if idx > 0:
            players[idx] , players[idx-1]= players[idx-1], players[idx]
            players_positions[i], players_positions[players[idx]] = idx-1, idx

    return players