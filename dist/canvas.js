//Version type
var version = "V1";
//Other vars
var edition;
//Sets label for each axis
function setLabel(val, ary) {
    if (val > 100) {
        return "";
    }
    else if (val > 80) {
        return ary[0];
    }
    else if (val > 60) {
        return ary[1];
    }
    else if (val >= 40) {
        return ary[2];
    }
    else if (val >= 20) {
        return ary[3];
    }
    else if (val >= 0) {
        return ary[4];
    }
    else {
        return "";
    }
}
//Setting value svg sources
//Paternalism axis
var img_libertarian = new Image();
img_libertarian.src = "assets/values/libertarian.svg";
var img_paternalist = new Image();
img_paternalist.src = "assets/values/paternalist.svg";
//Economics axis
var img_planned = new Image();
img_planned.src = "assets/values/planned.svg";
var img_laissez = new Image();
img_laissez.src = "assets/values/laissez.svg";
//Authority axis
var img_autocracy = new Image();
img_autocracy.src = "assets/values/autocracy.svg";
var img_democracy = new Image();
img_democracy.src = "assets/values/democracy.svg";
//Partisanship axis
var img_partisan = new Image();
img_partisan.src = "assets/values/partisan.svg";
var img_nonpartisan = new Image();
img_nonpartisan.src = "assets/values/nonpartisan.svg";
//Creates canvas
var makeUserCanvas = function (ptnl_input, stat_input, auth_input, part_input, dark, ideology) {
    //Parsing input values into numbers
    var ptnl = parseFloat(ptnl_input);
    var stat = parseFloat(stat_input);
    var auth = parseFloat(auth_input);
    var part = parseFloat(part_input);
    //toFixed(1) of all values (converts to string with 1 decimal)
    var libertarian = ptnl.toFixed(1);
    var planned = stat.toFixed(1);
    var autocracy = auth.toFixed(1);
    var partisan = part.toFixed(1);
    var paternalist = (100 - ptnl).toFixed(1);
    var laissez = (100 - stat).toFixed(1);
    var democracy = (100 - auth).toFixed(1);
    var nonpartisan = (100 - part).toFixed(1);
    //Canvas drawing
    var c = document.createElement("canvas");
    var ctx = c.getContext("2d");
    c.width = 800;
    c.height = 650;
    if (dark == true) {
        ctx.fillStyle = "#333";
    }
    else {
        ctx.fillStyle = "#EEE";
    }
    //Drawing value images
    ctx.fillRect(0, 0, 800, 650);
    ctx.drawImage(img_libertarian, 20, 170, 100, 100);
    ctx.drawImage(img_paternalist, 680, 170, 100, 100);
    ctx.drawImage(img_planned, 20, 290, 100, 100);
    ctx.drawImage(img_laissez, 680, 290, 100, 100);
    ctx.drawImage(img_autocracy, 20, 410, 100, 100);
    ctx.drawImage(img_democracy, 680, 410, 100, 100);
    ctx.drawImage(img_partisan, 20, 530, 100, 100);
    ctx.drawImage(img_nonpartisan, 680, 530, 100, 100);
    //Drawing bar background
    ctx.fillStyle = "#222222";
    for (var i = 0, len = 4; i < len; i++) {
        ctx.lineJoin = "round";
        ctx.lineWidth = 75;
        ctx.strokeRect(165, 220 + 120 * i, 470, 0);
    }
    //Drawing bars
    ctx.lineJoin = "round";
    ctx.lineWidth = 65;
    //Paternalism axis
    if (ptnl >= 50) {
        ctx.strokeStyle = "#00F";
        ctx.strokeRect(636 - 4.72 * (100 - ptnl), 220, 4.72 * (100 - ptnl) - 2, 0);
        ctx.strokeStyle = "#B22222";
        ctx.strokeRect(166, 220, 4.72 * ptnl - 2, 0);
    }
    else {
        ctx.strokeStyle = "#B22222";
        ctx.strokeRect(166, 220, 4.72 * ptnl - 2, 0);
        ctx.strokeStyle = "#00F";
        ctx.strokeRect(636 - 4.72 * (100 - ptnl), 220, 4.72 * (100 - ptnl) - 2, 0);
    }
    //Economic axis
    if (stat >= 50) {
        ctx.strokeStyle = "#333";
        ctx.strokeRect(636 - 4.72 * (100 - stat), 340, 4.72 * (100 - stat) - 2, 0);
        ctx.strokeStyle = "#EDB509";
        ctx.strokeRect(166, 340, 4.72 * stat - 2, 0);
    }
    else {
        ctx.strokeStyle = "#EDB509";
        ctx.strokeRect(166, 340, 4.72 * stat - 2, 0);
        ctx.strokeStyle = "#333";
        ctx.strokeRect(636 - 4.72 * (100 - stat), 340, 4.72 * (100 - stat) - 2, 0);
    }
    //Authority axis
    if (auth >= 50) {
        ctx.strokeStyle = "#FF0000";
        ctx.strokeRect(636 - 4.72 * (100 - auth), 460, 4.72 * (100 - auth) - 2, 0);
        ctx.strokeStyle = "#00F";
        ctx.strokeRect(166, 460, 4.72 * auth - 2, 0);
    }
    else {
        ctx.strokeStyle = "#00F";
        ctx.strokeRect(166, 460, 4.72 * auth - 2, 0);
        ctx.strokeStyle = "#FF0000";
        ctx.strokeRect(636 - 4.72 * (100 - auth), 460, 4.72 * (100 - auth) - 2, 0);
    }
    //Partisanship axis
    if (part >= 50) {
        ctx.strokeStyle = "#EE2436";
        ctx.strokeRect(636 - 4.72 * (100 - part), 580, 4.72 * (100 - part) - 2, 0);
        ctx.strokeStyle = "#C000FF";
        ctx.strokeRect(166, 580, 4.72 * part - 2, 0);
    }
    else {
        ctx.strokeStyle = "#C000FF";
        ctx.strokeRect(166, 580, 4.72 * part - 2, 0);
        ctx.strokeStyle = "#EE2436";
        ctx.strokeRect(636 - 4.72 * (100 - part), 580, 4.72 * (100 - part) - 2, 0);
    }
    //Top info
    if (dark == true) {
        ctx.fillStyle = "#DDDDDD";
    }
    else {
        ctx.fillStyle = "#222222";
    }
    ctx.font = "700 50px Source Sans Pro";
    ctx.textAlign = "left";
    ctx.fillText("State Values", 20, 90);
    ctx.font = "30px Source Sans Pro";
    ctx.fillText("Closest Match: " + ideology, 20, 130);
    //Left column percentages
    ctx.font = "50px Source Sans Pro";
    ctx.textAlign = "left";
    ctx.fillStyle = "#000";
    if (ptnl > 30) {
        ctx.fillText(libertarian + "%", 150, 237.5);
    }
    if (stat > 30) {
        ctx.fillText(planned + "%", 150, 357.5);
    }
    if (auth > 30) {
        ctx.fillText(autocracy + "%", 150, 477.5);
    }
    if (part > 30) {
        ctx.fillText(partisan + "%", 150, 597.5);
    }
    //Right column percentages
    ctx.textAlign = "right";
    if (ptnl < 70) {
        ctx.fillText(paternalist + "%", 650, 237.5);
    }
    if (stat < 70) {
        ctx.fillText(laissez + "%", 650, 357.5);
    }
    if (auth < 70) {
        ctx.fillText(democracy + "%", 650, 477.5);
    }
    if (part < 70) {
        ctx.fillText(nonpartisan + "%", 650, 597.5);
    }
    //Adds more text on the top
    if (dark == true) {
        ctx.fillStyle = "#DDDDDD";
    }
    else {
        ctx.fillStyle = "#222222";
    }
    ctx.font = "300 25px Source Sans Pro";
    ctx.fillText("steelsmasher93.github.io/state-values", 780, 40);
    ctx.fillText(version, 780, 70);
    //Draw array matches
    ctx.textAlign = "center";
    ctx.font = "bold 30px Source Sans Pro";
    //@ts-ignore
    ctx.fillText("Paternalism Axis: " + setLabel(ptnl, ptnl_array), 400, 170);
    //@ts-ignore
    ctx.fillText("Economic Axis: " + setLabel(stat, stat_array), 400, 290);
    //@ts-ignore
    ctx.fillText("Authority Axis: " + setLabel(auth, auth_array), 400, 410);
    //@ts-ignore
    ctx.fillText("Partisanship Axis: " + setLabel(part, part_array), 400, 530);
    //@ts-ignore
    document.getElementById("banner").src = c.toDataURL();
};
