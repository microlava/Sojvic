document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('uploadForm');
    const countdownElement = document.getElementById('countdown');
    const statusElement = document.getElementById('status');
    let countdownTimer;

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const fileInput = document.getElementById('fileInput');

        if (fileInput.files.length > 0) {
            console.log(`Name: ${name}, Email: ${email}, Password: ${password}`);
            // Send data to server via AJAX or other methods
            startCountdown();
        } else {
            alert("Please upload a file.");
        }
    });

    function startCountdown() {
        const endTime = Date.now() + 2 * 24 * 60 * 60 * 1000; // 2 days from now

        countdownTimer = setInterval(() => {
            const now = Date.now();
            const remaining = endTime - now;

            if (remaining <= 0) {
                clearInterval(countdownTimer);
                countdownElement.textContent = 'Countdown ended!';
                checkApprovalStatus();
                return;
            }

            const days = Math.floor(remaining / (24 * 60 * 60 * 1000));
            const hours = Math.floor((remaining % (24 * 60 * 60 * 1000)) / (60 * 60 * 1000));
            const minutes = Math.floor((remaining % (60 * 60 * 1000)) / (60 * 1000));
            const seconds = Math.floor((remaining % (60 * 1000)) / 1000);

            countdownElement.textContent = `Time remaining: ${days}d ${hours}h ${minutes}m ${seconds}s`;
        }, 1000);
    }

    function checkApprovalStatus() {
        // Simulate a backend check (replace with real backend call)
        setTimeout(() => {
            // You can replace this with actual logic to check the status from your backend
            const isApproved = Math.random() > 0.5; // Simulated approval
            if (isApproved) {
                statusElement.textContent = 'Status: Approved';
                statusElement.style.color = 'green';
            } else {
                statusElement.textContent = 'Status: Pending';
                statusElement.style.color = 'orange';
            }
        }, 2000); // Simulate delay
    }
});