const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    const movies = data.results;
    const listMovies = document.getElementById('list_movies');

    movies.foreach(movie => {
        const listItem = document.createElement('li');
        listItem.textcontent = movie.title;
        listMovies.appendChild(listItem);
    });
})
.catch(error => {
    const listMovies = document.getElementById('list_movies');
    listMovies.textContent = 'Failed to load movie titles';
    console.error('There was a problem with the fetch operation:', error);
});