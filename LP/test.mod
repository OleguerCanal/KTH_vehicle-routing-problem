set CITIES;
var PERSON {i in CITIES, j in CITIES} binary;

maximize HAPPY_PEOPLE: sum {i in CITIES} PERSON[i,i];
