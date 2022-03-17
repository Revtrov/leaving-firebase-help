//inside the fetch method (function) you put the url to your firebase this 
//should be in the realtime database section under data to the left of the plus button
//add .json to the end of the url
fetch("https://leaving-cert-test-default-rtdb.europe-west1.firebasedatabase.app/.json")
    //use the .then method to turn the response into code called json, 
    //.then runs after your data has been fetched and recieved from firebase
    .then(response => response.json())
    //use another .then to run something after the previous then. this takes the response.json() and names it data
    //you can then manipulate this data for your own use inside the curly brackets
    .then(data => {
        //this turns your data into an array of entries
        //use this only if you have no folder or directory structure in your firebase
        data = Object.entries(data);
        //here we log all the data in your firebase
        console.log(data)
    });
//keep in mind that any code that uses or manipulates the data fetched must be in a .then method