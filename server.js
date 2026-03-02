import { createServer } from 'http'

const server = createServer((req, res) => {
    console.log("request recieved")
    res.writeHead(200, { "Content-type": "text/plain" })
    res.end("Hello")
})

server.listen(4000, () => {
    console.log("server running on port 3000")
})  