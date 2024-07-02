//This program generates JavaScript for the website, displaying a summary of the order form once it's submitted by the user.// Created by: Edgar Alan Emmanuel B. Tiamzon III
// B-1L
// 12-28-23

// Declarations of global variables to be used across functions
var selectappet = "";
var listOfMainDishes = [];
var listOfDesserts = [];
var selectrice = "";
var selectdrink = "";
var cost = 0;
var delivfee = 0;
var total_cost = 0;

var cname = document.getElementById("cname");
var mobilenumber = document.getElementById("mobilenumber");
var nofpeople = document.getElementById("nop");
var emailadd = document.getElementById("emailaddress");
var venueaddress = document.getElementById("venueaddress");
var partyDate = document.getElementById("partydate");
var partyTime = document.getElementById("partytime");

// Function to validate form completion and trigger the alert
function checkFormCompletion() {
    // Check if all fields are filled
    if (!document.getElementById("Tiamzon_ex11").checkValidity()) {
        alert("Please fill out all fields.");
    } else {
        foralert();
    }
}
function summarize() {
    var currentDate = new Date();
    var partyHour = parseInt(partyTime.value.split(":")[0]);
    var partyMinutes = parseInt(partyTime.value.split(":")[1]);

    // Selected Choices Arrays
    listOfMainDishes = [];
    listOfDesserts = [];
    selectappet = "";
    selectrice = "";
    selectdrink = "";

    // Pickupoption
    var pickupOption = document.getElementById("pickup").checked;

    cost = 0;
    delivfee = 0;
    total_cost = 0;

    // Appetizers
    if (document.getElementById("salad").checked) {
        cost += 100;
        selectappet = "Salad";
    }
    else if (document.getElementById("bread w/ dip").checked) {
        cost += 70;
        selectappet = "Bread w/ Dip";
    }
    else if (document.getElementById("tomato_surprise").checked) {
        cost += 120;
        selectappet = "Tomato Surprise";
    }

    else if (document.getElementById("mushroom_bites").checked) {
        cost += 150;
        selectappet = "Mushroom Bites";
    }

    // Main Dishes
    if (document.getElementById("roast_beef").checked) {
        cost += 300;
        listOfMainDishes.push("Roast Beef");
    }
    if (document.getElementById("beef_steak").checked) {
        cost += 270;
        listOfMainDishes.push("Beef Steak");
    }
    if (document.getElementById("pork_spareribs").checked) {
        cost += 240;
        listOfMainDishes.push("Pork Spareribs");
    }
    if (document.getElementById("pork_marbella").checked) {
        cost += 250;
        listOfMainDishes.push("Pork Marbella");
    }
    if (document.getElementById("grilled_chicken").checked) {
        cost += 190;
        listOfMainDishes.push("Grilled Chicken");
    }
    if (document.getElementById("roast_chicken").checked) {
        cost += 190;
        listOfMainDishes.push("Roast Chicken");
    }
    if (document.getElementById("boiled_salmon").checked) {
        cost += 170;
        listOfMainDishes.push("Boiled Salmon");
    }
    if (document.getElementById("grilled_salmon").checked) {
        cost += 180
        listOfMainDishes.push("Grilled Chicken");
    }

    // Desserts
    if (document.getElementById("molten_chocolate").checked) {
        cost += 120;
        listOfDesserts.push("Molten Chocolate Cake");
    }
    if (document.getElementById("red_velvet").checked) {
        cost += 90;
        listOfDesserts.push("Red Velvet Cake");
    }
    if (document.getElementById("lemon_bars").checked) {
        cost += 50;
        listOfDesserts.push("Lemon Bars");
    }
    if (document.getElementById("peanut_butter").checked) {
        cost += 60;
        listOfDesserts.push("Peanut Butter Bars");
    }
    if (document.getElementById("buko_pie").checked) {
        cost += 50;
        listOfDesserts.push("Buko Pie");
    }
    if (document.getElementById("lemon_meringue").checked) {
        cost += 70;
        listOfDesserts.push("Lemon Meringue");
    }

    // Rice
    if (document.getElementById("plain").checked) {
        cost += 30;
        selectrice = "Plain";
    } else if (document.getElementById("garlic").checked) {
        cost += 40;
        selectrice = "Garlic";
    } else if (document.getElementById("bagoong").checked) {
        cost += 35;
        selectrice = "Bagoong";
    }

    // Drinks
    if (document.getElementById("cucumber_lemonade").checked) {
        cost += 60;
        selectdrink = "Cucumber Lemonade";
    } else if (document.getElementById("red_icedtea").checked) {
        cost += 50;
        selectdrink = "Red Iced Tea";
    } else if (document.getElementById("ripemango_juice").checked) {
        cost += 70;
        selectdrink = "Ripe Mango Juice";
    }

    //Avail option
    if (pickupOption) {
        document.getElementById("venueaddress").disabled = true;
        document.getElementById("venueaddress").value = "";
        delivfee = 0;
    }
    else {
        document.getElementById("venueaddress").disabled = false;
        // Calculate delivery fee 
        delivfee = (Math.ceil(nofpeople.value / 50) + 1) * 500;
    }

    // Date Validation
    if (partyDate.valueAsDate <= currentDate) {
        document.querySelector('.invalidate').style.display = 'block';
    }
    else {
        document.querySelector('.invalidate').style.display = 'none';
    }

    // Time validation
    if (partyHour < 6 || partyHour > 18 || partyTime.value === "" || (partyHour === 18 && partyMinutes > 0)) {
        document.querySelector('.invalidtime').style.display = 'block';
    }
    else {
        document.querySelector('.invalidtime').style.display = 'none';
    }


    // Total Cost
    total_cost = (nofpeople.value * cost) + delivfee;

    document.getElementById("cinfo").innerHTML = "<b>Customer Name : </b>" + cname.value + "<br><b>Cell Number : </b>" + mobilenumber.value;
    document.getElementById("nop1").innerHTML = "<b>Number of People : </b>" + nofpeople.value;
    document.getElementById("emadd1").innerHTML = "<b>Email Address : </b>" + emailadd.value;
    document.getElementById("cost").innerHTML = "<b>Cost per meal :  </b> Php " + cost;
    document.getElementById("AZ").innerHTML = "<b>Appetizer : </b>" + selectappet;
    document.getElementById("MD").innerHTML = "<b>Main Dishes : </b>" + listOfMainDishes.join(", ");
    document.getElementById("DS").innerHTML = "<b>Desserts :  </b>"+ listOfDesserts.join(", ");
    document.getElementById("TRS").innerHTML = "<b>Type of Rice : </b>" + selectrice;
    document.getElementById("DR").innerHTML = "<b>Type of Drink : </b>" + selectdrink;
    document.getElementById("DD").innerHTML = "<b>Delivery Details : </b>" + venueaddress.value;
    document.getElementById("DF").innerHTML = "<b>Delivery Fee : </b> Php " + delivfee;
    document.getElementById("PD").innerHTML = "<b>Party Date : </b>" + partyDate.value;
    document.getElementById("PT").innerHTML = "<b>Party Time :  </b>" + partyTime.value;
    document.getElementById("TC").innerHTML = "<b>Total Cost :  </b> Php " + total_cost;


}

