document.addEventListener('DOMContentLoaded', function() {
    
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    document.querySelectorAll('.edit_button').forEach(item => {
        const id = item.dataset.id;
        item.addEventListener('click', () => edit(id));
    });
    document.querySelectorAll('.submit_button').forEach(item => {
        const id = item.dataset.id;
        item.style.display = 'none';
        item.addEventListener('click', () => submit(id));
    });

    document.querySelectorAll(`.likes_amount`).forEach(item => {
        const id = item.dataset.id;
        fetch(`/post/${id}`)
        .then(response => response.json())
        .then(get_post => {
            item.innerHTML = `${get_post["users_like"]}`;
        })
    });

    document.querySelectorAll(`.like_button`).forEach(item => {
        const id = item.dataset.id;
        const user = item.dataset.user;
        fetch(`/post/${id}`)
        .then(response => response.json())
        .then(get_post => {
            let like_list = get_post["input_like"];
            if (Object.values(get_post["input_like"]).includes(parseInt(user)) == false) {
                item.innerHTML = "Like";
                item.addEventListener('click', () => like(id, user, like_list, csrfToken));
            } else {
                item.innerHTML = "Unlike";
                item.addEventListener('click', () => unlike(id, user, like_list, csrfToken));
            }
        })
    });

});

function edit(id) {
    fetch(`/post/${id}`)
    .then(response => response.json())
    .then(get_post => {
        document.querySelector(`#post${id}`).innerHTML = 
        `<textarea rows="2" cols="80" name="comment" form="edit_comment">${get_post["post"]}</textarea>`;
        document.querySelector(`#edit${id}`).style.display = 'none';
        document.querySelector(`#submit${id}`).style.display = 'block';
    })
}

function submit(id) {
    const editedContent = document.querySelector(`#post${id}`).querySelector('textarea').value;
    document.querySelector(`#post${id}`).innerHTML = editedContent;
    fetch(`/post/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            post: editedContent
        })});
    document.querySelector(`#edit${id}`).style.display = 'block';
    document.querySelector(`#submit${id}`).style.display = 'none';
}

function like(id, user, like_list, csrfToken) {
    user = parseInt(user);
    like_list.push(user);
    const update_like = {
        input_like: like_list
    };
    fetch(`api/post/${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(update_like)
    })
    .then(response => response.json())
    .then(data => {
      // Handle successful response
      console.log('Updated data:', data);
    })
    var value = document.querySelector(`#likes_amount_${id}`).innerHTML;
    value = parseInt(value);
    ++value;
    document.querySelector(`#likes_amount_${id}`).innerHTML = `${value}`;
    document.querySelector(`#like_button_${id}`).innerHTML = "Unlike";
    document.querySelector(`#like_button_${id}`).removeEventListener('click', () => like(id, user, like_list, csrfToken));
    // Remove old listener
    var old_element = document.querySelector(`#like_button_${id}`);
    var new_element = old_element.cloneNode(true);
    old_element.parentNode.replaceChild(new_element, old_element);
    // Add new listener
    document.querySelector(`#like_button_${id}`).addEventListener('click', () => unlike(id, user, like_list, csrfToken));
}

function unlike(id, user, like_list, csrfToken) {
    user = parseInt(user);
    const index = like_list.indexOf(user);
    if (index > -1) {
        like_list.splice(index, 1);
      }
    const update_like = {
        input_like: like_list
    };
    fetch(`api/post/${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(update_like)
    })
    .then(response => response.json())
    .then(data => {
      // Handle successful response
      console.log('Updated data:', data);
    })
    var value = document.querySelector(`#likes_amount_${id}`).innerHTML;
    value = parseInt(value);
    --value;
    document.querySelector(`#likes_amount_${id}`).innerHTML = `${value}`;
    document.querySelector(`#like_button_${id}`).innerHTML = "Like";
    document.querySelector(`#like_button_${id}`).removeEventListener('click', () => unlike(id, user, like_list, csrfToken));
    // Remove old listener
    var old_element = document.querySelector(`#like_button_${id}`);
    var new_element = old_element.cloneNode(true);
    old_element.parentNode.replaceChild(new_element, old_element);
    // Add new listener
    document.querySelector(`#like_button_${id}`).addEventListener('click', () => like(id, user, like_list, csrfToken));
}