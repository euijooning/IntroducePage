$(document).ready(function () {
    fristSet();
});

function fristSet() {
    $.ajax({
        type: 'GET',
        url: '/introduceData',
        data: {},
        success: function (response) {
            let rows = response['introduceDatas']
            for (let i = 0; i < rows.length; i++) {
                let img_url = rows[i]['img_url']
                let text_title = rows[i]['text_title']
                let text = rows[i]['text']


                let temp_html = `<div class="cards">
                                        <img src="${img_url}" class="card-img-top">
                                        <div class="mycard_text">
                                        <h2 class="card-title">${text_title}</h2>
                                        <p class="card-text">${text}</p>
                                        <button  onclick="post_delete('${text_title}')" class="btn btn-outline-danger">삭제</button>
                                        </div>
                                        </div>`

                $('#cards-box').append(temp_html)
            }

            console.log(response['introduceDatas'])
        }
    })
}

function posting() {
    let url = $('#url').val()
    let comment_title = $('#comment_title').val()
    let comment = $('#comment').val()
    $.ajax({
        type: 'POST',
        url: '/introduceData',
        data: {img_url_give: url, text_title_give: comment_title, text_give: comment},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}

function post_delete(text_title) {
    $.ajax({
        type: 'DELETE',
        url: '/introduceData',
        data: {text_title_give: text_title},
        success: function (response) {
            alert(response['msg']);
            window.location.reload()
        }
    });
}

function open_box() {
    $('#add-box').show()
    $('#add-button').hide()
}

function close_box() {
    $('#add-box').hide()
    $('#add-button').show()
}