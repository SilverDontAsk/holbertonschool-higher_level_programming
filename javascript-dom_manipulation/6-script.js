const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch (url)
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response .json();
})
.then(data => {
    const charName = data.name;
    document.getElementById('character').textContent = charName;
})
.catch(error => {
    document.getElementById('character').textContent = 'Failed to load character name';
    console.error('There was a problem with the fetch operation:', error);
});