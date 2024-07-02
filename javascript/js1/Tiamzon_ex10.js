// This program computes the distance between two sets of coordinates, typically linked to a party location. It then identifies the nearest and farthest distances from a specified starting point.
// Created by: Edgar Alan Emmanuel B. Tiamzon III
// B1L
// 11-21-23
// Assisted by: Euan Jed Tabamo

// Global variables / paralell arrays
var names = ["Chelsea","Ralph","Andrew","Dustin"];
var coordinates = [[-3,3],[8,9],[6,7],[15,12]];
var home = [3,4];
var farth, near;

// This function gets the formula of the distance.
function getDistance(x1,x2,y1,y2){
    var a = x1 - x2;
    var b = y1 - y2;
    var c = Math.sqrt(a*a + b*b);
    return c
}

// This function collects and manages the specified origin array and all other coordinates.
function processMap(names, coordinates, home){
    var chelsea = getDistance(home[0], coordinates[0][0], home[1], coordinates[0][1]).toFixed(3);
    console.log("Chelsea's distance from HOME: " +chelsea);
    var ralph = getDistance(home[0], coordinates[1][0], home[1], coordinates[1][1]).toFixed(3);
    console.log("Ralph's distance from HOME: " +ralph);
    var andrew = getDistance(home[0], coordinates[2][0], home[1], coordinates[2][1]).toFixed(3);
    console.log("Andrew's distance from HOME: " +andrew);
    var dustin = getDistance(home[0], coordinates[3][0], home[1], coordinates[3][1]).toFixed(3);
    console.log("Dustin's distance from HOME: "+dustin);

    return [Number(chelsea),Number(ralph),Number(andrew),Number(dustin)];
}

// This function finds the farthest distance from the starting point.
function findFarthest(coordinates){
    var distance = [];
    for (let i = 0; i < coordinates.length; i++){
        var calcudistance = getDistance(home[0], coordinates[i][0], home[1], coordinates[i][1]);
        distance.push(calcudistance);
    }
    var farth = distance[0];
    
    var i = 1;
    while (i < distance.length){
       if(distance[i] > farth){
        farth = distance[i];
       }
       i++;

    }
        return farth;
}

// This function finds the nearest distance from the starting point.
function findNearest(coordinates){
    var distance = [];
    for (let i = 0; i < coordinates.length; i++){
        var calcudistance = getDistance(home[0], coordinates[i][0], home[1], coordinates[i][1]);
        distance.push(calcudistance);
    }
    var near = distance[0];

    var i = 1;
    while (i < distance.length){
        if(distance[i] < near){
            near = distance[i];
        }
        i++;
    }
        return near;
}

//This display all the console log
console.log("The longest distance from HOME is in Dustin's at " +findFarthest(coordinates).toFixed(3));
console.log("The nearest distance from HOME is in Andrew's at "+findNearest(coordinates).toFixed(3));
console.log("\n");
console.log("All locations away from HOME");
console.log("\n");
processMap(names, coordinates, home);



