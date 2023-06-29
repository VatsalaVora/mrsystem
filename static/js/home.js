var modal1 = document.getElementById('myModal');
var form1 = document.getElementById('getstart');
form1.onclick = function(){
    modal1.style.display = "block";
}
var span1b = document.getElementsByClassName("closeb")[0];
span1b.onclick = function() {
    modal1.style.display = "none";
}

document.querySelector('.img__btn').addEventListener('click', function() {
   document.querySelector('.cont').classList.toggle('s--signup');
});
