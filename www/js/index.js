

const serverPort = 4378;
const serverIp = '127.0.0.1'

document.addEventListener('deviceready', function () {
    var config = {
        type: Phaser.WEBGL,
        parent: 'game',
        scene: {
            preload: preload,
            create: create
        }
    };

    var net = require('net');

    var client = new net.Socket();
    client.connect(serverPort, '127.0.0.1', function () {
        console.log('Connected');
        client.write('Hello, server! Love, Client.');
    });

    client.on('data', function (data) {
        console.log('Received: ' + data);
        client.destroy(); // kill client after server's response
    });

    var game = new Phaser.Game(config);

    function preload() {

    }

    function create() {
    }
});