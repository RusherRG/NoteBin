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

function character_count(){
    var content = document.getElementById('notearea');
    // console.log(content.value.length);
    var nword = content.value.split(" "); //HAHA
    // console.log(nword);
    str="Characters: " + content.value.length + "<br>" + "Words: " + nword.length;
    document.getElementById("charcount").innerHTML= str;
}

$('.fixed-action-btn').floatingActionButton();
