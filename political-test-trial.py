from tkinter import *
import turtle as t
t.hideturtle()
import time

pat_level = 0
pat_tiers = ['Libertarian', 'Autonomist', 'Centrist', 'Paternalist-Leaning', 'Paternalist']
state_level = 0
state_tiers = ['Planned Economy', 'Regulationist', 'Centrist', 'Free-Market', 'Laissez-Faire']
part_level = 0
part_tiers = ['Partisan', 'Partisan-Leaning', 'Mixture', 'Non-Partisan Leaning', 'Non-Partisan']
auth_level = 0
auth_tiers = ['Autocracy', 'Authoritarian Democracy', 'Mixed Regime', 'Constitutional Democracy', 'Full Democracy']

def make_scale(val):
	t.pu()
	b=100
	y=75
	t.pencolor('black')
	t.pensize(10)
	t.goto(-b,y)
	t.pd()
	t.goto(b,y)
	t.pu()
	t.pencolor('#7c12a6')
	t.goto(-b,y)
	t.pd()
	t.goto(val,y)
	t.pencolor('#d69018')
	t.goto(b,y)

def make_scale1(val):
	t.pu()
	b=100
	y=25
	t.pencolor('black')
	t.pensize(10)
	t.goto(-b,y)
	t.pd()
	t.goto(b,y)
	t.pu()
	t.pencolor('red')
	t.goto(-b,y)
	t.pd()
	t.goto(val,y)
	t.pencolor('blue')
	t.goto(b,y)

def make_scale2(val):
	t.pu()
	b=100
	y=-25
	t.pencolor('black')
	t.pensize(10)
	t.goto(-b,y)
	t.pd()
	t.goto(b,y)
	t.pu()
	t.pencolor('#1f1f1f')
	t.goto(-b,y)
	t.pd()
	t.goto(val,y)
	t.pencolor('#c9c9c9')
	t.goto(b,y)

def make_scale3(val):
	t.pu()
	b=100
	y=-75
	t.pencolor('black')
	t.pensize(10)
	t.goto(-b,y)
	t.pd()
	t.goto(b,y)
	t.pu()
	t.pencolor('#3d1606')
	t.goto(-b,y)
	t.pd()
	t.goto(val,y)
	t.pencolor('#e9fa32')
	t.goto(b,y)
	time.sleep(15)

