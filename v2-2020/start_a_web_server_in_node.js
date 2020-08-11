/* Start a simple web server in node.js */

// Import the http module, which has tools we need to send and receive things across the web
const http = require('http'); 

let requestListener = (request, response) => {
  response.writeHead(200, {'Content-Type': 'text/plain' }); // Write the response header indicating no errors (200) and that the data being sent is text
  response.write('Here is the text I will include in the response data, after the header \n');
  response.end();
};

const server = http.createServer(requestListener);
server.listen(3000); // assign the port to use to listen for requests