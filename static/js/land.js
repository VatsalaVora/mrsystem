const topRatedLink = document.getElementById('toprated');
const topIndianLink = document.getElementById('topindian');
const recommendBtn = document.getElementById('recbtn');
const defaultDiv = document.getElementById('default');
const newDiv2 = document.getElementById('new-div2');
const newDiv3 = document.getElementById('new-div3');

topRatedLink.addEventListener('click', () => {
    defaultDiv.style.display = 'none';
    newDiv3.style.display = 'none';
	newDiv2.style.display = 'block';
});

topIndianLink.addEventListener('click', () => {
    defaultDiv.style.display = 'none';
    newDiv2.style.display = 'none';
	newDiv3.style.display = 'block';
});

recommendBtn.addEventListener('click', () => {
    defaultDiv.style.display = 'block';
    newDiv2.style.display = 'none';
	newDiv3.style.display = 'none';
});
