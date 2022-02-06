const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const {spawn} = require('child_process');

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
	
}

exports.app = app

if (require.main === module) {
	app.listen(80)
}