const BASE_URL = 'http://127.0.0.1:8000/';

async function fetchData(endpoint) {
    await fetch(`${BASE_URL}/${endpoint}`)
        .then((resp) => resp.json())
        .then(function(data){
            console.log(data)
        }
        )}

