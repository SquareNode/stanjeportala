const express = require('express');
const mongoose = require('mongoose');

const db = 'mongodb+srv://Dzoni:dzoni123@cluster0.udsmc.mongodb.net/test?retryWrites=true&w=majority';

mongoose.connect(db, { useNewUrlParser : true, useUnifiedTopology: true });

const app = express();

const router = require('./routes/routes');

app.use(express.static('static'))

app.set('view engine', 'ejs');
app.set('views', 'views');

app.use('/', router);

module.exports = app;