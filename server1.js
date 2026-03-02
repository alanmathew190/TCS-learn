import { createServer } from "http"

const server = createServer((req,res) => {
    // console.log("Request Recieved")
    // res.writeHead(200, { "content-type": "text/plain" })
    console.log(req.method)
    console.log(req.url)
    res.end("Hello")

})
server.listen(3000, () => {
    console.log("Check localhost 3000")
})