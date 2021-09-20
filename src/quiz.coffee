#Initializes questions text
init_question = () ->
    document.getElementById("question-text").innerHTML = questions[qn].question #Sets question text
    document.getElementById("question-number").innerHTML = "Question " + (qn + 1) + " of " + (questions.length) # Sets question number
    #Disables back button if answers is empty
    if answers.length is 0
        document.getElementById("back_button").style.display = "none"
        document.getElementById("back_button_off").style.display = "block"
    else
        document.getElementById("back_button").style.display = "block"
        document.getElementById("back_button_off").style.display = "none"
    if questions[qn].answers.text1 isnt false
        document.getElementById("button1").style.display = "block"
        document.getElementById("button1").innerHTML = questions[qn].answers.text1
    else
        document.getElementById("button1").style.display = "none"
    if questions[qn].answers.text2 isnt false
        document.getElementById("button2").style.display = "block"
        document.getElementById("button2").innerHTML = questions[qn].answers.text2
    else
        document.getElementById("button2").style.display = "none"
    if questions[qn].answers.text3 isnt false
        document.getElementById("button3").style.display = "block"
        document.getElementById("button3").innerHTML = questions[qn].answers.text3
    else
        document.getElementById("button3").style.display = "none"
    if questions[qn].answers.text4 isnt false
        document.getElementById("button4").style.display = "block"
        document.getElementById("button4").innerHTML = questions[qn].answers.text4
    else
        document.getElementById("button4").style.display = "none"
    if questions[qn].answers.text5 isnt false
        document.getElementById("button5").style.display = "block"
        document.getElementById("button5").innerHTML = questions[qn].answers.text5
    else
        document.getElementById("button5").style.display = "none"


#Jumps to next question when option button clicked or to results if no questions are left
next_question = (choice) ->
    mult = questions[qn].answers.weight[choice]
    ptnl += mult*questions[qn].effect.ptnl
    stat += mult*questions[qn].effect.stat
    part += mult*questions[qn].effect.part
    auth += mult*questions[qn].effect.auth
    qn++
    answers.push mult
    if qn < questions.length
        do init_question
    else
        do results

#Rewinds to previous question when back button clicked (if previous answer exists)
prev_question = () ->
    if answers.length is 0
        return
    else
        qn--
        prev_answer = answers[..].pop()
        ptnl -= prev_answer * questions[qn].effect.ptnl
        stat -= prev_answer * questions[qn].effect.stat
        part -= prev_answer * questions[qn].effect.part
        auth -= prev_answer * questions[qn].effect.auth
        do answers.pop
        do init_question

#Calculates the score by diving the obtained values by the maxiumum for each axis
calc_score = (score,max) ->
    if max is 0
        return "50.0"
    else
        return (100*(max+score)/(2*max)).toFixed(1)

#Jumps to results page with the correct percentage scores for each axis
results = () ->
    window.location.href = "results.html" \
        + "?a=" + calc_score(ptnl,max_ptnl) \
        + "&b=" + calc_score(stat,max_stat) \
        + "&c=" + calc_score(part,max_part) \
        + "&d=" + calc_score(auth,max_auth) 

#Defines each variable as 0
max_ptnl = max_stat = max_part = max_auth =\
ptnl = stat = part = auth = qn = 0
#Defines arrrays as empty
answers = []
#Calculates max score for each axis
for question in questions
    max_ptnl += Math.abs(question.effect.ptnl)
    max_stat += Math.abs(question.effect.stat)
    max_part += Math.abs(question.effect.part)
    max_auth += Math.abs(question.effect.auth)
#starts the question initializer
do init_question
