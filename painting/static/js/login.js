const displayLogin = document.querySelector('.hd-sign');
const displayLogout = document.querySelector('.hd-sign-loggedIn');
if (isLoggedIn) {
    // Người dùng đã đăng nhập
    // Thực hiện các hành động khi đã đăng nhập
    displayLogin.style.display = "none";
  }
else{
    displayLogout.style.display = "none";
}