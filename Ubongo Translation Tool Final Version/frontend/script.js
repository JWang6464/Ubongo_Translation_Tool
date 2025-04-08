function translateText() {
    const text = document.getElementById('textInput').value;
    fetch('http://127.0.0.1:5000/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        const translationsDiv = document.getElementById('translations');
        if (data.error) {
            translationsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        } else {
            translationsDiv.innerHTML = `
                <p>Translation 1: ${data.translation1} (Formal)</p>
                <p>Translation 2: ${data.translation2} (Humorous)</p>
                <p>Translation 3: ${data.translation3} (Conversational)</p>
            `;
        }
    })
    .catch(error => {
        const translationsDiv = document.getElementById('translations');
        translationsDiv.innerHTML = `<p>An error occurred: ${error}</p>`;
    });
}
