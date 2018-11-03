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
		return (date[0]+"/"+date[1]+"/"+date[2]);
	}
	
}


//define a fuction to filter data by input datetime
function filterData(date){
	var formatedDate = standardDate(date);
	var resultData = data.filter(ufoData => (ufoData.datetime===formatedDate));
	return resultData;
}



var button = d3.select("#filter-btn");
var filterField = d3.select("#datetime");

//define a null variable to save whatever was inputed
var filterCondition ="";
filterField.on("change",function(){
	var newDate = d3.event.target.value;
	filterCondition =newDate;
})

//when button is clicked, 
button.on("click",function(){
	d3.event.preventDefault();
	//check if anything was inputed in the field
	if (filterCondition !=""){	
		var targetData = filterData(standardDate(filterCondition));
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
			alert("No result or Wrong input. Please try again.")
		}
	}
	else {
		alert("Please input some filter condition.")
	}
	filterField.node().value="";
	

})
