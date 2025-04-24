//All Button Clicks
document.addEventListener("DOMContentLoaded", function () {
    var starting_grounds = document.getElementById("start");
    var confirm_close = document.querySelector(".confirm_close");
    var outcome_window = document.getElementById("outcome");

    document.querySelectorAll(".animal_button").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Button clicked: " + this.dataset.animal);
            sendDataToBackend(this.dataset.animal);
            starting_grounds.style.display = "none";
            document.getElementById("animal_chosen").style.display = "block";
        });
    });

    document.querySelectorAll(".lets_go").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Rando Button Clicked");
            document.getElementById("animal_chosen").style.display = "none";
            outcome_window.style.display = "block";
            
            sendOutcomeToBackend();
        });
    });

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
    };
    document.querySelectorAll(".confirmation").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Exited game successfully.")
            window.location.href = "404" //We will change this to the homepage once you get it on your website
        });
    });

    document.querySelectorAll(".replay").forEach(button => {
        button.addEventListener("click", function() {
            console.log("Restarting...");
            outcome_window.style.display = "none";
            starting_grounds.style.display = "block";
        })
    })
});

//All functions that send data to the backend
let player_action, computer_action

function sendDataToBackend(animal) {
    fetch("/animal_click", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ animal: animal })
    })
    .then(response => response.json())
    .then(data => {
        player_action = data.player;
        computer_action = data.computer;

        const message = `It's ${player_action} vs ${computer_action}!!`;
        document.getElementById("game_message").textContent = message;

        document.getElementById("player_choice_img").src = `/static/img/${player_action} fighting.jpg`;
        document.getElementById("player_choice_img").alt= `There should be an angry ${player_action} here.`;

        document.getElementById("computer_choice_img").src = `/static/img/${computer_action} fighting.jpg`;
        document.getElementById("computer_choice_img").alt= `There should be an angry ${computer_action} here.`;
        console.log(`It's ${data.player} vs ${data.computer}!!`);

        document.getElementById("computer_choice_img").classList.add("flip"); 
        
        sendOutcomeToBackend();
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

function sendOutcomeToBackend() {
    fetch("/outcome", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ player_action: player_action, computer_action: computer_action })
    })
    .then(response => response.json())
    .then( data => {
        const message = data.description;
        const result = data.result;

        if (result === "tie") {
            document.getElementById("outcome").style.display = "none";
            document.getElementById("animal_chosen").style.display = "none";
            document.getElementById("tie").style.display = "block";
            return;
        }

        document.getElementById("outcome_dialogue").textContent = message;
        console.log("Message:", message);
        console.log("Result", result);

        if (player_action == "human") {
            if (computer_action == "human") {
                document.getElementById("winner_image").src = "/static/img/outcomes/human_vs_human.png";
            }
            else {
                if (result == "win") {
                    document.getElementById("winner_image").src = `/static/img/outcomes/${player_action}_vs_${computer_action}_win.png`;
                }
                else if (result == "lose") {
                    document.getElementById("winner_image").src = `/static/img/outcomes/${player_action}_vs_${computer_action}_lose.png`;
                }
                else {
                    console.log("Something isn't right.")
                }
            }
        }
        else {
            if (computer_action == "human") {
                if (result == "win") {
                    document.getElementById("winner_image").src = `/static/img/outcomes/${player_action}_vs_${computer_action}_win.png`;
                }
                else if (result == "lose") {
                    document.getElementById("winner_image").src = `/static/img/outcomes/${player_action}_vs_${computer_action}_lose.png`;
                }
                else {
                    console.log("Something isn't right.")
                }                
            }
            else {
                document.getElementById("winner_image").src = `/static/img/outcomes/${player_action}_vs_${computer_action}.png`;
            }
        };
    })
    .catch(error => console.error("Error:", error));
}