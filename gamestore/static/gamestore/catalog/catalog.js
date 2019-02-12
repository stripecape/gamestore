var WIDTH = 500;
var HEIGHT = 500;
var page = 1;
var games = [{
"name" : "Sudoku Shooter",
"info" : " to the SETTING message). A version that's inside an iframe already can be found at https://andriamanitra.github.io/games/Sudoku/",
"url" : "https://andriamanitra.github.io/games/Sudoku/game.html"
},
{
"name" : "Swat_Kats revisited",
"info" : "Instructions of the game: Game playing instructions are in the game.Move the plane with arrow keys and shoot using space bar. Avoid colliding with the enemies. Also going in close proximity to the dark cloud causes gameover.",
"url" : "https://cdn.rawgit.com/Shaptarshi-Basu/flightGame/f10e93bc/game.html"
},
{
"name" : "Click the Square",
"info" : "http://frightening-drink.surge.sh/",
"url" : "Instructions of the game: Instructions can be found at the game page."
},

{
"name" : "Pong",
"info" : "Instructions of the game: Up and down arrows move the block representing the player's bat on the left. A simple ai plays against the player on the right. The ball's speed increases on each horizontal direction change.",
"url" : "https://milanfin.github.io/pong.html"
},
{
"name" : "Breakout",
"info" : "Instructions of the game: A simple breakout game where the player aims to remove all blocks from the game board. This is done by hitting them with the ball. The ball can be bounced back with the paddle on the bottom of the game board. The paddle can be moved with arrow keys. The direction the ball bounces to can be altered by using the left or right third of the paddle. Once all blocks are cleared from the board, new blocks will spawn and a new level will start. The game ends when the ball crosses the line on the bottom of the game board. Game can be paused by pressing 'P'.",
"url" : "https://eki95.github.io/jsGame/jsGame.html"
},
{
"name" : "Tom and Jerry",
"info" : "Instructions of the game: Eat as much as you can while running away from Tom. Your score will be saved automatically after eating cheese. You can also save the game by clicking anywhere on the screen. Wish you luck!!!",
"url" : "https://niloufarvalinejad.github.io/"
},
{
"name" : "Single player pong",
"info" : "Instructions of the game: Instructions of the game: Do not let the ball pass your paddle. The ball's speed increases on each paddle hit. The paddle can be moved with left and right arrow keys.",
"url" : "http://www.students.tut.fi/~salmin23/Single_player_pong.html"
},
{
"name" : "The Snake",
"info" : "Instructions of the game:",
"url" : "https://cdn.rawgit.com/niskaman/wsd18/05a710bc/snake4.html"
},
{
"name" : "Super Complex And Original Game",
"info" : "Instructions of the game: Jump till you die, then jump more",
"url" : "https://cdn.rawgit.com/Cunen/McDonaldsGames/f16e1fbd/Game.html"
},
{
"name" : "Math game",
"info" : "Instructions of the game: Game is simple. Start by pressing 'New problem' where you are presented with new problem where you calculate sum of two numbers. Check your solution with 'Check' and you are presented with results. Points you get are 10 pts times winstreak. So first right answer is 10 points second is 20 and so on. You can press save, which saves score and winstreak. You can also load state, if you have database which stores and handles your save data. Submit score sends out current score.",
"url" : "https://math-game-site.herokuapp.com/math_game.html"
},
{
"name" : "Space Waifus Lite",
"info" : "Instructions of the game: A super simple dating simulator based on the hit game Space Waifus",
"url" : "https://hot-gun.surge.sh/"
}];
var game_xy = [
  {"x":75,"y":72},
  {"x":325,"y":72},
  {"x":75,"y":144},
  {"x":325,"y":144},
  {"x":75,"y":216},
  {"x":325,"y":216},
  {"x":75,"y":288},
  {"x":325,"y":288},
  {"x":75,"y":360},
  {"x":325,"y":360}
  ];
var welcome_text;
var game_placholder;
var stage;
var context;
var queue;
var page_number;
var arrow_left;
var  arrow_right;
var game_objects = [];
var game_name;
var game_info;
var text_hitarea = [];
var buy_game;
var rightarrowimg;

window.onload = function(){
  var canvas = document.getElementById('game_catalog_canvas');
  context = canvas.getContext('2d');
  context.canvas.height = HEIGHT;
  context.canvas.width = WIDTH;

  stage = new createjs.Stage('game_catalog_canvas');

  queue = new createjs.LoadQueue(false);
  //rightarrowimg = img.crossOrigin="images/arrow_right.png"
  queue.on("complete", queueLoad, this)
  queue.loadManifest([
    {id:'game_placholder', src:'wsd2018project/games/game_placeholder.png'},
    {id:'arrow_left_img', src:'arrow_left.png'},
    {id:'arrow_right_img', src:"static 'gamestore/images/icon.png'"}
  ]);
  document.getElementById("search").addEventListener("click", show_catalog);

}

