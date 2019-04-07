var title = location.href.split('/')[3];
document.getElementById('note_name').innerHTML = title; 
console.log(title);

function save(){
    console.log("Save");
    data = {
        note: document.getElementById('notearea').value,
        name: title,
    }
    var url = 'save_note/';
    $.get(url, data, function(data, status){
        console.log(`Status : ${status}`);
    })
}

function share(){
    console.log("Share");
}

$('.fixed-action-btn').floatingActionButton();
