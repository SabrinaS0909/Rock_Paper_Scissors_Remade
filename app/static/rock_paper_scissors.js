//All Button Clicks
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".animal_button").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Button clicked: " + this.dataset.animal);
            sendDataToBackend(this.dataset.animal);
            document.getElementById("start").style.display = "none";
            document.getElementById("animal_chosen").style.display = "block";
        });
    });

    document.querySelectorAll(".lets_go").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Rando Button Clicked");
            document.getElementById("animal_chosen").style.display = "none";
            document.getElementById("outcome").style.display = "block";
        });
    });

    var confirm_close = document.querySelector(".confirm_close")
    document.querySelectorAll(".close_game").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Opened confirmation prompt.")
            confirm_close.style.display = "block";
        });
    });
    document.querySelectorAll(".close").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Closed confirmation prompt.");
            confirm_close.style.display = "none";
        });
    });
    window.onclick = function(event) {
        if (event.target == confirm_close) {
            confirm_close.style.display = "none";
            console.log("Closed confirmation prompt via clicking window.")
        }
    }
    document.querySelectorAll(".confirmation").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Exited game successfully.")
            window.location.href = "404" //We will change this to the homepage once you get it on your website
        });
    });
});

//All functions that send data to the backend
function sendDataToBackend(animal) {
    fetch("/animal_click", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ animal: animal })
    })
    .then(response => response.json())
    .then(data => {
        const message = `It's ${data.player} vs ${data.computer}!!`;
        document.getElementById("game_message").textContent = message;
        document.getElementById("player_choice_img").src = `/static/img/${data.player} fighting.jpg`;
        document.getElementById("computer_choice_img").src = `/static/img/${data.computer} fighting.jpg`;
        console.log(`It's ${data.player} vs ${data.computer}!!`)

        document.getElementById("computer_choice_img").classList.add("flip");

        sendRandomButtonToBackend();
    })
    .catch(error => console.error("Error:", error));
}

function sendRandomButtonToBackend() {
    fetch("/random_button", {
        method: "POST",
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        const message = data.random_button;
        document.getElementById("lets_go").textContent = message;
        console.log(message);
    })
    .catch(error => console.error("Error:", error));
}