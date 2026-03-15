def climbingLeaderboard(ranked, player):
    unique_ranked_scores = []
    
    for score in ranked:
        if not unique_ranked_scores or unique_ranked_scores [-1] != score:
            unique_ranked_scores.append(score)
    leaderboard_index = len(unique_ranked_scores) - 1
    player_ranks =[]
        
    for player_score in player:
            while leaderboard_index >= 0 and player_score >= unique_ranked_scores[leaderboard_index]:
                leaderboard_index -= 1
            player_ranks.append(leaderboard_index + 2)
    return player_ranks