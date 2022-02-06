const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const {spawn} = require('child_process');

recording = false;
var pythonRec

score = 0;
saveText = "";

app.use(bodyParser.json());

app.set('views', __dirname + "/views")
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	console.log("loaded")
	res.render('bchacks-front', { score })
})

app.post('/calc', (req, res) => {
	saveText = req.body.text;
	var pyOut;
	const python = spawn('python', ['posScore.py', req.body.text]);
	python.stdout.on('data', function (data){
		pyOut = JSON.parse(data.toString())
	});
	python.on('exit', (code) => {
		score = pyOut.weightedScore
		console.log(pyOut)
		res.end()
	});
})

app.post('/rec', (req, res) => {
	recording = true;
	var pyOut;
	console.log("recording")
	pythonRec = spawn('python', ['real_time_speech.py']);
	pythonRec.stdout.on('data', function (data){
		pyOut += data.toString()
		recText = data.toString()
		console.log("line: "+data.toString())
	});
	pythonRec.on('exit', (code) => {
		recText = pyOut.substring(9)
		console.log("out: " + recText)
		saveText = recText;
		res.end()
	});
})

app.post('/stopRec', (req, res) => {
	if(recording){
		pythonRec.kill('SIGTERM');
		recording = false;
		console.log("Killed");
	}
});

exports.app = app

if (require.main === module) {
	app.listen(80)
}