let runAddition = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    fetch(`/sum?num1=${num1}&num2=${num2}`)
        .then(response => response.json())
        .then(result => {
            document.getElementById("system_response").innerHTML = "Result: " + result.data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    
};

let runSubtraction = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    fetch(`/sub?num1=${num1}&num2=${num2}`)
        .then(response => response.json())
        .then(result => {
            document.getElementById("system_response").innerHTML = "Result: " + result.data;
        })
        .catch(error => {
            console.error('Error:', error);
        })
    
};

let runMultiplication = () => {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    // Por POST
    fetch('/mul',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({num1: num1, num2: num2})
    })
        .then(response => response.json())
        .then(result => {
            document.getElementById("system_response").innerHTML = "Result: " + result.data;
        })
        .catch(error => {
            console.error('Error:', error);
        });

    // fetch(`/mul?num1=${num1}&num2=${num2}`)
    //     .then(response => response.json())
    //     .then(result => {
    //         document.getElementById("system_response").innerHTML = "Result: " + result.data;
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //     })

};