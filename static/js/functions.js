// Abrir modales
var $ = jQuery.noConflict()

function abrirmodalcreate(url) {
    $('#crear').load(url, function () {
        $(this).modal('show');
    });
}

function abrirmodaledit(url) {
    $('#editar').load(url, function () {
        $(this).modal('show');
    });
}

function abrirmodaldetail(url) {
    $('#detail').load(url, function () {
        $(this).modal('show');
    });
}

function abrirmodaldelete(url) {
    $('#delete').load(url, function () {
        $(this).modal('show');
    });
}

// Filtrar instrumentos por nombre
function filterList() {
    const searchTerm = searchInput.value.toLowerCase();
    document.querySelectorAll('tbody tr').forEach(row => {
        const name = row.querySelector('td:nth-child(1)').textContent.toLowerCase();
        const nameMatch = name.includes(searchTerm);
        if (nameMatch) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

const searchInput = document.getElementById('searchInput');
searchInput.addEventListener('input', filterList);
