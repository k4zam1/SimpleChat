
function get(url){
    fetch(url)
    .then(function(response){
        return response.json;
    })
    .then(function(text))
}