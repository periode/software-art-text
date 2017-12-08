var express = require('express')
var eliza = require('./eliza.js')
var bp = require('body-parser')
var port = 2046;
var jade = require('jade')
var app = express();

//this we need because i'm doing post requests
app.use(bp.urlencoded({
  extended: true
}));
app.use(bp.json());
app.set('view engine', 'jade')
app.set('views', './templates')

app.listen(port, function(){
  console.log('listening on', port);
});

app.get('/', function(req, res, err){
  res.render('./reine-bot.jade')
});


app.post('/discuss', function(req, res, err){
  console.log('human said:',req.body.words);
  var answer = eliza.process(req.body.words)
  res.send(answer);
});