function queueLoad(event) {

  //Tehdään pelien teksteille objectit
  for ( var i = 0; i < 10; i++){
    game_objects.push(new createjs.Text("", "15px Arial", "Black"));
  }

  //Tehdään pelien teksteille hitbox
  for ( var i = 0; i < 10; i++){
    text_hitarea.push(new createjs.Shape());
  }

  game_objects.forEach(function(element){
    element.visible = false;
    stage.addChild(element);
  })

  welcome_text = new createjs.Text("Welcome to the store!", "30px Arial", "Black");
  welcome_text.name = "welcome_text";
  welcome_text.x = 250 - (welcome_text.getBounds().width)/2;
  welcome_text.y = 250 - (welcome_text.getBounds().height)/2;
  stage.addChild(welcome_text);

  page_number = new createjs.Text(page.toString(), "30px Arial", "Black");
  page_number.visible = false;
  stage.addChild(page_number);

  game_name = new createjs.Text("blank", "30px Arial", "Black");
  game_info = new createjs.Text("", "15px Arial", "Black");
  game_name.visible = false;
  game_info.visible = false;
  stage.addChild(game_name);
  stage.addChild(game_info);

  var buyhit = new createjs.Shape();
  buy_game = new createjs.Text("Buy", "20px Arial", "Black");
  buyhit.graphics.beginFill("#000").drawRect(0,0,buy_game.getMeasuredWidth(),buy_game.getMeasuredHeight());
  buy_game.hitArea = buyhit;
  buy_game.x = 250 - buy_game.getMeasuredWidth()/2;
  buy_game.y = 450;
  buy_game.visible = false;
  stage.addChild(buy_game);

  arrow_left = new createjs.Bitmap(document.getElementById("arrow_left"));
  arrow_left.scaleX = 0.5;
  arrow_left.scaleY = 0.5;
  arrow_left.visible = false;
  arrow_left.x = 100;
  arrow_left.y = 400;
  stage.addChild(arrow_left);

  arrow_right = new createjs.Bitmap(document.getElementById("arrow_right"));
  arrow_right.scaleX = 0.5;
  arrow_right.scaleY = 0.5;
  arrow_right.visible = false;
  arrow_right.x = 350;
  arrow_right.y = 400;
  stage.addChild(arrow_right);

  back_button = new createjs.Bitmap(document.getElementById("arrow_left"));
  back_button.scaleX = 0.5;
  back_button.scaleY = 0.5;
  back_button.visible = false;
  back_button.x = 10;
  back_button.y = 10;
  stage.addChild(back_button);

  stage.update();

  arrow_left.addEventListener("click", left_click);
  arrow_right.addEventListener("click", right_click);
  back_button.addEventListener("click", back_click);

  game_objects.forEach(function(element){
    element.addEventListener("click", function(){
      game_selected(element.text);
    });
  });
  buy_game.addEventListener("click", buy_clicked);
}

function buy_clicked(){
  console.log("asd");
}

function back_click(){
  game_name.visible = false;
  game_info.visible = false;
  back_button.visible = false;
  buy_game.visible = false;
  show_catalog();
}

function game_selected(gamename){
  console.log(gamename);
  buy_game.visible = true;
  game_objects.forEach(function(object){
    object.visible = false;
  });
  arrow_left.visible = false;
  arrow_right.visible = false;
  page_number.visible = false;

  games.forEach(function(el){
    if (el.name == gamename){
      for (i = 67; i< el.info.length; i = i+71){
        el.info = el.info.slice(0,i) + "\n\n" + el.info.slice(i, el.info.length);
      }
      game_name.text = el.name;
      game_info.text = el.info;
    }
  });
  game_name.x = 250 - (game_name.getBounds().width)/2;
  game_name.y = 10;
  game_info.x = 50;
  game_info.y = 100;
  game_name.visible = true;
  game_info.visible = true;
  back_button.visible = true;
  stage.update();

}

function left_click(){
  game_objects.forEach(function(element){
    element.visible = false;
  });
  page = page - 1;
  page_number.text = page.toString();
  show_catalog();
}
function right_click(){
  game_objects.forEach(function(element){
    element.visible = false;
  });
  page = page + 1;
  page_number.text = page.toString();
  show_catalog();
}



function show_catalog(){
  game_name.visible = false;
  game_info.visible = false;
  back_button.visible = false;
  buy_game.visible = false;
  welcome_text.visible = false;
  var i = 0;
  for (j = 0; j < page - 1; j++){
    j = j +9;
  }
  i = 0;

  for (k = j; k<=j+9;k++){
    if (games[k] != null){
      game_objects[i].text = games[k].name;
      game_objects[i].x = game_xy[i].x;
      game_objects[i].y = game_xy[i].y;
      game_objects[i].visible = true;

      text_hitarea[i].graphics.beginFill("#000").drawRect(0,0,game_objects[i].getMeasuredWidth(),game_objects[i].getMeasuredHeight());
      game_objects[i].hitArea = text_hitarea[i];
      i = i + 1;
    }
  }
  page_number.text = page.toString();
  page_number.x = 250 -(page_number.getBounds().width)/2;
  page_number.y = 425 -(page_number.getBounds().height)/2;
  page_number.visible = true;
  if (page == 1){
    arrow_left.visible = false;
  }else{
    arrow_left.visible = true;
  }

  if (page == Math.ceil(games.length / 10) ){
    arrow_right.visible = false;
  }else{
    arrow_right.visible = true;
  }
  stage.update();
}
