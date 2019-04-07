var socket = io.connect('http://' + document.domain + ':' + '5000');

counter = 0;
function change(){
    if(counter!=5){
        counter++;
        return;
    }
    counter = 0;
    var note = document.getElementById('notearea').value;
    console.log(note);
    var message = {
        note: note,
    }
    socket.emit('update', message);
}
socket.on( 'connect', function() {
    socket.emit( 'update', {
    data: 'User Connected'
    } )
} )
socket.on( 'response', function( msg ) {
    console.log( msg ,"Response");
    if(msg.hasOwnProperty('note')){
        console.log("Updating");
        document.getElementById('notearea').value = msg.note;
    }
})

$('.fixed-action-btn').floatingActionButton();

function open_new_tab(){
    var url=window.location.href;
    console.log(url);
    var win=window.open(url,'_blank');
    win.focus();
}

