var request = window.superagent;

function sendOverride(index) {
    request.post('/api/override/')
        .type('form')
        .send({ override: index })
        .end(() => { console.log(index) });
}

document.addEventListener('DOMContentLoaded', () => {
    let cont = document.getElementById("control");
    console.log(cont);
    classes = ['dummy', 'smol', 'smol', 'smoler', 'smoler', 'smoler', 'dummy'];
    text = ['CALLING', 'MOTIVATION', 'CRISIS', 'SUPPORT', 'STASIS', 'DECLINE', 'RING RING']

    for (let i = 0; i < classes.length; ++i) {
        let button = document.createElement("button");
        button.textContent = text[i];
        button.classList.add(classes[i]);
        button.addEventListener('click', () => {
            sendOverride(i);
        });
        cont.appendChild(button);
    }
}, false);