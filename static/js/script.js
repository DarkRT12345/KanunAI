let currentLanguage = 'english';

// Language toggle
document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        currentLanguage = e.target.dataset.lang;
    });
});

// Ask button
document.getElementById('askBtn').addEventListener('click', askQuestion);

// Enter key on input
document.getElementById('questionInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        askQuestion();
    }
});

async function askQuestion() {
    const question = document.getElementById('questionInput').value.trim();

    if (!question) {
        showError('Please enter a question');
        return;
    }

    // Show loading state
    const resultsContainer = document.getElementById('results');
    const loading = document.getElementById('loading');
    const resultContent = document.getElementById('resultContent');
    const error = document.getElementById('error');

    resultsContainer.style.display = 'block';
    loading.style.display = 'flex';
    resultContent.style.display = 'none';
    error.style.display = 'none';

    try {
        const response = await fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: question,
                language: currentLanguage
            })
        });

        const data = await response.json();

        loading.style.display = 'none';

        if (data.success) {
            displayResults(data);
            resultContent.style.display = 'block';
        } else {
            showError(data.answer || 'An error occurred');
        }
    } catch (err) {
        loading.style.display = 'none';
        showError('Network error: ' + err.message);
    }
}

function displayResults(data) {
    document.getElementById('answerText').textContent = data.answer;
    document.getElementById('sectionNumber').textContent = data.section || '—';
    document.getElementById('citation').textContent = data.citation || '—';

    // Show Nepali text if available
    const nepaliSection = document.getElementById('nepaliText');
    if (data.nepali_text) {
        document.getElementById('nepaliContent').textContent = data.nepali_text;
        nepaliSection.style.display = 'block';
    } else {
        nepaliSection.style.display = 'none';
    }
}

function showError(message) {
    const resultsContainer = document.getElementById('results');
    const error = document.getElementById('error');
    const loading = document.getElementById('loading');
    const resultContent = document.getElementById('resultContent');

    resultsContainer.style.display = 'block';
    loading.style.display = 'none';
    resultContent.style.display = 'none';
    error.style.display = 'block';
    error.textContent = '❌ ' + message;
}
