const lights = document.querySelectorAll(".headlight span");
const strip = document.querySelector(".led-strip");

let on = true;

document.getElementById("toggleLights").onclick = () => {

    on = !on;

    lights.forEach(light=>{
        light.style.opacity = on ? "1" : "0.2";
        light.style.boxShadow = on
        ? "0 0 12px white,0 0 30px white"
        : "none";
    });

    strip.style.opacity = on ? "1" : "0.2";

};