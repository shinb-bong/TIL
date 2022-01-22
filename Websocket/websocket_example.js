const express = require('express');
const app = express();

app.use("/",function(req,res){
    res.sendFile(__dirname+'/index.html');

})

app.listen(8080);

const WebSocket = require('ws');
const socket = new WebSocket.Server({
    port:8081
});
// 웹소켓으로 유저 메세지를 받는법 
socket.on('connection',(ws,req)=>{

    ws.on('message',(msg)=>{
        console.log('유저가 보낸거: ' + msg);
        ws.send('Okay');
    })
});