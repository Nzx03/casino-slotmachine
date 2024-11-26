import random

MAX_L=3
# MAX_B=10
# MIN_B=1

Rows=3
Cols=3

symbol_count={
  "A":3,
  "B":4,
  "C":2,
  "D":8
 }
symbol_value={
  "A":3,
  "B":4,
  "C":5,
  "D":2
 }


def check_win(columns,lines,bet,value):
  win=0
  win_line=[]

  for line in range(lines):
    symbol=columns[0][line]
    for column in columns:
      check=column[line]
      if symbol!= check:
       break
    else:
      win+= value[symbol]*bet
      win_line.append(lines+1)
  
  return win, win_line


       



def get_spin(rows,cols,symbols):
  all_s=[]
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_s.append(symbol)
      
  columns=[]
  for _ in range(cols):
    column=[]
    new_s=all_s[:]
    for _ in range(rows):
      value=random.choice(new_s)
      new_s.remove(value)
      column.append(value)
    
    columns.append(column)
  
  return columns

def print_slot(columns):

  #transposing
  for row in range(len(columns[0])):  
    for i,column in enumerate(columns):
      if i!=len(columns)-1:  
       print(column[row],end=" | ")   
      else:
        print(column[row],end="")
    print()
       

def deposit():
  while True:

    amount=input("How much would you like to deposit? (in ₹)")
    if amount.isdigit():
        amount=int(amount)
        if amount > 0:
          return amount
        else:
         print("Enter the amount greater than 0")
    else:
        print("Please enter the deposit in numbers! ")
    
     
  
def lines_number():
  while True:

     line=input("Enter the numbers of lines to bet on(1-" + str(MAX_L)+ ")?")
     if line.isdigit():
        line=int(line)
        if 1<=line <= MAX_L:
          return line
        else:
         print("Enter the line within range.")
     else:
        print("Please enter the lines in numbers! ")

def get_bet():
  while True:

     line=input("Enter the amount to bet on line?")
     if line.isdigit():
        line=int(line)
        # if MIN_B<=line <= MAX_B:
        #   break
        # else:
        #  print(f"Amount must be between ₹{MIN_B}-₹{MAX_B}" )
     else:
        print("Please enter the amount in numbers! ")
     return line  
    
def spin(balance):
  lines=lines_number()
  while True:
    bet=get_bet()
    total_bet=bet*lines
    if total_bet>balance:
      print(f"You do not have enough amount. Your current balance is ₹{balance}")
    else:
      break
  print(f"You are betting ₹{bet} on {lines} line.")
  print(f"Total bet is ₹{total_bet}")

  slots=get_spin(Rows,Cols,symbol_count)
  print_slot(slots)
  win,win_line=check_win(slots,lines,bet,symbol_value)
  print(f"You won ₹{win}") 
  print(f"You won on lines:", *win_line)
  return win-total_bet

   
def main():
  
  balance=deposit()
  while True:
    print(f"Current balance is ₹{balance}")
    ans=input("Press enter to play(q to quit).")
    if ans=='q':
      break
    
    balance+=spin(balance)
  print(f"You left with ₹{balance}")

main()
