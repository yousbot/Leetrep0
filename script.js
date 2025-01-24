const problemsPerPage = 20;
let currentPage = 1;
let allProblems = [];
let filteredProblems = [];

async function fetchProblems() {
    const response = await fetch('./problems_data.json');
    allProblems = await response.json();
    filteredProblems = allProblems;
    renderProblems();
}

function renderProblems() {
    const start = (currentPage - 1) * problemsPerPage;
    const end = start + problemsPerPage;
    const problemsToRender = filteredProblems.slice(start, end);

    const problemList = document.getElementById('problemList');
    problemList.innerHTML = '';

    problemsToRender.forEach(problem => {
        const listItem = document.createElement('li');
        const problemNumber = problem.title.split('.')[0].trim();
        listItem.innerHTML = `
            <span>${problem.title}</span>
            <span>${problem.difficulty}</span>
        `;
        listItem.addEventListener('click', () => {
            window.location.href = `./Problems/all_${problemNumber}.html`;
        });
        problemList.appendChild(listItem);
    });

    updatePagination();
}

function updatePagination() {
    const prevPageButton = document.getElementById('prevPage');
    const nextPageButton = document.getElementById('nextPage');

    prevPageButton.disabled = currentPage === 1;
    nextPageButton.disabled = currentPage * problemsPerPage >= filteredProblems.length;

    prevPageButton.onclick = () => {
        currentPage--;
        renderProblems();
    };

    nextPageButton.onclick = () => {
        currentPage++;
        renderProblems();
    };
}

document.getElementById('searchBar').addEventListener('input', event => {
    const searchTerm = event.target.value.toLowerCase();
    filteredProblems = allProblems.filter(problem => 
        problem.title.toLowerCase().includes(searchTerm)
    );

    if (!searchTerm) {
        filteredProblems = allProblems;
    }

    currentPage = 1;
    renderProblems();
});

document.getElementById('easyFilter').addEventListener('click', () => {
    filteredProblems = allProblems.filter(problem => problem.difficulty === 'Easy');
    currentPage = 1;
    renderProblems();
});

document.getElementById('mediumFilter').addEventListener('click', () => {
    filteredProblems = allProblems.filter(problem => problem.difficulty === 'Medium');
    currentPage = 1;
    renderProblems();
});

document.getElementById('hardFilter').addEventListener('click', () => {
    filteredProblems = allProblems.filter(problem => problem.difficulty === 'Hard');
    currentPage = 1;
    renderProblems();
});

fetchProblems();
