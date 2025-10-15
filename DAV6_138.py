#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


games= np.array([1,2,3,4,5,6])
points_scored =np.array([95,102,78,88,110,100])
opponent_points= np.array([90,88,100,85,95,100])
attendance=np.array([1500,1800,1200,1600,2000,1900])
change_in_points= np.diff(points_scored,prepend=points_scored[0])
print("Game\tPoints Scored\tChange from Previous game")
for g,p,c in zip(games ,points_scored,change_in_points):
    print(f"(g)\t{p}\t\t{c:+}?")

plt.figure(figsize=(8,5))
plt.plot(games,points_scored,marker='o',color='b',label="Points Scored")
plt.title("Teams's Points Scored over the season")
plt.xlabel("Game Number")
plt.ylabel("Points Scored")
plt.grid(True)
plt.legend()
plt.show()


# In[4]:


games = np.array([1, 2, 3, 4, 5, 6])
points_scored = np.array([95, 102, 78, 88, 110, 100])
opponent_points = np.array([90, 88, 100, 85, 95, 100])
attendance = np.array([1500, 1800, 1200, 1600, 2000, 1900])


average_attendance = np.mean(attendance)
print(f"Average attendance throughout the season: {average_attendance:.2f}")


plt.figure(figsize=(8,5))
plt.plot(games, attendance, marker='o', color='green', label='Attendance')
plt.title("Attendance over the Season")
plt.xlabel("Game Number")
plt.ylabel("Attendance")
plt.grid(True)
plt.legend()
plt.show()


# In[6]:


players = ['A', 'B', 'C', 'D', 'E']
points = np.array([
    [20, 15, 25, 18, 17],
    [22, 18, 20, 25, 17],
    [15, 12, 28, 10, 13],
    [18, 20, 22, 15, 13],
    [25, 25, 30, 20, 10],
    [20, 22, 18, 30, 10]
])

total_points = np.sum(points, axis=0)
top_player_index = np.argmax(total_points)
top_player = players[top_player_index]

print(f"The player who scored the most points over the season is: Player {top_player} with {total_points[top_player_index]} points.")


plt.figure(figsize=(8,5))
plt.bar(players, total_points, color='orange')
plt.title('Total Points Scored by Each Player Over the Season')
plt.xlabel('Player')
plt.ylabel('Total Points')
plt.grid(axis='y')
plt.show()


# In[8]:


import numpy as np
import matplotlib.pyplot as plt

Games = [1, 2, 3, 4, 5, 6]
PointsScored = np.array([95, 102, 78, 88, 110, 100])
threshold = 100


games_above_threshold = np.sum(PointsScored > threshold)
print(f"Number of games where the team scored above {threshold} points: {games_above_threshold}")


bins = [80, 90, 100, 110, 120]
labels = ['80-90', '90-100', '100-110', '110-120']

counts, _ = np.histogram(PointsScored, bins=bins)


plt.figure(figsize=(8,5))
plt.bar(labels, counts, color='black')
plt.title('Number of Games Scored in Different Point Ranges')
plt.xlabel('Points Range')
plt.ylabel('Number of Games')
plt.grid(axis='y')
plt.show()


# In[12]:


import numpy as np
import matplotlib.pyplot as plt


opponents = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F']
points_scored = np.array([95, 102, 78, 88, 110, 100])


best_opponent_index = np.argmax(points_scored)
best_opponent = opponents[best_opponent_index]
print(f"The team performed best against {best_opponent}, scoring {points_scored[best_opponent_index]} points.")


plt.figure(figsize=(8,5))
plt.bar(opponents, points_scored, color='orange')
plt.title('Points Scored Against Each Opponent')
plt.xlabel('Opponent')
plt.ylabel('Points Scored')
plt.grid(axis='y')
plt.show()


# In[13]:


import matplotlib.pyplot as plt

opponents = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F']
attendance = [1500, 1800, 1200, 1600, 2000, 1900]

plt.figure(figsize=(8,5))
plt.bar(opponents, attendance, color='skyblue')
plt.title('Game Attendance by Opponent')
plt.xlabel('Opponent')
plt.ylabel('Attendance')
plt.grid(axis='y')
plt.show()


# In[14]:


import numpy as np
import matplotlib.pyplot as plt


points_scored = np.array([95, 102, 78, 88, 110, 100])
opponent_points = np.array([90, 88, 100, 85, 95, 100])

wins = np.sum(points_scored > opponent_points)
losses = np.sum(points_scored < opponent_points)


avg_points = np.mean(points_scored)

categories = ['Wins', 'Losses', 'Average Points Scored']
values = [wins, losses, avg_points]

max_points = max(points_scored)
wins_scaled = wins * max_points / max(wins, losses)
losses_scaled = losses * max_points / max(wins, losses)

values_scaled = [wins_scaled, losses_scaled, avg_points]

plt.figure(figsize=(8,5))
bars = plt.bar(categories, values_scaled, color=['green', 'red', 'blue'])
plt.title("Team's Win-Loss Record vs. Average Points Scored")
plt.ylabel("Scaled Values")

plt.text(0, values_scaled[0] + 1, f'{wins} wins', ha='center')
plt.text(1, values_scaled[1] + 1, f'{losses} losses', ha='center')
plt.text(2, values_scaled[2] + 1, f'{avg_points:.1f} pts', ha='center')

plt.show()


# In[ ]:




