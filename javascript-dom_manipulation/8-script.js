document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    const helloElement = document.getElementById('hello');

    fetch (url)
    .then(response => response.json())
    .then(data => {
        helloElement.textContent = data.hello;
    })
    .catch(error => {
        console.error('Error fetching hello:', error);
    });
});