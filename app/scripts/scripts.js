const changingText = document.getElementById('changingText');
const words = ['importante', 'una amiga', 'tu día a día'];
let currentWordIndex = 0;

function changeWord() {
  currentWordIndex = (currentWordIndex + 1) % words.length;
  changingText.textContent = words[currentWordIndex];
}

function changeColor() {
  changingText.style.color = 'red';
  setTimeout(() => {
    changingText.style.color = '';
  }, 1000);
}

setInterval(changeWord, 300);
setInterval(changeColor, 500);
