var userName = "";
var cardDiv = document.querySelector("#cards");

function getUsername(element) {
    console.log(element.value);
    userName = element.value;
}

async function search() {
    var response = await fetch('https://api.github.com/users/' + userName);
    var userData = await response.json();
    cardDiv.innerHTML = makeCoderCard(userData) + cardDiv.innerHTML;
}

function makeCoderCard(data) {

    var response = `<div class="container mt-5 border border-light">
                        <img class="img-thumbnail mt-2" src="${data.avatar_url}" alt="${data.login}">
                        <div class="container mt-3 ">
                            <h3>${data.login} - ${data.name} </h3>
                            <p>Location: ${data.location}</p>
                            <p>Repositories: ${data.public_repos}</p>
                        </div>
                    </div>`;
    return response;
}