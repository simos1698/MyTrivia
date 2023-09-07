function addToFavorites(questionId, category) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var url;    
    category=='home'?url='':url='/questions/' + category
    console.log(url)

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'question_id': questionId
        })
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to add question to favorites.');
            }
        })
}

function removeFromFavorites(questionId, category) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var url;    
    category=='home'?url='':url='/questions/' + category
    console.log(url)

    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'question_id': questionId
        })
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to remove question from favorites.');
            }
        })
}

function toggleFavorite(e, questionId, category) {
    console.log(questionId, category);
    e.parentElement.parentElement.classList.toggle("liked");
    if(e.parentElement.parentElement.classList.contains("liked"))
    {
        console.log("Favorite!");
        addToFavorites(questionId, category);
    }
    else {
        console.log("Unfavorite!");
        removeFromFavorites(questionId, category);
    }
    
}