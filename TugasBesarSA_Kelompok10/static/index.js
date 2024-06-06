
function generateMatrixInputs(idPrefix, rows, containerId) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';

    for (let i = 0; i < rows; i++) {
        let row = document.createElement('div');
        for (let j = 0; j < rows; j++) {
            let input = document.createElement('input');
            input.type = 'text';
            input.name = `${idPrefix}_${i}_${j}`;
            input.required = true;
            input.classList.add('matrix-input');
            row.appendChild(input);
        }
        container.appendChild(row);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const initialRows = document.getElementById('activities-count').textContent;
    generateMatrixInputs('matrix', initialRows, 'matrix-container');
});

// Fungsi untuk menambahkan kegiatan baru ke dalam daftar
function addActivity() {
    document.getElementById("add-activity-btn").classList.add("d-none");

    var activitiesList = document.getElementById("activities-list");
    var activityInput = document.createElement("input");
    activityInput.type = "text";
    activityInput.placeholder = "Masukkan nama kegiatan";
    activityInput.className = "form-control mb-2 flex-grow-1 me-4";

    var addButton = document.createElement("button");
    addButton.textContent = "Tambah";
    addButton.className = "btn btn-primary mb-2";
    addButton.onclick = function () {
        var activityName = activityInput.value.trim();
        if (activityName !== "") {
            var activityNumber = activitiesList.childElementCount + 1; // Nomor kegiatan
            var activityItem = document.createElement("li");
            activityItem.textContent = String.fromCharCode(activityNumber + 63) + " : " + activityName; // Menambahkan nomor kegiatan ke nama kegiatan
            activitiesList.appendChild(activityItem);
            updateActivitiesCount(); // Memperbarui jumlah kegiatan
            generateMatrixInputs('matrix', activitiesList.childElementCount - 1, 'matrix-container');
            activityInput.value = ""; // Mengosongkan input setelah ditambahkan
        } else {
            alert("Invalid input!");
        }
    };


    var activityItem = document.createElement("div");
    activityItem.className = "d-flex align-items-center";
    activityItem.appendChild(activityInput);
    activityItem.appendChild(addButton);
    activitiesList.appendChild(activityItem);
}

// Fungsi untuk memperbarui nilai dalam elemen <span> jumlah kegiatan
function updateActivitiesCount() {
    var activitiesCount = document.getElementById("activities-count");
    var activitiesList = document.getElementById("activities-list").getElementsByTagName("li");
    activitiesCount.textContent = activitiesList.length;
    document.getElementById("activities-count-input").value = activitiesList.length;
}

// Menambahkan event listener untuk tombol "Tambah Kegiatan"
document.getElementById("add-activity-btn").addEventListener("click", addActivity);


