
document.body.addEventListener('click', function(event) {
    if (event.target.tagName === 'BUTTON') {
        const animal = event.target.dataset.animal;
        console.log("You've clicked the ${animal}!");
        fetch('/animal_click', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ animal: animal }),
        });
    }
});

