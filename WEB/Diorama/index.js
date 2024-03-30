
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("create").addEventListener("click", function(event) {
        let main = document.getElementById("main");
        main.innerHTML = "";

        let table = document.createElement("table");

        table.addEventListener("click", function(event) {
            const color = document.getElementById("color").value;
            console.log(color)
            let clickedElement = event.target;
            if (clickedElement.classList.contains("pixel")) {
                if (clickedElement.style.backgroundColor !== "") return clickedElement.style.backgroundColor = "";
                clickedElement.style.backgroundColor = color;
            }
        });
        
        main.appendChild(table)
        const amount = document.getElementById("amount").value;
    
        for (x=0; x<amount; x++){
            let row = document.createElement("tr");
            table.appendChild(row);
            for (y=0; y<amount; y++) {
                let cell = document.createElement("td");
                cell.id = y;
                cell.classList.add("pixel");
                row.appendChild(cell);
            }
        }
    });
});
