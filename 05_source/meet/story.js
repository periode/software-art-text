var life = true;
var lastWords = false;
var him;
var her;
var currentDate = new Date();
var time = currentDate.getHours();
var hope = 0;
var light = 50;
var timeToWakeUp = 10;
var music = false;
var memories;
var coffee = 70;

memories = [];

document.addEventListener("DOMContentLoaded", function(){

var end = document.getElementById("answer");
epilogue('the end is just the beginning');

var Sun = function(){
	this.pos = 0;
	pos++;
};

var Phone = function(a, b, c){
	this.number = parseFloat(a+''+b+''+c);
};

var Fate = function(o){
	this.obstacles = o;
	this.distance = 2+Math.random()*10;
	this.inAction = function(){
		hope++;
	};
};

var Human = function(a, w, h, aw, l, x, y, ws, p1, p2, p3, _h){
	this.age = a;
	this.weight = w;
	this.height = h;
	this.awake = aw;
	this.love = l;
	this.posX = x;
	this.posY = y;
	this.walkingSpeed = ws;
	this.havePhone = false;
	this.phone = new Phone(p1, p2, p3);
	this.heart = 'http://'+_h;
	this.memories = ["yesterday"];

	this.checkNeeds = function(){
		var needs = ["sunshine", "rest", "coffee"];

		var i = parseInt(Math.random()*needs.length);
		var n = needs[i];
		return n;
	};

	this.act = function(n){
		console.log(this,'felt the need to',n,'at',this.posX);
	if(n === "sunshine"){
				if(this.posX < light){
					while(this.posX < light){
						console.log("walking left", this.posX);
						this.posX += this.walkingSpeed;
					}

					if(this.posX > light) this.posX = light;
				}else{
					while(this.posX > light){
						console.log("walking right", this.posX);
						this.posX -= this.walkingSpeed;
					}

					if(this.posX < light) this.posX = light;
				}
		}else if(n == "rest"){

			this.posX = Math.min(parseInt(this.posX), parseInt(this.posX));

		}else if(n == "coffee"){
			if(this.posX < coffee){
					while(this.posX < coffee){
						this.posX += this.walkingSpeed;
					}

					if(this.posX > coffee) this.posX = coffee;
			}else{
				while(this.posX < coffee){
					this.posX -= this.walkingSpeed;
				}

				if(this.posX < coffee) this.posX = coffee;
			}
		}

		if(n == "coffee" || n == "sunshine"){
			if(Math.random() > 0.5){
				this.havePhone = false;
			}
		}
		console.log('position after action', this.posX);
	};

	this.getTaste = function(){
		var taste = parseInt(Math.random()*2);
		console.log('a taste of',taste);
		return taste;
	};

	this.smoke = function(cigarette){
		while(cigarette.length > 0){
			cigarette--;
		}
	};

	this.lookAt = function(o){
		var glance = new Fate();
		if(o == him || o == her){
			glance.inAction();
			console.log("one looked at the other");
		}else{
			this.walkingSpeed -= 0.001;
			console.log("one looked at a phone screen");
		}
	};

	this.talkTo = function(other){
		console.log("they talked to each other");
		var flash = "";
		try{ //TODO generate random URLs
			var url = other.heart;
			var xmlHttp = new XMLHttpRequest();
			var greet = 'hey';

			xmlHttp.onreadystatechange = function(){
				if(xmlHttp.readyState == 4 && xmlHttp.statut == 200){
					callback(xmlHttp.responseText);
				}
			};
			xmlHttp.open( "GET", url, true );
			xmlHttp.send( greet );

			flash = xmlHttp.responseText;
		} catch (e){
			//mistake of conversation
		} finally {
			flash = "hello";
		}

		return flash;
	};

	this.wakeUp = function(){
		this.awake = true;
	};
};

function timeStops(){
	time = time;
}

function epilogue(sentence){
	end.innerHTML = sentence;
	lastWords = true;
}

function fate(){
	var f = new Fate(null);
	console.log("it is");
	return f;
}

function inLine(Human, time){
	console.log('line');
	for(var i = 0; i < time; i++){
		wait();
	}
	him.talkTo(her);
}

function interact(one, another, reason){//might not work might have to go back (Human, Human, reason)
	console.log('interaction thanks to',reason);
	var r = Math.random();
	var newMemory, present;
	var past = her.memories;
	r = 0;
	if(r < 0.5){
		newMemory = her.talkTo(him);
		her.memories.push(newMemory);
		present = her.memories[0];
	}else{
		newMemory = him.talkTo(her);
		him.memories.push(newMemory);
		present = him.memories[0];
	}

	if(reason == 'music'){
		epilogue("their meeting was a melody");
	}else if(reason == 'stumble'){
		epilogue("their bodies met before their souls");
	}else if(reason == 'ignore'){
		epilogue("they were too busy to talk to each other");
	}
}

function wait(){
	var r = Math.random();
	var thought = memories[parseInt(r*memories.length)];

	 var past;
	 var present;
	 past = present;
}

if(life){
	var neighborhood = (parseInt(Math.random()*3));
	him = new Human(24, 73, 180, false, null, 62+neighborhood, 60, 2, 347, 458, 9804, '45.55.67.217');
	her = new Human(28, 64, 174, false, null, 57-neighborhood, 60, 1, 929, 428, 0719, '173.203.204.123');

	if(time > 10){
		him.wakeUp();
		her.wakeUp();
	}else{
		wait();
	}

	if(him.awake){
		var need = him.checkNeeds();
		him.act(need);
	}

	if(her.awake){
		var want = her.checkNeeds();
		her.act(want);
	}

	var immediacy = fate();

	console.log("hope",hope,'fate',immediacy.distance);

	if(Math.abs(her.posX - him.posX) < immediacy.distance){
		console.log("they are within distance...");
		if(her.havePhone && him.havePhone){
			console.log("...both looking at their phones");
			her.lookAt(her.phone);
			him.lookAt(him.phone);
		}

		if(!her.havePhone && him.havePhone){
			console.log("she looked");
			her.lookAt(him);
			him.lookAt(him.phone);
		}

		if(her.havePhone && !him.havePhone){
			console.log("he looked");
			her.lookAt(her.phone);
			him.lookAt(her);
		}

		if(!her.havePhone && !him.havePhone){
			console.log("they saw each other");
			him.lookAt(her);
			her.lookAt(him);
			timeStops();

			if(him.checkNeeds() == 'coffee'){
				console.log("they listened");
				inLine(him, 2);
				inLine(her, 3);
				music = true;
				window.open("jeteveux.mp3");
				epilogue('it was a melody');
			}

			if(her.checkNeeds() == 'sunshine'){
				if(hope > 1){
					var marlboro = ['une', 'cigarette', 'tue', 'le', 'temps'];
					her.smoke(marlboro);
					him.lookAt(her);

					var chance = fate();
					var words = '';

					if(chance < 7){
						if(chance > 3.5){
							words = him.talkTo(her);
						}else{
							words = her.talkTo(him);
						}
					}else{
						epilogue("they met in a street, under the sun.");
					}
				}
			}
		}
	}

	console.log('he is at', him.posX, 'she is at', her.posX);

	if(him.posX == her.posX){
		console.log('they met at',her.posX);

		if(music === true && him.getTaste() == her.getTaste() && (!him.havePhone || !her.havePhone)){
			interact(him, her, 'music');
		}else if(music === false && him.getTaste() == her.getTaste() && (him.havePhone || her.havePhone)){
			interact(him, her, 'stumble');
		}else if(him.getTaste() != her.getTaste() && (him.havePhone || her.havePhone)){
			interact(him, her, 'ignore');
		}
	}


	var clue = "stories aren't always sentences";
	console.log(clue);
	}
});
