// linear-clock.js
const readline = require("readline");

function linearClock() {
  setInterval(() => {
    const now = new Date();

    let hours = now.getHours().toString().padStart(2, "0");
    let minutes = now.getMinutes().toString().padStart(2, "0");
    let seconds = now.getSeconds().toString().padStart(2, "0");

    // Clear console
    process.stdout.write("\x1Bc");

    // Linear clock display
    console.log("LINEAR CLOCK");
    console.log("-----------------------");
    console.log(`${hours} : ${minutes} : ${seconds}`);
    console.log("-----------------------");
  }, 1000);
}

linearClock();