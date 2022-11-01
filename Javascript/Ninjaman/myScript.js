var world = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ];

var worldDictionary = {
    0: 'blank', 
    1: 'wall',
    2: 'sushi',
    3: 'onigiri'
}

var ninjaman = {
    x: 0,
    y: 0
}

var bluey = {
    x: 9,
    y: 8
}

var red = {
    x: 9,
    y: 0
}

var pumpky = {
    x: 0,
    y: 8
}

var score = 0;
var lives = 3;

function createWorld(){
    for (var row = 0; row < world.length; row++) {
        for (var column = 0; column < world[row].length; column++) {
            if ((row == 0 && column == 0) || (row == 0 && column == 9) || (row == 8 && column == 0) || (row == 8 && column == 9)){
                world[row][column] = 0;
            }
            else {
                world[row][column] = Math.floor(Math.random() * 4);
            }
        }
    }
}

function drawWorld(){
    output = "";
    for (var row = 0; row < world.length; row++){
        output += "<div class = 'row'>";
        for (var x = 0; x < world[row].length; x++) {
            output += "<div class = '" + worldDictionary[world[row][x]] + "'></div>";
        }
        output += "</div>";
    }
    document.getElementById('world').innerHTML = output;
}

function drawNinjaMan(){
    document.getElementById('ninjaman').style.top = ninjaman.y * 40 + 'px';
    document.getElementById('ninjaman').style.left = ninjaman.x * 40 + 'px';

}

function drawGhosts(){
    document.getElementById('bluey').style.top = bluey.y * 40 + 'px';
    document.getElementById('bluey').style.left = bluey.x * 40 + 'px';
    document.getElementById('red').style.top = red.y * 40 + 'px';
    document.getElementById('red').style.left = red.x * 40 + 'px';
    document.getElementById('pumpky').style.top = pumpky.y * 40 + 'px';
    document.getElementById('pumpky').style.left = pumpky.x * 40 + 'px';
}

function determineDirection(ghostx, ghosty){
    if (ghostx == ninjaman.x && ghosty == ninjaman.y) {
        return 0; //ghost prefers not to move
    }
    else if(Math.abs(ghostx - ninjaman.x) >= Math.abs(ghosty - ninjaman.y)){
        if(ghostx > ninjaman.x && world[ghosty][ghostx-1] != 1 && ghostx>0){
            return 1; //ghost prefers to move left
        }
        else if(ghostx < ninjaman.x && world[ghosty][ghostx+1] != 1 && ghostx<9){
            return 2; //ghost prefers to move right
        }
        else if(ghosty > ninjaman.y && world[ghosty-1][ghostx] != 1 && ghosty>0){
            return 4; //ghost prefers to move up
        }
        else if(ghosty < ninjaman.y && world[ghosty+1][ghostx] != 1 && ghosty<9){
            return 3; //ghost prefers to move down
        }
        //section below removed because it's causing unknown issues
        else if(world[ghosty-1][ghostx] != "1" && ghosty>0){
            return 4; //ghost has to move up if possible
        }
        else if(world[ghosty+1][ghostx] != "1" && ghosty<9){
            return 3; //ghost has to move down if possible
        }
        else if(world[ghosty][ghostx+1] != "1" && ghostx<9){
            return 2; //ghost has to move right if possible
        }
    }
    else if(Math.abs(ghostx - ninjaman.x) < Math.abs(ghosty - ninjaman.y)){
        if(ghosty > ninjaman.y && world[ghosty-1][ghostx] != 1 && ghosty>0){
            return 4; //ghost prefers to move up
        }
        else if(ghosty <= ninjaman.y && world[ghosty+1][ghostx] != 1 && ghosty<9){
            return 3; //ghost prefers to move down
        }
        else if(ghostx < ninjaman.x && world[ghosty][ghostx+1] != 1 && ghostx<9){
            return 2; //ghost prefers to move right
        }
        else if(ghostx > ninjaman.x && world[ghosty][ghostx-1] != 1 && ghostx>0){
            return 1; //ghost prefers to move left
        }
        //section below removed because it's causing unknown issues
        /*else if(world[ghosty][ghostx-1] != 1 && ghostx>0){
            return 1; //ghost has to move left if possible
        }
        else if(world[ghosty][ghostx+1] != 1 && ghostx<9){
            return 2; //ghost has to move right if possible
        }
        else if(world[ghosty+1][ghostx] != 1 && ghosty<9){
            return 3; //ghost has to move down if possible
        }*/
    else
        return 5; //ghost has no preference
    }
}

