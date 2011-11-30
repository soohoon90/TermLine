var timeline = {
    backYears: 10,
    year: {},
}


function addNewYear(year){
    
}

$(document).ready(function() {
    // $("#generatorForm").append("jquery magic js loaded ");
    options = ""
    d = new Date();
    year = d.getFullYear();
    for (i=0;i<timeline.backYears;i++){
        options += '<a href="#" class="btn medium info">' + (year-i).toString() + '</a> '
        // options += "<option>" + (year-i).toString() +"</option>";
    }
    $("#yearButtons").html(options);
    
    $("$yearButtons a").click(function(){
        alert("button "+$(this).html() );
    });
    
    $("#startyear").change(function() {
        // alert();
        $(this).val()
    });
    
    $("#addNewYear").click(function(){
        
    });
    
    $("#submitButton").click(function(){
       return true; 
    });
});