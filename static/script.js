function makeGuess() {
    const guessInput = document.getElementById('guess-input').value;
    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `guess=${guessInput}`,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.response;
    })
    .catch(error => console.error('Error:', error));
}
