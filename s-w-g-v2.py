from random import choice

# List of possible moves
l = [0, 1, 2]

def get_max_rounds():
	while True:
		try:
			max_rounds = int(input("Enter the max rounds you wanna play: "))
			return max_rounds
		except ValueError:
			print("INVALID INPUT!")

def get_computer_move():	     	    
	     """Returns a random move from the list of possible moves."""
	     return choice(l)
   
   
player_score = 0  # Player score
computer_score = 0  # Computer score

move = {0 : 'Snake', 1 : 'Water', 2 : 'Gun'}

# 2d List for storing results 
result_table = [
  ['D','W','L'],
  ['L','D','W'],
  ['W','L','D']
]

# dictionary for Mapping the results
result_map = { 'W': "You win", 'L': "You lose", 'D': "It's a draw" }




	    
def get_result_msg(result):
		    
	    
	    # Mapping the results 
	    message = result_map[result]
	    return message
	
	
def get_player_move():
	"""This function takes player input"""
	while True:
		try:
			player_move = int(input("\n 0. Snake\n 1. Water\n 2. Gun\n Choose Your Move:\n 0 or 1 or 2\n"))
			
			if player_move not in [0, 1, 2]:
			     raise ValueError
			     
			return player_move   # ✅ only valid input returns
			
		except ValueError:
		      	print("Invalid input,\n enter a number between 0, 1 or 2 \n\n TRY AGAIN!")

def update_score(result):
    global player_score, computer_score

    match result:
        case "W":
            player_score += 1
        case "L":
            computer_score += 1

def final_result():
	print("FINAL RESULT:")
	if (player_score == computer_score):
		print('ITS A DRAW')
	elif (player_score > computer_score):
		print('YOU WIN')
	elif(player_score < computer_score):
		print('YOU LOSE')

def game():
	rounds = 0
	max_rounds=get_max_rounds()
	while True:
		player_move = get_player_move()
		computer_move = get_computer_move() 
		print('-'*20)
		print(f'Your move is {move[player_move]} \nComputer move is {move[computer_move]}')
		result = result_table[player_move][computer_move]
		print(get_result_msg(result))
		update_score(result)
		rounds += 1
		print('-'*20)
		
		if rounds >= max_rounds:
			break
	final_result()
		
	
	
	
game()


