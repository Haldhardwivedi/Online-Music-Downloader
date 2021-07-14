const express = require('express');
const bodyParser = require("body-parser");
var  {PythonShell} = require('python-shell');
const path = require('path');

const app = express();
const port = process.env.PORT;


app.use(express.static(path.join(__dirname, 'public/css')));

app.use(bodyParser.urlencoded({
    extended:true
}));

app.get('/',function(req,res){
    res.sendFile(__dirname + "/index.html");
});

app.post('/', (req, res) => {
    let videolink=req.body.vlink;

    var options = {
      mode: 'text',
      pythonPath: '/usr/bin/python3', 
      pythonOptions: ['-u'],
      scriptPath: __dirname,
      args: [videolink]
    };

    PythonShell.run('script.py', options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results);
      res.download('./new.mp4');
      //res.sendFile(__dirname +"/downloaded.html");
    });
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))
