// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody=d3.select("tbody");

//display table before any filter from user
data.forEach(ufo =>{
	var row = tbody.append("tr");
	Object.values(ufo).forEach(value =>{
		var cell = row.append("td");
		cell.text(value);
	})
})


//function to put date input to standard
function standardDate(date){
	var dateList = date.split("/");
	var date=[]
	//for input without 2 "/" in it, return a unexist date
	if (dateList.length != 3){
		return "0/0/0000"
	}
	else{
		//remove initial 0 from month if any
		if (dateList[0].substring(0,1)==="0"){
			date.push(dateList[0].substring(1));
		}
		else {
			date.push(dateList[0]);
		}
		//remove initial 0 from day if any
		if (dateList[1].substring(0,1)==="0"){
			date.push(dateList[1].substring(1));
		}
		else {
			date.push(dateList[1]);
		}
		//make year in format of 20xx
		if (dateList[2].length === 4) {
			date.push(dateList[2]);
		 }
		 else{
		 	date.push("20"+dateList[2])
		 }
		//return date in 'x/x/20xx'
		return (date[0]+"/"+date[1]+"/"+date[2]);
	}
	
}


//define a fuction to filter data with formating the input date
function filterData(arr,date){
	var formatedDate = standardDate(date);
	var resultData = arr.filter(ufoData => (ufoData.datetime===formatedDate));
	return resultData;
}

//define other filter fuction
function filterCity(arr,city){
	var resultData = arr.filter(ufoData => (ufoData.city===city));
	return resultData;
}

function filterState(arr,state){
	var resultData = arr.filter(ufoData => (ufoData.state===state));
	return resultData;
}

function filterCountry(arr,country){
	var resultData = arr.filter(ufoData => (ufoData.country===country));
	return resultData;
}

function filterShape(arr,shape){
	var resultData = arr.filter(ufoData => (ufoData.shape===shape));
	return resultData;
}



var button = d3.select("#filter-btn");
var dateField = d3.select("#datetime");
var cityField = d3.select("#city");
var stateField = d3.select("#state");
var countryField = d3.select("#country");
var shapeField = d3.select("#shape");

//define null variables to save whatever was inputed
var dateCondition ="";
var cityCondition ="";
var stateCondition ="";
var countryCondition ="";
var shapeCondition ="";
dateField.on("change",function(){
	var newDate = d3.event.target.value;
	dateCondition =newDate;
})
cityField.on("change",function(){
	var newCity = d3.event.target.value;
	//lowercase for input
	cityCondition =newCity.toLowerCase();
})
stateField.on("change",function(){
	var newState = d3.event.target.value;
	//lowercase for input
	stateCondition =newState.toLowerCase();
})
countryField.on("change",function(){
	var newCountry = d3.event.target.value;
	//lowercase for input
	countryCondition =newCountry.toLowerCase();
})
shapeField.on("change",function(){
	var newShape = d3.event.target.value;
	//lowercase for input
	shapeCondition =newShape.toLowerCase();
})

//when button is clicked, 
button.on("click",function(){
	d3.event.preventDefault();
	var targetData;
	//check if anything was inputed in at least one field
	if ((dateCondition !="")||(cityCondition !="")||(stateCondition !="")||(countryCondition !="")||(shapeCondition !="")){	
		//if there is at least one filter condition
		//process the each filter if the corresponding field has a input
		if (dateCondition !="") {
			targetData = filterData(data,standardDate(dateCondition));
		}
		else {targetData=data}

		if (cityCondition !=""){
			targetData = filterCity(targetData,cityCondition);
		}

		if (stateCondition !=""){
			targetData = filterState(targetData,stateCondition);
		}

		if (countryCondition !=""){
			targetData = filterCountry(targetData,countryCondition);
		}

		if (shapeCondition !=""){
			targetData = filterShape(targetData,shapeCondition);
		}

		if (targetData.length != 0 ){
			tbody.selectAll("tr").remove();
			targetData.forEach(ufo =>{
				var row = tbody.append("tr");
				Object.values(ufo).forEach(value =>{
					var cell = row.append("td");
					cell.text(value);
				})
			})	
		}
		else {
			tbody.selectAll("tr").remove();
			alert("No result. Please try again.");
		}
	}
	else {
		alert("Please input some filter condition.");
	}
	button.node().value="";
	dateField.node().value="";
	cityField.node().value="";
	stateField.node().value="";
	countryField.node().value="";
	shapeField.node().value="";
	

})
