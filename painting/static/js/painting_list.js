async function like_pain(id) {
    let icon  = document.querySelector(`.icon_like${id}`);
    icon.classList.toggle('active_like');
    console.log(id)
    if(icon.classList.contains('active_like')) {
        await fetch(`http://localhost:8000/painting/like/${id}/`) 
        .then((res) => {
            console.log(res)
        })
        .catch((err) => {
            console.log(err)
        })
    }
    else {
        await fetch(`http://localhost:8000/painting/like_delete/${id}/`) 
        .then((res) => {
            console.log(res)
        })
        .catch((err) => {
            console.log(err)
        })
    }    
    
}

function likeNoUser() {
    const res = confirm('Vui lòng đăng nhập để tiếp tục');
    if(res) {
        location.href = "http://localhost:8000/painting/loginPage/"
    }
}