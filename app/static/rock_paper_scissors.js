document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".animal-button").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Button clicked: " + this.dataset.animal);
            sendDataToBackend(this.dataset.animal);
            document.getElementById("start").style.display = "none";
            document.getElementById("animal_chosen").style.display = "block";
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
    .then(data => {
        const message = `It's ${data.player} vs ${data.computer}!!`;
        document.getElementById("game-message").textContent = message;
        console.log(`It's ${data.player} vs ${data.computer}!!`)
    })
    .catch(error => console.error("Error:", error));
}

