const canvas = document.getElementById("tachoCanvas");
const ctx = canvas.getContext("2d");
let speed = 0
let rpm = 0

// Draw the tachometer
function drawTachometer(speed, rpm) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Base arc
    ctx.beginPath();
    ctx.arc(200, 200, 180, 0.75 * Math.PI, 0.25 * Math.PI, false);
    ctx.strokeStyle = "#0078d7";
    ctx.lineWidth = 10;
    ctx.stroke();

    // Speed scale
    ctx.font = "16px Arial";
    ctx.fillStyle = "#333";
    for (let i = 0; i <= 220; i += 20) {
        let angle = (Math.PI * 0.75) + (i / 220) * (Math.PI * 1.5);
        let x = 200 + Math.cos(angle) * 160;
        let y = 200 + Math.sin(angle) * 160;
        ctx.fillText(i, x - 10, y + 5);
    }

    // Speed pointer
    ctx.beginPath();
    let speedAngle = (Math.PI * 0.75) + (speed / 220) * (Math.PI * 1.5);
    ctx.moveTo(200, 200);
    ctx.lineTo(
        200 + Math.cos(speedAngle) * 150,
        200 + Math.sin(speedAngle) * 150
    );
    ctx.strokeStyle = "red";
    ctx.lineWidth = 5;
    ctx.stroke();

    // Display RPM and speed
    ctx.font = "20px Arial";
    ctx.fillStyle = "black";
    ctx.fillText(`Drehzahl: ${rpm} RPM`, 130, 350);
    ctx.fillText(`Geschwindigkeit: ${speed} km/h`, 100, 380);
}

// Generate a random speed and RPM every second
function startInfiniteRandomUpdate() {
    setInterval(() => {
        let randomSpeed = 0
        if (speed >= 220) {
            randomSpeed = speed -= 1;
        } else if (speed >= 0) {
            randomSpeed = speed += 1;
        }
        let randomRPM = rpm += 100
        drawTachometer(randomSpeed, randomRPM);
    }, 10); // Update every 1 second
}

// Start the infinite random updates
startInfiniteRandomUpdate();