def find_pat():
	adder = 0
	temp_pat_level = 0

	print('Question 1: If there was a man who was about to cross an unstable bridge, and he would die if he crossed it, would you stop him from crossing it?\n\t1) Yes\n\t2) Only until I was sure he knew it would kill him\n\t3) No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '3':
		adder = -10
	temp_pat_level += adder

	print('Question 2: Should car manufacturers be forced to put seatbelts in their cars?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 3: Should vaccines be mandatory?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 20
	if input1 == '2':
		adder = 10
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 4: What do you think about the War on Drugs?\n\t1) It was fully good\n\t2) It was a good idea, but it failed\n\t3) It was a bad idea')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	temp_pat_level += adder

	print('Question 5: Is freedom inherently good?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 10
	temp_pat_level += adder

	print('Question 6: Should suicide be legal?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 10
	temp_pat_level += adder

	print('Question 7: Should all drugs be legal?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -20
	if input1 == '2':
		adder = -10
	if input1 == '3':
		adder = 0
	if input1 == '4':
		adder = -5
	temp_pat_level += adder

	print('Question 8: Are there "victimless crimes" that should be legal?\n\t1) Yes\n\t2) No')
	input1 = input()
	if input1 == '1':
		adder = -5
	if input1 == '2':
		adder = 5
	temp_pat_level += adder

	print('Question 9: Should homeless people be forcefully housed?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 10: Is one aspect of why guns are bad is that they lead to increased suicide?\n\t1) Hard Yes\n\t2) Yes\n\t3) Yes, but guns are still mostly good\n\t4) No\n\t5) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = 0
	if input1 == '4':
		adder = -5
	if input1 == '5':
		adder = -10
	temp_pat_level += adder

	return temp_pat_level

def find_state():
	adder = 0
	temp_pat_level = 0

	print('Question 1: Are there too many regulations on businesses?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 10
	temp_pat_level += adder

	print('Question 2: Should Silicon Valley be more heavily regulated?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 3: Is a "free market" a goal worth striving for?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 10
	temp_pat_level += adder

	print('Question 4: Is free trade good, in almost all circumstances?\n\t1) It it always good\n\t2) Yes\n\t3) No\n\t4) It is never good')
	input1 = input()
	if input1 == '1':
		adder = -15
	if input1 == '2':
		adder = -10
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 15
	temp_pat_level += adder

	print('Question 5: Which should be beholden to the other?\n\t1) Businesses should be beholden to the State\n\t2) The State should be beholden to businesses\n\t3) Business and the State should cooperate\n\t4) Neither should be beholden to the other')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = -10
	if input1 == '3' or input1 == '4':
		adder = 0
	temp_pat_level += adder

	print('Question 6: True or False: corporations should never act against the country.\n\t1) Hard True\n\t2) True\n\t3) False\n\t4) Hard False')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 7: Are there some commodities that shouldn\'t be sold?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 8: Are many issues in your nation caused by overregulation?\n\t1) Yes\n\t2) Not many, but still some\n\t3) No')
	input1 = input()
	if input1 == '1':
		adder = -5
	if input1 == '2':
		adder = 0
	if input1 == '3':
		adder = 5
	temp_pat_level += adder

	print('Question 9: Is the EU bad because of bureaucracy?\n\t1) Hard Yes\n\t2) Yes\n\t3) The EU is good, but it\'s too bureaucratic\n\t4) No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 0
	if input1 == '4':
		adder = 10
	temp_pat_level += adder

	print('Question 10: Should the government stop businesses from hurting the environment?\n\t1) Yes\n\t2) Usually\n\t3) Not Usually\n\t4) No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	return temp_pat_level

def find_part():
	adder = 0
	temp_pat_level = 0

	print('Question 1: Would you prefer if your country had no political parties?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 2: Would you prefer a party list proportional representation system?\n\t1) Yes\n\t2) I would prefer it over my current system, but, ultimately, I would prefer non-partisan first-past-the-post\n\t3) No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = 10
	if input1 == '3':
		adder = 10
	temp_pat_level += adder

	print('Question 3: Would you vote for a party besides the last party you voted for?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 4: What do you think about the two-party system in America?\n\t1) It is a good system that ensures stability\n\t2) It should have no parties\n\t3) It should have three parties\n\t4) It should be a one-party/dominant-party system\n\t5) It should have many parties trying to form coalitions')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = 10
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -5
	if input1 == '5':
		adder = -10
	temp_pat_level += adder

	print('Question 5: Would you vote for a politician you agree with from a party with a platform you strongly disagree with?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10

	print('Question 6: Would you rather vote for a political "insider" or a political "outsider"?\n\t1) Insider\n\t2) Outsider')
	input1 = input()
	if input1 == '1':
		adder = -5
	if input1 == '2':
		adder = 5
	temp_pat_level += adder

	print('Question 7: Is the idea of a political party inherently flawed, because it comes with a certain set of ideas/policies you must agree with?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 8: Is the concept of "syncretic politics" good?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 9: Would you consider yourself to be a non-partisan?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 15
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -15
	temp_pat_level += adder

	print('Question 10: Is partisanship one of the three biggest problems in modern politics?\n\t1) Yes\n\t2) No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = -10
	temp_pat_level += adder

	return temp_pat_level

def find_auth():
	adder = 0
	temp_pat_level = 0

	print('Question 1: Has democracy failed?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('True or false: "[Representative] Democracy is the worst system of government, except for all the others we\'ve tried."\n\t1) True\n\t2) False\n\t3) False, because democracy is good')
	input1 = input()
	if input1 == '1':
		adder = -5
	if input1 == '2':
		adder = 5
	if input1 == '3':
		adder = -5
	temp_pat_level += adder

	print('Question 3: Is Direct Democracy a good system?\n\t1) Hard Yes\n\t2) Yes\n\t3) Sometimes\n\t4) No\n\t5) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 0
	if input1 == '4':
		adder = 5
	if input1 == '5':
		adder = 10
	temp_pat_level += adder

	print('Question 4: Can democracy oppress the rights of the minority?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = 0
	if input1 == '3':
		adder = -5
	if input1 == '4':
		adder = -10
	temp_pat_level += adder

	print('Question 5: Should democracy be implemented in all governments/states?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 10

	print('Question 6: Which is worse: an oppressive democracy or a benevolent dictatorship?\n\t1) Oppressive Democracy\n\t2) Benevolent Dictatorship')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = 10
	temp_pat_level += adder

	print('Question 7: Which is more important: security or democracy?\n\t1) Security\n\t2) Democracy')
	input1 = input()
	if input1 == '1':
		adder = 10
	if input1 == '2':
		adder = -10
	temp_pat_level += adder

	print('Question 8: Should everyone in your country be able to vote for representatives?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 10
	temp_pat_level += adder

	print('Question 9: Is a decision better when the input of more people is taken into account?\n\t1) Hard Yes\n\t2) Yes\n\t3) No\n\t4) Hard No')
	input1 = input()
	if input1 == '1':
		adder = -10
	if input1 == '2':
		adder = -5
	if input1 == '3':
		adder = 5
	if input1 == '4':
		adder = 10
	temp_pat_level += adder

	print('Question 10: Which label defines you more?\n\t1) Authoritarian\n\t2) Anti-Authoritarian')
	input1 = input()
	if input1 == '1':
		adder = 15
	if input1 == '2':
		adder = -15
	temp_pat_level += adder

	return temp_pat_level

pat_level = find_pat()
print(pat_level)

print('Section 2')
state_level = find_state()
print(state_level)

print('Section 3')
part_level = find_part()
print(part_level)

print('Section 4')
auth_level = find_auth()
print(auth_level)

make_scale(pat_level)
make_scale1(state_level)
make_scale2(part_level)
make_scale3(auth_level)

print("You are " + str((pat_level+100)/2) + '% Paternalist\nYou are ' + str((state_level+100)/2) + '% Statist\n You are ' + str((part_level+100)/2) + '% Non-Partisan\n You are ' + str((auth_level+100)/2) + '% Authoritarian')

ts = t.getscreen()
ts.getcanvas().postscript(file="results.eps")
