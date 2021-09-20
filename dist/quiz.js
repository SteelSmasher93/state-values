// Generated by CoffeeScript 2.6.0
//Initializes questions text
var answers, auth, calc_score, i, init_question, len, max_auth, max_part, max_ptnl, max_stat, next_question, part, prev_question, ptnl, qn, question, results, stat;

init_question = function() {
  document.getElementById("question-text").innerHTML = questions[qn].question; //Sets question text
  document.getElementById("question-number").innerHTML = "Question " + (qn + 1) + " of " + questions.length; // Sets question number
  //Disables back button if answers is empty
  if (answers.length === 0) {
    document.getElementById("back_button").style.display = "none";
    document.getElementById("back_button_off").style.display = "block";
  } else {
    document.getElementById("back_button").style.display = "block";
    document.getElementById("back_button_off").style.display = "none";
  }
  if (questions[qn].answers.text1 !== false) {
    document.getElementById("button1").style.display = "block";
    document.getElementById("button1").innerHTML = questions[qn].answers.text1;
  } else {
    document.getElementById("button1").style.display = "none";
  }
  if (questions[qn].answers.text2 !== false) {
    document.getElementById("button2").style.display = "block";
    document.getElementById("button2").innerHTML = questions[qn].answers.text2;
  } else {
    document.getElementById("button2").style.display = "none";
  }
  if (questions[qn].answers.text3 !== false) {
    document.getElementById("button3").style.display = "block";
    document.getElementById("button3").innerHTML = questions[qn].answers.text3;
  } else {
    document.getElementById("button3").style.display = "none";
  }
  if (questions[qn].answers.text4 !== false) {
    document.getElementById("button4").style.display = "block";
    document.getElementById("button4").innerHTML = questions[qn].answers.text4;
  } else {
    document.getElementById("button4").style.display = "none";
  }
  if (questions[qn].answers.text5 !== false) {
    document.getElementById("button5").style.display = "block";
    return document.getElementById("button5").innerHTML = questions[qn].answers.text5;
  } else {
    return document.getElementById("button5").style.display = "none";
  }
};

//Jumps to next question when option button clicked or to results if no questions are left
next_question = function(choice) {
  var mult;
  mult = questions[qn].answers.weight[choice];
  ptnl += mult * questions[qn].effect.ptnl;
  stat += mult * questions[qn].effect.stat;
  auth += mult * questions[qn].effect.auth;
  part += mult * questions[qn].effect.part;
  qn++;
  answers.push(mult);
  if (qn < questions.length) {
    return init_question();
  } else {
    return results();
  }
};

//Rewinds to previous question when back button clicked (if previous answer exists)
prev_question = function() {
  var prev_answer;
  if (answers.length === 0) {

  } else {
    qn--;
    prev_answer = answers.slice(0).pop();
    ptnl -= prev_answer * questions[qn].effect.ptnl;
    stat -= prev_answer * questions[qn].effect.stat;
    auth -= prev_answer * questions[qn].effect.auth;
    part -= prev_answer * questions[qn].effect.part;
    answers.pop();
    return init_question();
  }
};

//Calculates the score by diving the obtained values by the maxiumum for each axis
calc_score = function(score, max) {
  if (max === 0) {
    return "50.0";
  } else {
    return (100 * (max + score) / (2 * max)).toFixed(1);
  }
};

//Jumps to results page with the correct percentage scores for each axis
results = function() {
  return window.location.href = "results.html" + "?a=" + calc_score(ptnl, max_ptnl) + "&b=" + calc_score(stat, max_stat) + "&c=" + calc_score(auth, max_auth) + "&d=" + calc_score(part, max_part);
};


//Defines each variable as 0
max_ptnl = max_stat = max_auth = max_part = ptnl = stat = auth = part = qn = 0;

//Defines arrrays as empty
answers = [];

//Calculates max score for each axis
for (i = 0, len = questions.length; i < len; i++) {
  question = questions[i];
  max_ptnl += Math.abs(question.effect.ptnl);
  max_stat += Math.abs(question.effect.stat);
  max_auth += Math.abs(question.effect.auth);
  max_part += Math.abs(question.effect.part);
}

//starts the question initializer
init_question();
