let animal = null;
let element = null;

//All Button Clicks
document.addEventListener("DOMContentLoaded", function () {
    const starting_grounds = document.getElementById("start");
    const confirm_close = document.querySelector(".confirm_close");
    const outcome_window = document.getElementById("outcome");

    document.querySelectorAll(".animal_button").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Animal Button Clicked: " + this.dataset.animal);
            sendDataToBackend(this.dataset.animal);
            starting_grounds.style.display = "none";
            document.getElementById("animal_chosen").style.display = "block";
        });
    });

    document.querySelectorAll(".lets_go").forEach(button => {
        button.addEventListener("click", function () {
            console.log("Fight Initiated!");
            document.getElementById("animal_chosen").style.display = "none";
            outcome_window.style.display = "block";
            
            sendOutcomeToBackend();
        });
    });

    document.querySelectorAll(".element_button").forEach(button => {
        button.addEventListener("click", function () {
            element = this.dataset.element;
            
            console.log("Element Button Clicked: " + element);

            getComboAnimalandOutcome(animal, element);

            document.getElementById("tie").style.display = "none";
            document.getElementById("element_animal").style.display = "block";
            document.getElementById("element_animal_one").style.display = "block";
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

            getComboAnimalandOutcome(animal, element);
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
    document.querySelectorAll(".element_outcome_button").forEach(button => {
        button.addEventListener("click", function () {
            document.getElementById("element_animal_five").style.display = "none";
            document.getElementById("element_outcome").style.display = "block";
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
let player_combo, computer_combo

function sendDataToBackend(selectedAnimal) {
    animal = selectedAnimal;

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

        document.getElementById("player_choice_img").src = `/static/img/animals/${player_action} fighting.png`;
        document.getElementById("player_choice_img").alt= `an angry ${player_action} that's ready to fight`;

        document.getElementById("computer_choice_img").src = `/static/img/animals/${computer_action} fighting.png`;
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

function getComboAnimalandOutcome(selectedAnimal, selectedElement) {
    animal = selectedAnimal;
    element = selectedElement;

    console.log("Sending combo request:", { animal, element });

    fetch("/get_combos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ animal, element })
    })
    .then(response => response.json())
    .then(data => {
        const player_combo = data.player_combo;
        const computer_combo = data.computer_combo;
        let article
        if (["a", "e", "i", "o", "u"].includes(Array.from(player_combo)[0].toLowerCase())) {
            article = "an "
        }
        else {
            article = "a "
        }

        //"You've turned into..."
        const player_combo_message = `${article}${player_combo}!!`;
        document.getElementById("player_combo_text").textContent = player_combo_message;

        document.getElementById("player_combo_img").src = `/static/img/element_combos/${player_combo}.png`;
        document.getElementById("player_combo_img").alt= `$${article}{player_combo}`;

        console.log(`You've become ${article}${player_combo}!!`);

        //"And your opponent has turned into..." display
        const computer_combo_message = `${article}${computer_combo}!!`;
        document.getElementById("computer_combo_text").textContent = computer_combo_message;

        document.getElementById("computer_combo_img").src = `/static/img/element_combos/${computer_combo}.png`;
        document.getElementById("computer_combo_img").alt= `${article}${computer_combo}`;
        console.log(`And your opponent has become ${article}${computer_combo}!!`);
        
        //"vs" display
        const message = `It's ${player_combo} vs ${computer_combo}!!`;
        document.getElementById("combo_message").textContent = message;

        document.getElementById("fighting_player_combo_img").src = `/static/img/element_combos/${player_combo} fighting.png`;
        document.getElementById("fighting_player_combo_img").alt= `${player_combo} that's angry and ready to fight`;

        document.getElementById("fighting_computer_combo_img").src = `/static/img/element_combos/${computer_combo} fighting.png`;
        document.getElementById("fighting_computer_combo_img").alt= `${computer_combo} that's angry and ready to fight`;
        console.log(`It's ${data.player_combo} vs ${data.computer_combo}!!`);

        document.getElementById("fighting_computer_combo_img").classList.add("flip");
        
        //outcome display
        const outcome_message = data.description;
        const result = data.result;

        if (result === "tie") {
            document.getElementById("").style.display = "none";
            document.getElementById("").style.display = "none";
            document.getElementById("second_tie").style.display = "block";
            return;
        }

        document.getElementById("element_outcome_dialogue").textContent = outcome_message;
        console.log("Message:", outcome_message);
        console.log("Result", result);

        if (element == "earth") {
            if (data.computer_element == "earth") {
                document.getElementById("element_outcome_image").src = "/static/img/outcomes/human_vs_human.png";
            }
            else {
                if (result == "win") {
                    document.getElementById("element_outcome_image").src = `/static/img/animals/bee.png`;
                }
                else if (result == "lose") {
                    document.getElementById("element_outcome_image").src = `/static/img/animals/bun.png`;
                }
                else {
                    console.log("Something isn't right.")
                }
            }
        }
        else {
            if (data.computer_element == "earth") {
                if (result == "win") {
                    document.getElementById("element_outcome_image").src = `/static/img/animals/cat.png`;
                }
                else if (result == "lose") {
                    document.getElementById("element_outcome_image").src = `/static/img/animals/corvid.png`;
                }
                else {
                    console.log("Something isn't right.")
                }                
            }
            else {
                document.getElementById("element_outcome_image").src = `/static/img/animals/wolf.png`;
            }
        };
        
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