function moveGhosts(){
    var result = determineDirection(bluey.x, bluey.y);
    if (result == 0){
        return; //end function as ghost has captured ninjaman
    }
    else if (result === 1){
        bluey.x--;
    }
    else if (result === 2){
        bluey.x++;
    }
    else if (result === 3){
        bluey.y++;
    }
    else if (result === 4){
        bluey.y--;
    }

    result = determineDirection(red.x, red.y);
    if (result == 0){
        return; //end function as ghost has captured ninjaman
    }
    else if (result === 1){
        red.x--;
    }
    else if (result === 2){
        red.x++;
    }
    else if (result === 3){
        red.y++;
    }
    else if (result === 4){
        red.y--;
    }

    result = determineDirection(pumpky.x, pumpky.y);
    if (result === 0){
        return; //end function as ghost has captured ninjaman
    }
    else if (result === 1){
        pumpky.x--;
    }
    else if (result === 2){
        pumpky.x++;
    }
    else if (result === 3){
        pumpky.y++;
    }
    else if (result === 4){
        pumpky.y--;
    }
}

function main(){
    document.onkeydown = function(e){
        console.log(e);
        if (e.keyCode == 37 && ninjaman.x > 0 && world[ninjaman.y][ninjaman.x-1] != 1){ // LEFT
            ninjaman.x--;
        }
        else if (e.keyCode == 39 && (ninjaman.x < 9) && world[ninjaman.y][ninjaman.x+1] != 1) { // RIGHT
            ninjaman.x++;   		
        }
        else if (e.keyCode == 40 && (ninjaman.y < 9) && world[ninjaman.y+1][ninjaman.x] != 1) { // DOWN
            ninjaman.y++;
        }
        else if (e.keyCode == 38 && ninjaman.y > 0 && world[ninjaman.y-1][ninjaman.x] != 1) { // UP
            ninjaman.y--;
        }
        drawNinjaMan();
        drawGhosts();
        moveGhosts();
        if ((((ninjaman.y == bluey.y) && (ninjaman.x == bluey.x)) || ((ninjaman.y == red.y) && (ninjaman.x == red.x)) || ((ninjaman.y == pumpky.y) && (ninjaman.x == pumpky.x))) && (lives > 0)) {
            ninjaman.y = 0;
            ninjaman.x = 0;
            bluey.x = 9;
            bluey.y = 8
            pumpky.x = 0;
            pumpky.y = 8;
            red.x = 9;
            red.y = 0;
            lives--;
            drawNinjaMan();
            if (lives == 0) {
                console.log("GAME OVER");
                console.log("Final score: " + score);
                return;
            }
            else if (lives < 0) {
                console.log("Stop playing! The game is over!")
            }
            else if (lives == 1) {
                console.log("You have 1 life left.")
            }
            else {
                console.log("You have " + lives + " lives left.");
            }
        }
        drawGhosts();
        if ((world[ninjaman.y][ninjaman.x] == 2) && (lives > 0)) {
            world[ninjaman.y][ninjaman.x] = 0;
            score += 10;
            console.log("Your score is " + score);
        }
        else if ((world[ninjaman.y][ninjaman.x] == 3) && (lives > 0)) {
            world[ninjaman.y][ninjaman.x] = 0;
            score += 5;
            console.log("Your score is " + score);
        }
        drawWorld();
        }
}

console.log("Welcome to Ninjaman! You start with 3 lives.\nAvoid the ghosts and collect sushi and onirigi to score points.\nTry to top your high score!")
createWorld();
drawWorld();
drawNinjaMan();
drawGhosts();
main();
