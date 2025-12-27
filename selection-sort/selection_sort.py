play_counts = [456, 34, 3, 4, 5]

for i in range(len(play_counts) - 1):
    smallest_idx = i
    for j in range(i+1, len(play_counts)):
        if play_counts[j] < play_counts[smallest_idx]:
            smallest_idx = j
    play_counts[i], play_counts[smallest_idx] = play_counts[smallest_idx], play_counts[i]
            
print(play_counts)
