async function addComment(id) {
    let cmt  = document.getElementById('comment').value
    let data = {
        cmt
    }
    let username;
    const csrftoken = getCookie('csrftoken');
    await fetch(`http://localhost:8000/painting/add_comment/${id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data.res_data)
        username = data.res_data.username;
    })
    .catch((err) => {
        console.log(err)
    })
    const comment = document.getElementById('comment').value
    document.querySelector('.cmt_tam').innerHTML += `
            <div class="cmt-par">
                <img src="/static/image/logo.png" alt="" class="user-image">
                <div class="cmt-detail">
                    <h4>${username}</h4> 
                    <p>${comment}</p>
                </div>
                <i class="bi bi-three-dots-vertical"></i>
            </div>
            <div class="cmt-add">
                <span>Thích</span>
                <span>Trả lời</span>
                <span>5 giờ</span>
            </div>

    `

    document.getElementById('comment').value = ''
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function commentNoUser() {
    const res = confirm("Vui lòng đăng nhập để tiếp tục")
    if(res) {
        location.href = "http://localhost:8000/painting/loginPage/"
    }
}

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