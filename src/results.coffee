#Gets variables from url query and parses them into individual variables
getQueryVariable = (variable) ->
    query = window.location.search.substring(1)
    vars = query.split("&")
    i = 0
    while i < vars.length
        pair = vars[i].split("=")
        if pair[0] is variable
            return pair[1]
        i++
    return(NaN)

#Sets the value for each bar div (if value is over 20%)
setBarValue = (name, value) ->
    innerel = document.getElementById(name)
    outerel = document.getElementById("bar-" + name)
    outerel.style.width = value + "%"
    innerel.innerHTML = value + "%"
    if value < 20
        innerel.style.display = "none"
    else
        innerel.style.display = "block"

#Sets the label for each axis
setLabel = (val,ary) ->
    if val > 100
        return ""
    else if val > 80 
        return ary[0]
    else if val > 60
        return ary[1]
    else if val >= 40
        return ary[2]
    else if val >= 20
        return ary[3]
    else if val >= 0
        return ary[4]
    else
        return ""

#Defines value of each value
paternalist = getQueryVariable("a")
planned     = getQueryVariable("b")
autocracy   = getQueryVariable("c")
partisan    = getQueryVariable("d")
libertarian = (100 - paternalist).toFixed(1)
laissez     = (100 - planned    ).toFixed(1)
democracy   = (100 - autocracy  ).toFixed(1)
nonpartisan = (100 - partisan   ).toFixed(1)


#Sets bar values for all bars
#Left collumn
setBarValue("paternalist", paternalist)
setBarValue("planned", planned)
setBarValue("autocracy", autocracy)
setBarValue("partisan", partisan)
#Right collumn
setBarValue("libertarian", libertarian)
setBarValue("laissez", laissez)
setBarValue("democracy", democracy)
setBarValue("nonpartisan", nonpartisan)


#Sets label for all axis divs
document.getElementById("ptnl-label").innerHTML = setLabel(paternalist, ptnl_array)
document.getElementById("stat-label").innerHTML = setLabel(planned, stat_array)
document.getElementById("auth-label").innerHTML = setLabel(autocracy, auth_array)
document.getElementById("part-label").innerHTML = setLabel(partisan, part_array)

#Finds closest match to this user
match = ""
userdist = Infinity
for ideology in ideologies
    dist = 0
    dist += Math.pow(Math.abs(ideology.stats.ptnl - paternalist), 2)
    dist += Math.pow(Math.abs(ideology.stats.stat - planned), 2)
    dist += Math.pow(Math.abs(ideology.stats.auth - autocracy), 2)
    dist += Math.pow(Math.abs(ideology.stats.part - partisan), 2)
    if dist < userdist
        match = ideology.ideology
        userdist = dist
document.getElementById("user-label").innerHTML = match

#Starts canvas element and sets darkmode to true if present
window.onload = -> 
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)
        darkmode = true
    else
        darkmode = false
    makeUserCanvas(paternalist,planned,partisan,autocracy,darkmode,match)