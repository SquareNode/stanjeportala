const express = require('express');

const control = require('../control/controller');
const r = express.Router();

r.get('/', control.home);

module.exports = r;