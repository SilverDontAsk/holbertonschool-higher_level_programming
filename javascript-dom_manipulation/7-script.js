document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const listMovies = document.getElementById('list_movies');

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const films = data.results;
        films.forEach(film => {
            const li = document.createElement('li');
            li.textContent = film.title;
            listMovies.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error fetching movie titles:', error);
    });
});