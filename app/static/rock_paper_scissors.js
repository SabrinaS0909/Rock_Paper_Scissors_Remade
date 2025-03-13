document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".animal-button").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Button clicked: " + this.dataset.animal);
            sendDataToBackend(this.dataset.animal);
            document.getElementById("start").style.visibility = "hidden";
        });
    });
});

function sendDataToBackend(animal) {
    fetch("/animal_click", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ animal: animal })
    })
    .then(response => response.json())
    .then(data => console.log("Server response:", data))
    .catch(error => console.error("Error:", error));
}

