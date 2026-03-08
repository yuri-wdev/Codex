const btnBooks = document.getElementById('btn-books');
const btnLendings = document.getElementById('btn-lendings');
const sectionBooks = document.getElementById('section-books');
const sectionLendings = document.getElementById('section-lendings');

btnBooks.onclick = () => {
    btnBooks.classList.add('active');
    btnLendings.classList.remove('active');
    sectionBooks.style.display = 'block';
    sectionLendings.style.display = 'none';
};

btnLendings.onclick = () => {
    btnLendings.classList.add('active');
    btnBooks.classList.remove('active');
    sectionLendings.style.display = 'block';
    sectionBooks.style.display = 'none';
};