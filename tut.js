const http = require('http')
const fs = require('fs')

const text = fs.readFileSync('index.html', 'utf-8')

const server = http.createServer((req, res)=>{
    res.writeHead(200, {'Content-type':'text/html'});
    res.end(text)
})

server.listen(80, '127.0.0.1',()=>{
    console.log("listning")
})