// Function to display the alert with collected data
function foralert() {
    // Construct the alert message using the collected data
    var alertMessage =
        ":::::::::::::::::CUSTOMER INFORMATION:::::::::::::::::" + "\n" +
        "Customer Name: " + cname.value + "\n" +
        "Cell Number: " + mobilenumber.value + "\n" +
        "Number of People: " + nofpeople.value + "\n" +
        "Email Address: " + emailadd.value + "\n" +
        ":::::::::::::::::PARTY DETAILS:::::::::::::::::" + "\n" +
        "Appetizer: " + selectappet + "\n" +
        "Main Dishes: " + listOfMainDishes.join(", ") + "\n" +
        "Desserts: " + listOfDesserts.join(", ") + "\n" +
        "Type of Rice: " + selectrice + "\n" +
        "Type of Drink: " + selectdrink + "\n" +
        ":::::::::::::::::DELIVERY DETAILS:::::::::::::::::" + "\n" +
        "Delivery Details: " + venueaddress.value + "\n" +
        "Party Date: " + partyDate.value + "\n" +
        "Party Time:  " + partyTime.value + "\n" +
        ":::::::::::::::::COST:::::::::::::::::" + "\n" +
        "Delivery Fee: Php " + delivfee + "\n" +
        "Cost per meal: Php " + cost + "\n" +
        "Total Cost: Php " + total_cost + "\n";

    alert(alertMessage); // Display the alert with the collected data
}

console.log(document.getElementById('Tiamzon_ex11'));


function formReset() {
    document.getElementById("Tiamzon_ex11").reset();
    summarize();
}

// Event Listeners
document.getElementById("Tiamzon_ex11").addEventListener("submit", function (event) {
    event.preventDefault();
    checkFormCompletion();
});
    
window.onload = summarize;
