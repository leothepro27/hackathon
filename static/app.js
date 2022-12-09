async function myFunction(answer, answer2, answer3, answer4, answer5, answer6) {
    let response = await fetch('/results?q=' + answer + '&p=' + answer2 + '&k=' + answer3 + '&e=' + answer4 + '&g=' + answer5 + '&o=' + answer6);
    let resultss = await response.json()
    let length = resultss.length

    if (length == 0) {
        document.getElementById("note").style.display="block"
        document.getElementById("table1").style.display="none"
        document.getElementById("table2").style.display="none"
        document.getElementById("info").style.display="none"
        return 1;
    }
    else {
        document.getElementById("table1").style.display="block"
        document.getElementById("table2").style.display="block"
        document.getElementById("note").style.display="none"
        document.getElementById("info").style.display="block"
    }

    let tem = Array.from(resultss)[0]
    let results1 = []
    results1.push(tem)
    let html = display(results1)
    document.getElementById("table1").innerHTML = html

    // Same thing I guess for second option
    let tem2 = Array.from(resultss)[1]
    let results2 = []
    results2.push(tem2)
    let html2 = display(results2)
    document.getElementById("table2").innerHTML = html2
}

function display(results) {
    const htmlString = results
    .map((result) => {
        return `
        <tr>
            <td colspan="2" style="width: 635px">Modelname: ${result.Modelname}</td>
        </tr>
        <tr>
            <td>Brand: ${result.Manufacturer}</td>
            <td>Price: €${result.Price}</td>
        </tr>
        <tr>
            <td>CPU: ${result.CPU}</td>
            <td>RAM: ${result.RAM}</td>
        </tr>
        <tr>
            <td>Storage: ${result.Storage}</td>
            <td>GPU: ${result.GPU}</td>
        </tr>
        <tr>
            <td>Screen: ${result.Screen}</td>
            <td>Screensize: ${result.Screensize}"</td>
        </tr>
        <tr>
            <td>Weight: ${result.Weight}kg</td>
            <td>Operating System: ${result.Operatingsystem}</td>
        </tr>
        <br>
    `;
    })
    .join('');

    return htmlString;
}

//
let form = document.getElementById("form")


form.addEventListener("submit", function(e) {
    e.preventDefault();
    let answer = []
    let options = Array.from(document.querySelectorAll(".options"))
    for (option of options) {
        if (option.checked) {
            answer.push(option.value)
        }
    }

    myFunction(answer[0], answer[1], answer[2], answer[3], answer[4], answer[5])

})







