    

async function getMarvelData() {
    var response = await fetch("http://gateway.marvel.com/v1/public/comics?ts=1&apikey=39709fbc7c5ac46c633597175d0db97c6396ee9e");
    var heroData = await response.json();
    console.log(heroData);
}
    
getMarvelData();