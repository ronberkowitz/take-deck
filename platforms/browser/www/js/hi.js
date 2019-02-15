$(document).ready(function(){
    var socket = io.connect('http://' + '127.0.0.1' + ':' + '5000' + '/test');
    console.log(socket)
    socket.on('my response', function(msg) {
        $('#log').append('<p>Received: ' + msg.data + '</p>');
        console.log('hewheohewiohwgoehwi')
        console.log(msg);
    });

    socket.on('message', function(msg){
        console.log('recieved the following message ! :' + msg)
    })

    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
});