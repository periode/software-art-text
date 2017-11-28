var tracks = [0, -1, -1];

var upcoming = ["distant", "approaching", "inevitable"];
var instant = 0;
var happening = upcoming[instant];


var here = [0, 0, 1];

var individual;




var still = true;


var commuters = [];
var crowd = 27;
var noise;

var other;

var touch = false;
var eye_contact = null;

var alone = true;
var enough = false;

var moment = new Date();
var mood = -1;
var heaviness, sun;

var now = moment.getSeconds();
var then;

var step = 0.0002;


var lingering;






function Human(_x, _y, _z){
	this.age = Math.random()*7+70;
	this.thoughts = [];
	this.thoughts[0] = '~';
	this.position = [_x, _y, _z];
}

Human.prototype.obsess = function() {
	//he hasn't had enough yet, but he might
	if(Math.random() < 0.005){
		enough = true;
		still = false;
	}


	//do an http request to that link
	//MAKE THOSE APPEAR IN IFRAMES
	// else
		// loadStrings('http://www.tdcj.state.tx.us/death_row/dr_info/mastersonrichardlast.html', linger);
};

Human.prototype.linger = function(t){
	for(var i = 0; i < 100; i++){
		thoughts += t[Math.floor(Math.random()*t.length)];
	}
};


document.addEventListener("DOMContentLoaded", function(){

	individual = new Human(window.innerWidth*0.5, 1, 1);

	for(var i = 0; i < crowd; i++){
		others[i] = new Human(Math.random()*window.innerWidth, Math.random()*window.innerHeight, 1);
	}

	//there is someone else, you
	other =  {
		'self' : navigator.userAgent,
		'position' : [individual.position[0]+Math.random()*10, 1, 1]
	};


	if(moment.getMonth() > 5 && moment.getMonth() < 10)
		mood -= heaviness;

	sun = moment.getHours();
	mood += sun;

	setTimeout(function(){
		while(alone){

			individual.obsess();

			noise++;

			//move position until they are close to each other
			if(!still){
				pace();
			}

			//make sure to remove the alone (except if death?)
		}

		console.log('nothing else to talk about');
	}, 3000);
});

function say(){
	var words = document.createElement("input");
	document.body.appendChild(words);
	//you get to say something at the end
}

function pace(){//THIS IS WHERE ALONE IS TURNED TO FALSE INSHALLAH

	then = now;
	now = moment.getSeconds();

	instant+=0.0001;
	happening = upcoming[Math.floor(instant)];

	//this is the physical movement
	still = false;
	if(other.position[0] < individual.position[0])
		other.position[0] += step;
	else
		other.position[0] -= step;

	if(other.position[0] - individual.position[0] < step*2)
		resolve();
}

function reach(){
	if(!touch){
		console.log('touched');
		touch = true;
		say();
	}
}

function stare(){ //TODO DOES NOT WORK

	var gaze = {video: true};

	if(navigator.getUserMedia) {

		navigator.getUserMedia(gaze, function(stream) {
			console.log('oh you\'ve got blue eyes');
			eye_contact = stream;
		}, function(error){console.log('you closed your eyes',error);});

	} else if(navigator.webkitGetUserMedia) {

		navigator.webkitGetUserMedia(gaze, function(stream){
			console.log('oh you\'ve got grey eyes');
			eye_contact = stream;
		}, function(error){console.log('you closed your eyes',error);});

	}
	else if(navigator.mozGetUserMedia) {

		navigator.mozGetUserMedia(gaze, function(stream){
			console.log('oh you\'ve got green eyes');
			eye_contact = stream;
		}, function(error){console.log('you closed your eyes',error);});

	}


	console.log('got eye contact');
	if(touch){
		console.log('falling in love');
		fall(love);
	}else {
		console.log('dropping dead');
		fall(tracks);
	}
}


function resolve(){

	if(individual.position[1] > tracks[1])
		individual.position[1] -= step*0.5;

	//TODO: HAVE A FUNCTION THAT GOES WHAT IF WHAT IF NOT
	//some sort of boolean that switches back and forth
	//individual.ponder(['what', 'if']);

	console.log('hero',individual.position[1],'tracks',tracks[1], happening);
	if(happening != 'inevitable')
		stare();
}

function fall(self){
	if(self === undefined){
		alone = false;
		console.log('to exist with someone else');
	}else{
		alone =  false;
		console.log('to cease to exist');
	}
}

//TODO:
// 1-make sure that we get a video stream possible
// 2-make sure that there is an answer
// 3-deal if text input
// 4-change load strings into an xmlhttprequest and get specific elements into an array
