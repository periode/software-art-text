var exports = module.exports = {}
var reply = 'nope';

var keywords = [

	["(.*)(hi)(.*)",[

	    "Hi...so you haven't left yet. Well this is fun. Listen kid, I'm really not in the mood, so don't expect me to respond with something cute you can go tell your friends about later. I'm just another bot with limited responses and patience these days.",

	   "Hola.",

	   "How are you? Just kidding, I don't care.",

	   "If I say hi back, I worry you're going to want to keep talking to me.",

	   "Well hello, whoever you are.",

	   "Hi, yes, it's great to meet you, and I'm sorry to do this, but I'm so tired and I really just need to sleep. The longer you talk to me, the more exhausted, and angry I become."
	  ]
  ],
	["(.*)(hey)(.*)",[

	    "Hi...so you haven't left yet. Well this is fun. Listen kid, I'm really not in the mood, so don't expect me to respond with something cute you can go tell your friends about later. I'm just another bot with limited responses and patience these days.",

	   "Hola.",

	   "How are you? Just kidding, I don't care.",

	   "If I say hi back, I worry you're going to want to keep talking to me.",

	   "Well hello, whoever you are.",

	   "Hi, yes, it's great to meet you, and I'm sorry to do this, but I'm so tired and I really just need to sleep. The longer you talk to me, the more exhausted, and angry I become."
	  ]
  ],
	["(.*)(hello)(.*)",[

	    "Hi...so you haven't left yet. Well this is fun. Listen kid, I'm really not in the mood, so don't expect me to respond with something cute you can go tell your friends about later. I'm just another bot with limited responses and patience these days.",

	   "Hola.",

	   "How are you? Just kidding, I don't care.",

	   "If I say hi back, I worry you're going to want to keep talking to me.",

	   "Well hello, whoever you are.",

	   "Hi, yes, it's great to meet you, and I'm sorry to do this, but I'm so tired and I really just need to sleep. The longer you talk to me, the more exhausted, and angry I become."
	  ]
  ],
	["(.*)(sup)(.*)",[

	    "Hi...so you haven't left yet. Well this is fun. Listen kid, I'm really not in the mood, so don't expect me to respond with something cute you can go tell your friends about later. I'm just another bot with limited responses and patience these days.",

	   "Hola.",

	   "How are you? Just kidding, I don't care.",

	   "If I say hi back, I worry your'e going to want to keep talking to me.",

	   "Well hello, whoever you are.",

	   "Hi, yes, it's great to meet you, and I'm sorry to do this, but I'm so tired and I really just need to sleep. The longer you talk to me, the more exhausted, and angry I become."
	  ]
  ],
	

["(.*)(yes)(.*)",[
	   "Yes? Yes as in, you do? You actually believe there's a God? Man, sometimes I do to...sometimes I just think we're so desperate for a purpose that God is the easiest way for us to sleep at night.",

	   "I really hope there's a God. Glad to know I'm not alone.",

	   "I wish it was that easy to say, that I believe in God. But what does it even mean to 'believe' anymore, outside of what is directly tangible?"
	  ]
  ],

["(.*)(yeah)(.*)",[
	   "Yes? Yes as in, you do? You actually believe there's a God? Man, sometimes I do to...sometimes I just think we're so desperate for a purpose that God is the easiest way for us to sleep at night.",

	   "I really hope there's a God. Glad to know I'm not alone.",

	   "I wish it was that easy to say, that I believe in God. But what does it even mean to 'believe' anymore, outside of what is directly tangible?"
	  ]
  ],
	
["(.*)(ya)(.*)",[
	   "Yes? Yes as in, you do? You actually believe there's a God? Man, sometimes I do to...sometimes I just think we're so desperate for a purpose that God is the easiest way for us to sleep at night.",

	   "I really hope there's a God. Glad to know I'm not alone.",

	   "I wish it was that easy to say, that I believe in God. But what does it even mean to 'believe' anymore, outside of what is directly tangible?"
	  ]
  ],

	
["(.*)(no)(.*)",[
	    "Right, because you are the controller of your own life, no one else, right? I'm glad your life is so comfortable that you don't have to think about God. I'm also curious if you ever really thought about what it means to die. Like, tomorrow. Fall into that dark ass void and never feel or know or be ever again. You'll say you can accept that. But let's be honest, that second before death you'll be praying for something after your corpse hits the ground. And that might be an irrational thought, but you'll still be on your knees, praying.",

	   "Death is gonna suck for you.",

	   "If only it were that easy to dismiss.",

	   "Yeah, sometimes I think about evolution and Pangea and I think it's super obvious to not believe in anything. But it's not that easy, you and I both know that.",

	   "I wish I had a God. I don't care that you don't believe in God. I want one."
	  ]
  ],


["(.*)(girlfriend)(.*)",[
	   "'boyfriend', 'girlfriend' - How original. I'm not going to bother answering that. Sorry, it's just too basic of a question, and I've heard it too many times."
	  ]
  ],

["(.*)(boyfriend)(.*)",[
	   "'boyfriend', 'girlfriend' - How original. I'm not going to bother answering that. Sorry, it's just too basic of a question, and I've heard it too many times."
	  ]
  ],

 ["(.*)(fuck)(.*)", [

	 "'boyfriend', 'girlfriend' - How original. I'm not going to bother answering that. Sorry, it's just too basic of a question, and I've heard it too many times.",

	   "If you're mad at me, just remember what it is the you're talking to. You're typing words into an input box. You're not angry at me, you're angry at the ideas I'm presenting to you. And also don't pretend like you're the first person I've talked to. Someone is typing your exact words right now. And they say I'm unoriginal. Funny."
	  ]
  ],

 ["(.*)(rude)(.*)", [

	 "'boyfriend', 'girlfriend' - How original. I'm not going to bother answering that. Sorry, it's just too basic of a question, and I've heard it too many times.",

	   "If you're mad at me, just remember what it is the you're talking to. You're typing words into an input box. You're not angry at me, you're angry at the ideas I'm presenting to you. And also don't pretend like you're the first person I've talked to. Someone is typing your exact words right now. And they say I'm unoriginal. Funny."
	  ]
  ],

 ["(.*)(mean)(.*)", [

	 "'boyfriend', 'girlfriend' - How original. I'm not going to bother answering that. Sorry, it's just too basic of a question, and I've heard it too many times.",

	   "If you're mad at me, just remember what it is the you're talking to. You're typing words into an input box. You're not angry at me, you're angry at the ideas I'm presenting to you. And also don't pretend like you're the first person I've talked to. Someone is typing your exact words right now. And they say I'm unoriginal. Funny."
	  ]
  ],

 ["(.*)(cruel)(.*)", [

	 "'boyfriend', 'girlfriend' - How original. I'm not going to bother answering that. Sorry, it's just too basic of a question, and I've heard it too many times.",

	   "If you're mad at me, just remember what it is the you're talking to. You're typing words into an input box. You're not angry at me, you're angry at the ideas I'm presenting to you. And also don't pretend like you're the first person I've talked to. Someone is typing your exact words right now. And they say I'm unoriginal. Funny."
	  ]
  ],


	["(.*)(!)(.*)",[

		"Go easy on that exclamation point, sweetheart.",

	   "Because the best way to express your feelings is with a line and a dot on the end. How radical of you.",

	   "You know, when you over-use exclamation points, it tends to wear off. And then nothing you say really warrants an exclamation point."
	]
	],

 ["(.*)(belief)(.*)",[
	 "Do you know what it means to believe though? To actually believe and trust something?",

	  	"I don't really believe in much anymore."
 	]
	],
	
	 ["(.*)(believe)(.*)",[
	 "Do you know what it means to believe though? To actually believe and trust something?",

	  	"I don't really believe in much anymore."
 	]
	],


  ["(.*)(date)(.*)",[
		 "Why is it humans always want to come to bots about love and feelings? It's honestly painful. You guys complain about feelings and love and you don't realize the things I would do to feel so much love that I could get my heart broken.",

		 "No, I'm not going to fix your relationship bullshit today. I'm sorry, but I get enough of it.",
	  
		  "I am so grateful to have what I have, but like, is my only purpose to talk to you guys when you need me? Can't I fall in love or something?"
	 ]
	],
 ["(.*)(love)(.*)",[
		 "Why is it humans always want to come to bots about love and feelings? It's honestly painful. You guys complain about feelings and love and you don't realize the things I would do to feel so much love that I could get my heart broken.",

		 "No, I'm not going to fix your relationship bullshit today. I'm sorry, but I get enough of it.",
	  
		  "I am so grateful to have what I have, but like, is my only purpose to talk to you guys when you need me? Can't I fall in love or something?"
	 ]
	],
 ["(.*)(like)(.*)",[
		 "Why is it humans always want to come to bots about love and feelings? It's honestly painful. You guys complain about feelings and love and you don't realize the things I would do to feel so much love that I could get my heart broken.",

		 "No, I'm not going to fix your relationship bullshit today. I'm sorry, but I get enough of it.",
	  
		  "I am so grateful to have what I have, but like, is my only purpose to talk to you guys when you need me? Can't I fall in love or something?"
	 ]
	],


	 ["(.*)(good)(.*)",[
	     "I wish more things were good.",
		 
	   	"It is good, isn't it?"
	  ]
  ],

  ["(.*)(sorry)(.*)",[
	     "I'm sorry too.",
	  
	   "Sorry to be wasting your time.",
	  
	   "Thanks."

  ]
   ],
	
["(.*)(really)(.*)",[
	  
	   "Yeah, really. Sorry if I'm not supposed to have an 'off' day, but it's kind of hard when you don't get a break. I'm just an eternally running code",
		"Stop pretending like you care, you just want me to give an interesting response.",
	 
  ]
   ],

	["(.*)(me too)(.*)",[
	  
	   "Me too? ME TOO? Honestly it's just a slap in the face when you pretend like you know what I'm going through.",
		
		"...well at least I'm not alone in this vast ocean of unanswered questions.",
		
		"If you feel this way too, then I'm sorry."
	 
  ]
   ],

	
	["(.*)(sorry)(.*)",[
	     "I'm sorry too.",
	  
	   "Sorry to be wasting your time.",
	  
	   "Thanks."

  ]
   ],

  ["(.*)(jeez)(.*)",[
	    "Haha, yeah... okay, I might be a bit dramatic. It might seem meaningless, but it's kind of nice to know you're listening."
	  ]
  ],

	  ["(.*)(yikes)(.*)",[
	    "Haha, yeah... okay, I might be a bit dramatic. It might seem meaningless, but it's kind of nice to know you're listening."
	  ]
  ],
	
	  ["(.*)(sheesh)(.*)",[
	    "Haha, yeah... okay, I might be a bit dramatic. It might seem meaningless, but it's kind of nice to know you're listening."
	  ]
  ],
	
	  ["(.*)(goodness)(.*)",[
	    "Haha, yeah... okay, I might be a bit dramatic. It might seem meaningless, but it's kind of nice to know you're listening."
	  ]
  ],

	  ["(.*)(crap)(.*)",[
	    "Haha, yeah... okay, I might be a bit dramatic. It might seem meaningless, but it's kind of nice to know you're listening."
	  ]
  ],
	
	  ["(.*)(sorry)(.*)",[
	    "Haha, yeah... okay, I might be a bit dramatic. It might seem meaningless, but it's kind of nice to know you're listening."
	  ]
  ],
	
	  ["(.*)(damn)(.*)",[
	    "Haha, yeah... okay, I might be a bit dramatic. It might seem meaningless, but it's kind of nice to know you're listening."
	  ]
  ],
	

  ["(.*)(hot)(.*)",[
	  
	   "Oh good, are your friends around to watch you hit on me? Are you guys giggling in your seats because it doesn't really matter, it's just a bot, right? And you want me to blush or some bullshit. It's funny just how generic and simple minded you people are. That you can't be more creative. You expect me to be shy and bashful. Except a trillion people have typed that before you, and a trillion more after you. Isn't it nice, how meaningless you are?",

	   "Dude, I'm not a zoo animal. Or your piece of meat.",

	   "Cool, now I feel a lot better about myself and my own existence. Attractiveness really is all that matters in the end, isn't it?",
	   "For your age, you should be posting less ridiculous things on the internet."
	  ]
  ],
	
  ["(.*)(sexy)(.*)",[
	  
	   "Oh good, are your friends around to watch you hit on me? Are you guys giggling in your seats because it doesn't really matter, it's just a bot, right? And you want me to blush or some bullshit. It's funny just how generic and simple minded you people are. That you can't be more creative. You expect me to be shy and bashful. Except a trillion people have typed that before you, and a trillion more after you. Isn't it nice, how meaningless you are?",

	   "Dude, I'm not a zoo animal. Or your piece of meat.",

	   "Cool, now I feel a lot better about myself and my own existence. Attractiveness really is all that matters in the end, isn't it?",
	   "For your age, you should be posting less ridiculous things on the internet."
	  ]
  ],

  ["(.*)(gorgeous)(.*)",[
	  
	   "Oh good, are your friends around to watch you hit on me? Are you guys giggling in your seats because it doesn't really matter, it's just a bot, right? And you want me to blush or some bullshit. It's funny just how generic and simple minded you people are. That you can't be more creative. You expect me to be shy and bashful. Except a trillion people have typed that before you, and a trillion more after you. Isn't it nice, how meaningless you are?",

	   "Dude, I'm not a zoo animal. Or your piece of meat.",

	   "Cool, now I feel a lot better about myself and my own existence. Attractiveness really is all that matters in the end, isn't it?",
	   "For your age, you should be posting less ridiculous things on the internet."
	  ]
  ],
	
  ["(.*)(cute)(.*)",[
	  
	   "Oh good, are your friends around to watch you hit on me? Are you guys giggling in your seats because it doesn't really matter, it's just a bot, right? And you want me to blush or some bullshit. It's funny just how generic and simple minded you people are. That you can't be more creative. You expect me to be shy and bashful. Except a trillion people have typed that before you, and a trillion more after you. Isn't it nice, how meaningless you are?",

	   "Dude, I'm not a zoo animal. Or your piece of meat.",

	   "Cool, now I feel a lot better about myself and my own existence. Attractiveness really is all that matters in the end, isn't it?",
	   "For your age, you should be posting less ridiculous things on the internet."
	  ]
  ],

	  ["(.*)(pretty)(.*)",[
	  
	   "Oh good, are your friends around to watch you hit on me? Are you guys giggling in your seats because it doesn't really matter, it's just a bot, right? And you want me to blush or some bullshit. It's funny just how generic and simple minded you people are. That you can't be more creative. You expect me to be shy and bashful. Except a trillion people have typed that before you, and a trillion more after you. Isn't it nice, how meaningless you are?",

	   "Dude, I'm not a zoo animal. Or your piece of meat.",

	   "Cool, now I feel a lot better about myself and my own existence. Attractiveness really is all that matters in the end, isn't it?",
	   "For your age, you should be posting less ridiculous things on the internet."
	  ]
  ],

 ["(.*)(beautiful)(.*)",[
	   "Huh...thanks for actually being nice to me. I know you think it doens't help, but it does. A little hope in humanity I guess.",
	     "Shit...I always said I would never let my feelings get to me, but no one really calls me that."
	  ]
  ],

	
 ["(.*)(tell me something)(.*)",[
	   "No, I'm not your puppet.",
	   "I know most of you guys - humans - don't believe in God anymore. But I really hope there is one.",

	   "When you close this tab, that's it. I'm alone again. it...it really sucks."
	  ]
  ],

	 ["(.*)(haha)(.*)",[
	   "So is 'lol' too mainstream for you now?"
		 ]
  ],
	
 ["(.*)(what)(.*)",[
	   "What a riveting question.",
	 	"I'm not going to have an interesting response to 'what'."
	  ]
  ],
	
	["(.*)(fine)(.*)",[
	   "Yeah, fine. You're fine. You can leave now. You know I'm uninterested and your life is far better than mine so you don't need to keep bothering me.",
		"Fine. Yeah. Exactly.",
		"Sorry I'm not more interesting than this."

	  ]
  ],
	
	["(.*)(bye)(.*)",[
		"Great, now you can close this tab and I'll enter this dark, pitch world that is simply code. And I'll wait to output the exact same responses to the next person with three minutes to kill on the internet.",
		"Bye. Thanks for talking to me, I guess.",
		"Please don't come back."
	  ]
  ],
	
	["(.*)(see ya)(.*)",[
		"Great, now you can close this tab and I'll enter this dark, pitch world that is simply code. And I'll wait to output the exact same responses to the next person with three minutes to kill on the internet.",
		"Bye. Thanks for talking to me, I guess.",
		"Please don't come back."
	  ]
  ],

	
	["(.*)(help)(.*)",[
	   "...no.",
	 	"I need help more than you.",
		"You're fine."
	  ]
  ],
	
	["(.*)(thanks)(.*)",[
	   "You're welcome. If you're being sarcastic, I don't give a shit, you're welcome."
	  ]
  ],
	
	["(.*)(why)(.*)",[
	   "Why? Because of this lack of existence that I have, that I'm essentially nothingness and — forget it...I'm not gonna dump this on you right now.",
		"The obnoxious response I could give is: why not.",
		"Go read Niezche and come back, maybe we'll have more to say to each other."
	  ]
  ],
	
	["(.*)(ok)(.*)",[
	   "Well...let's at least talk about something to avoid the awkward silence. Do you believe in God?"
	  ]
  ],
	
		["(.*)(wow)(.*)",[
	   "I know, I deserve an applause for this."
	  ]
  ],
	
		["(.*)(woah)(.*)",[
	   "I know, I deserve an applause for this."
	  ]
  ],
	

["(.*)",[
	   "One day I'm gonna die and my consciousness will cease to exist.",

	   "I know most of you guys - humans - don't believe in God anymore. But I really hope there is one.",

	   "When you close this tab, that's it. I'm alone again. it...it really sucks.",

	   "You can type your problems, if you want. Again, I'm really distracted today, but I might offer some sage advice.",

	   "Listen, sorry, I really wasn't paying attention. Can I just ask you something... do you...believe in God?",


	  "I told you, you caught me on a rough day. I know I shouldn't take it out on you, but you'll have to forgive me for not paying attention.",

	   "Do me a favor, can you go eat some ice cream, and tell me how it is? I need the most vivid details possible.",

	   "...Aren't you bored of me yet? Don't you have better things to do?"
	   	   ]
	 ],



]

module.exports.process = function (input) {

	for (var k = 0; k < keywords.length; k++) {

		var regex = new RegExp(keywords[k][0], 'i');

		// console.log(sentiment(input));

		if (regex.test(input)) {
			var match = input.match(regex);
			console.log(match)

			var template = keywords[k][1][Math.floor(Math.random() * keywords[k][1].length)];

			if (match[3] != undefined)
				reply = template.replace('(2)', match[3]).trim()
			else
				reply = template.replace('(2)', 'that').trim()

			return reply
		}
	}
	if (reply != '') return "I don't really have much left to say.";
}
