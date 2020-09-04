const http = require('http');

const app = require('./app');

const port = 8080;
const server = http.createServer(app);

server.listen(port);
server.once('listening', function () {
	console.log('listening on port 8080');
});