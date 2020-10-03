# This aint my last ride

### **Description :**
>This video game is made using python and pygame only.

- This is a 2 player game where 2 players compete each other and the player with higher score wins the game. 
- There are 4 rounds in this game.
>
Score increases by 5 if you cross an obstacle and by 10 for a moving one.
>
The score is counted and saved even if the player is eliminated before completion.
>
New enemies and number of obstacles increase after every round.
>
If a player wins a particular round the enemy's speed is increased in the next round.

### Game design
>Controls :
UP DOWN LEFT RIGHT : for Player1 \
>W A S D : for Player2

## For better gaming experience :
* I have declared 4 dedicated variables for up down left and right...instead of 2 variables
* The collision theory used is pixel perfect rather than distance and AABB .
Which allows narrow escape for the player.

![](https://github.com/cyk-psych/this-aint-my-last-ride/blob/master/miss.png?raw=true)
