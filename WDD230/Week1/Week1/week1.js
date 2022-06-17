console.log("connected");
let oLastModif = new Date(document.lastModified);
let days =["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
let d = new Date();
let dayName = days[d.getDay()];
let monthName = months[d.getMonth()];

let fulldate = dayName + ", " + monthName +  " " + d.getDate() + ", " + d.getFullYear();
console.log(fulldate);

document.getElementById("currentDate").innerHTML = fulldate;

let interest = ["placeholder link 1", "placeholder link 2" ];

document.getElementById("list1span").textContent = interest[0];
console.log(interest[0]);
document.getElementById("list2span").textContent = interest[1];
console.log(interest[1]);

console.log(oLastModif);
document.querySelector('.yearUpdated').textContent = oLastModif;
