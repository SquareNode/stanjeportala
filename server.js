const http = require('http');

const app = require('./app');

const port = 8080;
const server = http.createServer(app);

server.listen(process.env.PORT || port);
server.once('listening', function () {
	console.log('listening on port', process.env.PORT || port);
});