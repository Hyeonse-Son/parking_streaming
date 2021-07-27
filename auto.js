let spawn = require('child_process').spawn;

auto();

function auto(mission_name, directory_name) {
    var auto = spawn('./auto.sh');

    auto.stdout.on('data', function(data) {
        console.log('stdout: ' + data);
    });

    auto.stderr.on('data', function(data) {
        console.log('stderr: ' + data);
    });

    auto.on('exit', function(code) {
        console.log('exit: ' + code);
    });

    auto.on('error', function(code) {
        console.log('error: ' + code);

        setTimeout(auto, 1000);
    });
}
