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

    document.querySelectorAll(".element_button").forEach(button => {
        button.addEventListener("click", function () {
            const player_element = this.dataset.element;
            console.log("Element Button Clicked: " + player_element);

            document.getElementById("tie").style.display = "none";
            document.getElementById("element_animal").style.display = "block";
            document.getElementById("element_animal_one").style.display = "block";

            getComboAnimal(player_action, player_element, computer_action);
        });
    });
    document.querySelectorAll(".continue_one").forEach(button => {
        button.addEventListener("click", function () {
            document.getElementById("element_animal_one").style.display = "none";
            document.getElementById("element_animal_two").style.display = "block";
        });
    });
    document.querySelectorAll(".continue_two").forEach(button => {
        button.addEventListener("click", function () {
            document.getElementById("element_animal_two").style.display = "none";
            document.getElementById("element_animal_three").style.display = "block";

            getComboAnimal(computer_action, null, player_action);
        });
    });
    document.querySelectorAll(".continue_three").forEach(button => {
        button.addEventListener("click", function () {
            document.getElementById("element_animal_three").style.display = "none";
            document.getElementById("element_animal_four").style.display = "block";
        });
    });
    document.querySelectorAll(".continue_four").forEach(button => {
        button.addEventListener("click", function () {
            document.getElementById("element_animal_four").style.display = "none";
            document.getElementById("element_animal_five").style.display = "block";
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

        document.getElementById("player_choice_img").src = `/static/img/animals/${player_action} fighting.jpg`;
        document.getElementById("player_choice_img").alt= `an angry ${player_action} that's ready to fight`;

        document.getElementById("computer_choice_img").src = `/static/img/animals/${computer_action} fighting.jpg`;
        document.getElementById("computer_choice_img").alt= `an angry ${computer_action} that's ready to fight`;
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

function getComboAnimal(animal, element = null, computer_animal = null) {
    fetch("/get_combo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            animal: animal, 
            element: element, 
            computer_animal: computer_animal })
    })
    .then(response => response.json())
    .then(data => {
        const player_combo = data.player_combo_name;
        const computer_combo = data.computer_combo_name;

        const message = `It's ${player_combo} vs ${computer_combo}!!`;
        document.getElementById("combo_message").textContent = message;

        document.getElementById("player_combo_img").src = `/static/img/animals/${player_combo} fighting.jpg`;
        document.getElementById("player_combo_img").alt= `an angry ${player_combo} that's ready to fight`;

        document.getElementById("computer_combo_img").src = `/static/img/animals/${computer_combo} fighting.jpg`;
        document.getElementById("computer_combo_img").alt= `an angry ${computer_combo} that's ready to fight`;

        document.getElementById("computer_combo_img").classList.add("flip"); 
    })
    .catch(error => console.error(`Error getting ${owner} combo:`, error));
}