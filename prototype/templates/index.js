const visualisation = require('./include/visualisation.js');
const express = require('express');
const {spawn} = require('child_process');
const app = express();
const port = 3000;
app.get('/', (req, res) => {

    let dataToSend;
    // spawn new child process to call the python script
    const python = spawn('python', ['tree_test.py']);
    // collect data from script
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });
    // in close event we are sure that stream from child process is closed
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // send data to browser
        res.send(dataToSend)
    });

})

app.get('/', (req, res) => {
    res.status(200).json({ message: 'Enable CORS in Node.js - Clue Mediator' });
});

app.listen(port, () => console.log(`Example app listening on port 
${port}!`))