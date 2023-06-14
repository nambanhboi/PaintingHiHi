let index1 = 0;
const slides1 = document.getElementsByClassName('slide');
function Hien_thi_slide() {
  for (let i = 0; i < slides1.length; i++) {
    slides1[i].style.transform = `translateX(-${index1 * 100}%)`;
  }
}

function next() {
  if (index1 < slides1.length - 1) {
    index1++;
  } else {
    index1 = 0;
  }
  Hien_thi_slide();
}

function prev() {
  if (index1 > 0) {
    index1--;
  } else {
    index1 = slides1.length - 1;
  }
  Hien_thi_slide();
}

setInterval(next,3500);

Hien_thi_slide();

const manager_admin = document.querySelector('.icon-user-home')
const manager_pictures = document.querySelector('.man-pictures')

const isShow = false;
manager_admin.addEventListener('click',function (){
    this.isShow = !this.isShow;
    if(this.isShow == true){
        document.querySelector('.manager-admin').style.display = 'block';
    }
    else {
        document.querySelector('.manager-admin').style.display = 'none';
        document.querySelector('.manager-pictures').style.display = 'none'; 
    }
});

manager_pictures.addEventListener('click',function (){
  this.isShow = !this.isShow;
  if(this.isShow == true){
      document.querySelector('.manager-pictures').style.display = 'block';
      document.querySelector('.manager-admin').style.display = 'none';
  }
  else {
      document.querySelector('.manager-pictures').style.display = 'none';
  }
});