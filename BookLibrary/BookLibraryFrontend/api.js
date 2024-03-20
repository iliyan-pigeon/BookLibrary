const BASE_URL = 'https://your-django-api.com';

async function fetchData(endpoint) {
    await fetch(`${BASE_URL}/${endpoint}`)
        .then((resp) => resp.json())
        .then(function(data){
            console.log(data)
        }
        )}
