from random import choice as ch
# List of possible moves
l = [1, 2, 3]

def get_computer_move(l):	     	    
	     """Returns a random move from the list of possible moves."""
	     return ch(l)
   
   
pscore=0  # Player score
cscore =0  # Computer score
move = {1 : 'Snake', 2 : 'Water', 3 : 'Gun'}
# 2d List for storing results 
table = [
  ['D','W','L'],
  ['L','D','W'],
  ['W','L','D']
]
# dictionary for Mapping the results
result_map = { 'W': "You win", 'L': "You lose", 'D': "It's a draw" }

def get_result(player, computer):
	    """Make the result of a round based on player's and computer's moves. 
	    """
	    # converting user input and random into strings 
	    player_index = player - 1
	    computer_index = computer - 1
	    #Getting results from 2d list
	    r = table[player_index][computer_index]
	    
	    # Mapping the results 
	    message = result_map[r]
	    return message
	    

def get_player_input():
	"""This function takes player input"""
	while True:
		try:
			pmove = int(input("\n 1. Snake\n 2. Water\n 3. Gun\n Choose Your Move:\n 1 or 2 or 3\n"))
			
			if pmove not in [1, 2, 3]:
			     raise ValueError
			     
			return pmove   # ✅ only valid input returns
			
		except ValueError:
		      	print("Invalid input,\n enter a number between 1, 2 or 3\n\n TRY AGAIN!")

nround = 0
while True:
		
		#Get palyer's move
		x1 = get_player_input()
		
		
		# Get computer's move		
		x2 = get_computer_move(l)
		
	
	
		print(f' \nYour move is {move[x1]} \nComputer move is {move[x2]}')
		# Determine result of round
		x = get_result(x1, x2)
		print(x)
		# Update scores
		if x == "You win":
				pscore += 1
		elif x == "You lose":
				cscore += 1
		nround += 1
		
		# Check if game is over
		if nround >= 5:
			break
			
	
		
	
#
# Print final scores and result		
print(f"\n \n \nThe player score is {pscore} \nAnd \nThe computer score is {cscore}")

if (pscore == cscore):
	print('ITS A DRAW')
elif (pscore > cscore):
	print('YOU WIN')
elif(pscore < cscore):
	print('YOU LOSE')