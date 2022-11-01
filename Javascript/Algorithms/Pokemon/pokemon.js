var pokemon = [
    { "id": 1,   "name": "Bulbasaur",  "types": ["poison", "grass"] },
    { "id": 5,   "name": "Charmeleon", "types": ["fire"] },
    { "id": 9,   "name": "Blastoise",  "types": ["water"] },
    { "id": 12,  "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16,  "name": "Pidgey",     "types": ["normal", "flying"] },
    { "id": 23,  "name": "Ekans",      "types": ["poison"] },
    { "id": 24,  "name": "Arbok",      "types": ["poison"] },
    { "id": 25,  "name": "Pikachu",    "types": ["electric"] },
    { "id": 37,  "name": "Vulpix",     "types": ["fire"] },
    { "id": 52,  "name": "Meowth",     "types": ["normal"] },
    { "id": 63,  "name": "Abra",       "types": ["psychic"] },
    { "id": 67,  "name": "Machamp",    "types": ["fighting"] },
    { "id": 72,  "name": "Tentacool",  "types": ["water", "poison"] },
    { "id": 74,  "name": "Geodude",    "types": ["rock", "ground"] },
    { "id": 87,  "name": "Dewgong",    "types": ["water", "ice"] },
    { "id": 98,  "name": "Krabby",     "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime",   "types": ["psychic"] },
    { "id": 133, "name": "Eevee",      "types": ["normal"] },
    { "id": 144, "name": "Articuno",   "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos",     "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres",    "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair",  "types": ["dragon"] }
];

console.log("Pokémon whose id is evenly divisible by 3: ");
for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].id % 3 == 0) {
        console.log(pokemon[i]);
    }
}

console.log("Pokémon objects that have more than one type: ");
for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types.length > 1) {
        console.log(pokemon[i]);
    }
}

console.log("Pokémon whose only type is 'poison':");
for (var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types == "poison"){
        console.log(pokemon[i].name);
    }
}
console.log("Pokémon whose second type is 'flying':");
for(var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types[1] == "flying") {
        console.log(pokemon[i].name);
    }
}

console.log("Reverse names for all pokémon whose only type is poison:");
for (var i=0; i<pokemon.length; i++) {
    if(pokemon[i].types == "poison"){
        var newName = reverseString(pokemon[i].name);
        console.log(newName);
    }
}

function reverseString(str){
    var newName="";
    for(var i=str.length-1; i>=0; i--){
        newName += str[i];
    }
    return newName;
}