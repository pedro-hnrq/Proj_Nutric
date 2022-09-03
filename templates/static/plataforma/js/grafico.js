fetch("/grafico_peso/{{paciente.id}}/",{
        method: 'POST',
    }).then(function(result){
        return result.json()
    }).then(function(data_paciente){

        const data = {
            labels: data_paciente['labels'],
            datasets: [{
            label: 'Peso paciente',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(75, 192, 192)',
            data: data_paciente['peso'],
            }]
        };

        const config = {
            type: 'line',
            data: data,
            options: {}
        };

        const myChart = new Chart(
            document.getElementById('myChart'),
            config
        );


    })
