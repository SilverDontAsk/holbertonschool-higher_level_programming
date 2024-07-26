document.getElementById('add_item').addEventListener('click', function() {

    const nItem = document.createElement('li');
    nItem.textContent = 'Item'

    const list = document.querySelector('ul.my_list');
    list.appendChild(nItem);
});