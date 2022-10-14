function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crust = crustType;
    pizza.sauce = sauceType;
    pizza.cheese = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

function randomPizza(){
    var t1=Math.floor(Math.random() * 11);
    var pizza;
    console.log(t1);
    if (t1===0) {
        pizza = pizzaOven("neapolitan","pesto","aged havarti","pepperoni");
    }
    else if (t1===1){
        pizza = pizzaOven("new haven style","white garlic","goat cheese","sausage");
    }
    else if (t1===2){
        pizza = pizzaOven("double-dough","garilc ranch","cheddar","ham");
    }
    else if (t1===3){
        pizza = pizzaOven("st. louis style","hummus","mozzarella","chicken");
    }
    else if (t1===4){
        pizza = pizzaOven("new york style","buffalo","pecorino-romano","olives");
    }
    else if (t1===5){
        pizza = pizzaOven("chicago deep dish","traditional","ricotta","tomatoes");
    }
    else if (t1===6){
        pizza = pizzaOven("traditional","marinara","gouda","mushroom");
    }
    else if (t1===7){
        pizza = pizzaOven("cracker","alfredo","toma","garlic");
    }
    else if (t1===8){
        pizza = pizzaOven("flat bread crust","bbq","ultimate cheese combo","none");
    }
    else if (t1===9){
        pizza = pizzaOven("thin crust","tapenade","provolone","green pepper");
    }
    else if (t1===10){
        pizza = pizzaOven("stuffed crust","artichoke","gorgonzola","onion");
    }
    return pizza;
    
}
    
var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var pizza3 = pizzaOven("chicago", "tomato sauce", ["gouda", "feta"], ["pepperoni", "ham", "olives"]);
var pizza4 = pizzaOven("traditional", "traditional", ["swiss"], ["anchovies", "lettuce", "pineapple"]);

console.log(pizza1);
console.log(pizza2);
console.log(pizza3);
console.log(pizza4);
console.log("Here is your random pizza:", randomPizza());