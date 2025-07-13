let currentMode = "normal";

document.getElementById("toggleMode").addEventListener("click", function () {
    currentMode = currentMode === "normal" ? "fraud" : "normal";
    this.textContent = `Currently: ${currentMode.charAt(0).toUpperCase() + currentMode.slice(1)}`;
});

document.getElementById('paymentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const amt = parseFloat(document.getElementById('amount').value);
    const resultBox = document.getElementById("result");

    fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ amt: amt, mode: currentMode })
    })
    .then(res => res.json())
    .then(data => {
        if (data.prediction === 1) {
            resultBox.innerHTML = `
                <p class="alert">⚠️ ALERT: Fraudulent transaction detected! Are you sure you want to continue?</p>
                <div class="button-group">
                    <button id="continue-btn">Continue Payment</button>
                    <button id="cancel-btn">Cancel Payment</button>
                </div>
            `;

            document.getElementById("continue-btn").addEventListener("click", () => {
                resultBox.innerHTML = `<p class="safe">✅ Payment Processed Despite Risk</p>`;
            });

            document.getElementById("cancel-btn").addEventListener("click", () => {
                resultBox.innerHTML = `<p class="cancelled">❌ Payment Cancelled</p>`;
            });
        } else {
            resultBox.innerHTML = `<p class="safe">✅ Payment successful. No fraud detected.</p>`;
        }
    })
    .catch(error => {
        console.error("Prediction error:", error);
        resultBox.textContent = "❌ Something went wrong. Please try again.";
        resultBox.style.color = "red";
    });
});
