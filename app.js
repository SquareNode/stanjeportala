const express = require('express');
const mongoose = require('mongoose');

const db = 'mongodb+srv://Dzoni:dzoni123@cluster0.udsmc.mongodb.net/test?retryWrites=true&w=majority';

mongoose.connect(db, { useNewUrlParser : true, useUnifiedTopology: true })
	.then(console.log('connected to DB!'))
	.catch((err) => console.log(err));

// mongoose.connection.on('open', function (ref) {
    // console.log('Connected to mongo server.');
    // trying to get collection names
    // mongoose.connection.db.listCollections().toArray(function (err, names) {
        // console.log(names); // [{ name: 'dbname.myCollection' }]
        // module.exports.Collection = names;
    // });
// })


const app = express();

const router = require('./routes/routes');

app.set('view engine', 'ejs');
app.set('views', 'views');

app.use('/', router);

module.exports = app;