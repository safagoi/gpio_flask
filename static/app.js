// Elemento 
const led = document.querySelector(".led");

async function on() {
    // console.log("led is on");
    await fetch("/on").then(res => {
        // console.log(res);
        if (res.status == 200) {
            led.classList.toggle("on");
        }
    });
}

async function off() {
    // console.log("led is off");
    await fetch("/off").then(res => {
        // console.log(res);
        if (res.status == 200) {
            led.classList.toggle("on");
        }
    });
}