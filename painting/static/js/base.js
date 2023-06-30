
let user_btn = document.querySelector(".user_button");
let isShow1 = false;
let isShow2 = false;

let plus_btn = document.querySelector(".plus-btn");

if(plus_btn) {
    plus_btn.addEventListener('click', function () {
      console.log('running...')
      this.isShow2 = !this.isShow2;
      this.isShow1 = false;
    
      if(this.isShow2 == true){
        document.querySelector('.login_btn').style.display = "block";
      }
      else {
        document.querySelector('.login_btn').style.display = "none";
      }
    })
}

user_btn.addEventListener('click', function () {
  console.log('running...')
  this.isShow1 = !this.isShow1;
  this.isShow2 = false;

  if(this.isShow1 == true){
    document.querySelector('.logout_btn').style.display = "block";
  }
  else {
    document.querySelector('.logout_btn').style.display = "none";
  }
})