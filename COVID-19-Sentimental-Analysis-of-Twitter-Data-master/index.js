function makeplotSentiment() {
  Plotly.d3.csv("https://raw.githubusercontent.com/gowri-gs/COVID-19-Sentimental-Analysis-of-Twitter-Data/master/COVID-19-Sentimental-Analysis-of-Twitter-Data-master/Python%20codes/docemo.csv",
    function(data){ processDataSentiment(data) } );

};
function processDataSentiment(allRows) {
  // console.log(allRows);
  
  var sadness=[],joy=[],fear=[],disgust=[],anger=[],date=[],pos=[],neg=[],neu=[];

  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    // console.log(row)
    date.push(row['doc']);
    sadness.push(row['sadness%']);
    joy.push(row['joy%']);
    fear.push(row['fear%']);
    disgust.push(row['disgust%']);
    anger.push(row['anger%']);
    neg.push(row['neg%']);
    pos.push(row['pos%']);
    neu.push(row['neu%']);

//     x.push( row['AAPL_x'] );
//     y.push( row['AAPL_y'] );
  }
//   console.log( 'X',x, 'Y',y, 'SD',standard_deviation );
//   makePlotly( x, y, standard_deviation );
     makePlotlySentiment( sadness,joy,fear,disgust,anger,date,pos,neg,neu);
}

function makePlotlySentiment( sadness,joy,fear,disgust,anger,date,pos,neg,neu){
  var plotDiv = document.getElementById("plot");
  var sadness = {
    x: date,
    y: sadness,
    mode: 'lines+markers',
    name:"Sadness"
  };
  var joy = {
    x: date,
    y: joy,
    mode: 'lines+markers',
    name:"Joy"
  };
  var fear = {
    x: date,
    y: fear,
    mode: 'lines+markers',
    name:"Fear"
  };
  var disgust = {
    x: date,
    y: disgust,
    mode: 'lines+markers',
    name:"Disgust"
  };
  var anger = {
    x: date,
    y: anger,
    mode: 'lines+markers',
    name:"Anger"
  };
  var sum1 = pos.reduce((total, num) =>total += parseInt(num));
//   console.log("sum : "+sum1 )
  let positive = sum1 / pos.length;
  
  var sum2 = neu.reduce((total, num) =>total += parseInt(num));
  let neutral = sum2 / neu.length;
//   console.log("sum : "+sum2 )

  var sum3 = neg.reduce((total, num) =>total += parseInt(num));
  let negative = sum3 / neg.length;
//   console.log("sum : "+sum3 )
  
  let colours=[['rgb(0, 204, 0)','rgb(11, 0, 255)','rgb(255, 0, 0)']];
 
  // console.log(pos,positive,neg,negative,neu,neutral)
  var data_pie = [{
    values: [positive,neutral,negative],
    labels: ['Positive', 'Neutral', 'Negative'],
    type: 'pie',
    marker:{
        colors:colours[0]
    }
  }];
  var data_graph=[sadness,joy,fear,disgust,anger];
  var title={title: 'Emotion Graph'};
  Plotly.newPlot('myDiv',data_graph ,title);
  Plotly.newPlot('myDiv_pie',data_pie ,{title:"Sentiment Chart"})
};
  makeplotSentiment();

  function makeplotCategory(){
    Plotly.d3.csv("https://raw.githubusercontent.com/gowri-gs/COVID-19-Sentimental-Analysis-of-Twitter-Data/master/COVID-19-Sentimental-Analysis-of-Twitter-Data-master/Python%20codes/result1.csv",
    function(data){ processDataCategory(data) } );
  }
  function processDataCategory(data){
    console.log(data)
    let label=[], score=[];
    for(let i=0;i<data.length;i++){
      label.push(data[i].cat_label);
      score.push(data[i].cat_score);
    }
    console.log(score,label)
    makePlotlyCategory( score,label);
  }
  
  function makePlotlyCategory(cat_score,cat_label){
    var plotDiv = document.getElementById("plot");
    
    var data_bar = [
      {
        x:cat_label,
        y: cat_score,
        type: 'bar'
      }
    ];
    
    var title={title: 'Category Chart'};
    Plotly.newPlot('myDiv_bar_category',data_bar,title);
  }

  makeplotCategory();

// Calender

// $(function() {
//   $('input[name="daterange"]').daterangepicker({
//     opens: 'left'
//   }, function(start, end, label) {
//     console.log("A new date selection was made: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
//   });
// });

// Open the Modal
function openModal() {
  document.getElementById("myModal").style.display = "block";
}

// Close the Modal
function closeModal() {
  document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}


// Get all users
var url  = "https://api.covid19india.org/data.json";
var xhr  = new XMLHttpRequest()
xhr.open('GET', url, true)
xhr.onload = function () {
	var users = JSON.parse(xhr.responseText);
	if (xhr.readyState == 4 && xhr.status == "200") {
    console.log(users)
		document.getElementById('total_cases').innerHTML=users.cases_time_series[users.cases_time_series.length-1].totalconfirmed;
		document.getElementById('total_deaths').innerHTML=users.cases_time_series[users.cases_time_series.length-1].totaldeceased;
    }
    else {
		console.error(users);
	}
}
xhr.send(null);

function clear(){
  document.getElementById("tweet").innerHTML=" ";
}
