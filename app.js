const express = require('express');
const mongoose = require('mongoose');

const dotenv = require('dotenv').config();

const db = `mongodb+srv://${process.env.DB_USERNAME}:${process.env.DB_PASSWORD}`
+ `@cluster0.udsmc.mongodb.net/${process.env.DB_NAME}?retryWrites=true&w=majority`;

console.log(db);

mongoose.connect(db, { useNewUrlParser : true, useUnifiedTopology: true });

const app = express();

const router = require('./routes/routes');

app.use(express.static('static'))

app.set('view engine', 'ejs');
app.set('views', 'views');

app.use('/', router);

module.exports = app;