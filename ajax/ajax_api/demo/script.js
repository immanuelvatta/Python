console.log("this is connected");



const pokeBtn = document.querySelector("#poke-btn");
pokeBtn.addEventListener('click', function(){
    getPoke("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
})

// pokeBtn.addEventListener("click", function(){
    
//     fetch("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
//         .then(response => response.json() )
//         .then(coderData => {
//         let pokeShow = document.querySelector('#poke-show')
        
//         let ul = document.createElement('ul')

//         let pokeList = coderData.results
//         pokeList.forEach(poke => {
//             console.log(poke)
//             let li = document.createElement('li')
//             li.innerText = poke.name
//             ul.appendChild(li)
//         });
        
//         pokeShow.appendChild(ul)


//         console.log(coderData) })
//         .catch(err => console.log(err) )
// })

async function getPoke (url){
    let resp = await fetch(url)
    let data = await resp.json()

    console.log((data));

}

const pokeSearchBtn = document.querySelector("#poke-search-btn")

pokeSearchBtn.addEventListener('click', function(){
    const pokeNameEl = document.querySelector("#poke-name")
    // console.log(pokeNameEl.value);
    const pokeName = pokeNameEl.value
    let url = `https://pokeapi.co/api/v2/pokemon/${pokeName}`
    fetch(url)
    .then(resp => resp.json())
    .then(data => {
        let onePokeShow = document.querySelector("#one-poke-show")
        let img = data.sprites.front_default
        console.log(img);

        let listContent = ""

        data.

        onePokeShow.innerHTML= `
            <h2>${data.name}</h2>
            <img src="${img}" alt="poke-image">
            <p>Abilities</p>
            <ul>
            <li></li>
            </ul>
        `
        console.log(data);
    })
    .catch (err => console.log(err))
})