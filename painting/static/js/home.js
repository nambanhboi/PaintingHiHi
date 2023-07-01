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

// const manager_admin = document.querySelector('.icon-user-home')
// const manager_pictures = document.querySelector('.man-pictures')

// const isShow = false;
// manager_admin.addEventListener('click',function (){
//     this.isShow = !this.isShow;
//     if(this.isShow == true){
//         document.querySelector('.manager-admin').style.display = 'block';
//     }
//     else {
//         document.querySelector('.manager-admin').style.display = 'none';
//         document.querySelector('.manager-pictures').style.display = 'none'; 
//     }
// });

// manager_pictures.addEventListener('click',function (){
//   this.isShow = !this.isShow;
//   if(this.isShow == true){
//       document.querySelector('.manager-pictures').style.display = 'block';
//       document.querySelector('.manager-admin').style.display = 'none';
//   }
//   else {
//       document.querySelector('.manager-pictures').style.display = 'none';
//   }
// });

let plus_btn = document.querySelector(".plus_btn");
let user_btn = document.querySelector(".user_button");
let isShow1 = false;
let isShow2 = false;


plus_btn.addEventListener('click', function () {
  console.log('running...')
  this.isShow2 = !this.isShow2;

  if(this.isShow2 == true){
    document.querySelector('.login_btn').style.display = "block";
    document.querySelector('.logout_btn').style.display = "none";
  }
  else {
    document.querySelector('.login_btn').style.display = "none";
  }
})

user_btn.addEventListener('click', function () {
  console.log('running...')
  this.isShow1 = !this.isShow1;

  if(this.isShow1 == true){
    document.querySelector('.logout_btn').style.display = "block";
    document.querySelector('.login_btn').style.display = "none";
  }
  else {
    document.querySelector('.logout_btn').style.display = "none";
  }
})

  
