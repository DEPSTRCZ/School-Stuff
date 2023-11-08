
document.addEventListener('DOMContentLoaded', async function() {
    let speed = 1;
    let posX = 0;
    function updateViewportSize() {
        viewportWidth = window.innerWidth;
        viewportHeight = window.innerHeight;
    }
    
    updateViewportSize(); // Initialize viewport size
    window.addEventListener("resize", updateViewportSize);

    document.querySelector(".wheel1").style.animation = "spinner 10s linear infinite";
    document.querySelector(".wheel2").style.animation = "spinner 10s linear infinite";

    

    document.addEventListener('keydown', (event) => {
        const name = event.key;
        document.getElementById("speed").innerHTML = speed;
        document.getElementById("pos").innerHTML = posX;
        let car = document.querySelector(".car");
        car.style.opacity = 1;
        
        switch (name) {
            case "a":
                posX-=speed;
                break;
            case "d":
                posX+=speed;
                break;
            case "w":
                speed+=1;
                break;
            case "s":
                speed-=1;
                break;
            case "space":
                break;
        }
        console.log("bef", posX, viewportWidth)
        if (posX >= viewportWidth) {
            posX = -500;
            car.style.opacity = 0;
            
        } else if (posX < -500) {
            posX = viewportWidth;
            car.style.opacity = 0;
        } else car.style.opacity = 1;
        
        console.log("aft", posX, viewportWidth)
        console.log(viewportHeight, viewportWidth)
        car.style.transform = `translateX(${posX}px     `;
        
      }, false);
});
