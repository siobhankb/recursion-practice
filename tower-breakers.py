# Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.The rules of the game are as follows:

# Initially there are  towers.
# Each tower is of height .
# The players move in alternating turns.
# In each turn, a player can choose a tower of height  and reduce its height to , where  and  evenly divides .
# If the current player is unable to make a move, they lose the game.
# Given the values of  and , determine which player will win. If the first player wins, return . Otherwise, return .

# Example. 

# There are  towers, each  units tall. Player  has a choice of two moves:
# - remove  pieces from a tower to leave  as 
# - remove  pieces to leave 

# Let Player  remove . Now the towers are  and  units tall.

# Player  matches the move. Now the towers are both  units tall.

# Now Player  has only one move.

# Player  removes  pieces leaving . Towers are  and  units tall.
# Player  matches again. Towers are both  unit tall.

# Player  has no move and loses. Return .

# Function Description

# Complete the towerBreakers function in the editor below.

# towerBreakers has the following paramter(s):

# int n: the number of towers
# int m: the height of each tower
# Returns

# int: the winner of the game
# Input Format

# The first line contains a single integer , the number of test cases.
# Each of the next  lines describes a test case in the form of  space-separated integers,  and .

# Constraints

# Sample Input

# STDIN   Function
# -----   --------
# 2       t = 2
# 2 2     n = 2, m = 2
# 1 4     n = 1, m = 4
# Sample Output

# 2
# 1
# Explanation

# We'll refer to player  as  and player  as 

# In the first test case,  chooses one of the two towers and reduces it to . Then  reduces the remaining tower to a height of . As both towers now have height ,  cannot make a move so  is the winner.

# In the second test case, there is only one tower of height .  can reduce it to a height of either  or .  chooses  as both players always choose optimally. Because  has no possible move,  wins.


def towerBreakersBAD(n, m):
    towers = {}
    for i in range(n):
        towers[i] = m
    print('towers = ', towers)
    
    turn = 1
    play = True
    while play == True:
        for i in range (len(towers.keys())):
            chop = 0
            if towers[i] > 1:
                ht = towers[i]
                print('tower# ', i, ' = ', ht)
                chop = ht//2
                print('chop= ', chop)
                if ht % chop == 0:
                    towers[i] = chop
                    turn = -turn
                else:
                    while chop > 1:
                        chop -= 1
                        if ht % chop == 0:
                            towers[i] = chop
                            turn = -turn
                            break
                        else:
                            towers[i] = 1
                            turn = -turn
                            break
            else:
                break
        break
    #             while chop > 1:
    #                 if towers[i] % chop == 1:
    #                     chop -= 1
    #                 else:
    #                     towers[i] = chop
    #                     turn = -turn
    #                     break
    #         else:
    #             turn = -turn
    #             play = False
    #             break
    
    # winner = 0
    # if turn == 1:
    #     winner = 1
    # else:
    #     winner = 2

    # return winner
    return

ex1 = [2, 6]
test1 = towerBreakersBAD(ex1[0], ex1[1])
print(test1)



# All of the above is TRASH - it all comes down to game theory
# The solution comes from thinking at the end/what is needed to win and then working backwards. A player wins if the opponent has no moves left, and that occurs when the height of the last tower is 1.
# Since both players are playing optimally, they will make the same moves. If there is one move left, then the first player wins because he/she takes the move and the second player is left with no moves. If there are two moves left, the first player takes a move, then the second player and the first player is left with no moves. We can extend this thinking to any number, so any even numbers of plays makes second player win and any odd number makes first player win.

# The question seems complex, but:
# if tower%2 == 1:
# p1 wins
# else:
# p2 wins.

# SPECIAL CASES:
#   if there is only 1 tower (n == 1), player 1 always wins bc can reduce the tower to 1 block every time (since every number can be divided by 1)
#   if tower heights are 1 (m == 1), player 2 always wins bc player 1 can't do anything

# when there are even number of towers, player 1 will always lose bc player 2 will match/mirror previous play

# when there are odd number of towers, player 2 will always lose bc player 1 can come back and leave player 2 w no moves

def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1