var timeline = {
    backYears: 12,
    years: 0,
    terms: {},
}

function clearYear(){
    $("#timelineform").html("");
    $("#submitButton").val("Please fill out the form to Generate your Timeline").addClass("danger xxlarge large").attr('disabled', true);
    $("#notDone").hide();
    timeline.terms = {}
}

function addNewYear(year){
    console.log(year);
    y = year.toString();
    out = '<h3>'+y+'</h3>';
    out += '<p> Winter <input placeholder="Work or School? (eg.1B)" class="span4" type="text" size="20" name="'+y+'-1">'
    out += 'Spring <input placeholder="Work or School? (eg.Employer)" class="span4" type="text" size="20" name="'+y+'-2">'
    out += 'Fall <input placeholder="Work or School? (eg.1A)" class="span4" type="text" size="20" name="'+y+'-3"></p>';
    console.log(out);
    timeline.years += 1;
    $("#timelineform").append(out);
    
}

$(document).ready(function() {
    // $("#generatorForm").append("jquery magic js loaded ");
    clearYear(); 
    
    // Generate yearButtons
    options = ""
    d = new Date();
    year = d.getFullYear();
    for (i=0;i<timeline.backYears;i++){
        options += '<a href="#" class="btn medium">' + (year-i).toString() + '</a> '
        // options += "<option>" + (year-i).toString() +"</option>";
    }
    $("#yearButtons").html(options);
    
    // Bind yearButtons
    $("#yearButtons a").click(function(){
        $("#yearButtons a").each(function(i,button){
            $(button).addClass("").removeClass('info');
        });
        $(this).addClass("info");
        clearYear(); 
        timeline.startYear = parseInt($(this).html());
        timeline.currentYear = parseInt($(this).html());
        console.log(timeline);
        $("#notDone").show();
        addNewYear(timeline.startYear);
        $("#submitButton").removeClass("danger").val("Submit!").addClass("primary").attr('disabled', false);
        return false;
    });
    
    // add New Year
    $("#addNewYear").click(function(){
        timeline.currentYear += 1;
        addNewYear(timeline.currentYear);
    });
    
    $("#deleteLastYear").click(function(){
        if (timeline.currentYear != timeline.startYear){
            $("#timelineform h3:last").remove();
            $("#timelineform p:last").remove();
            timeline.currentYear -= 1;
        }
    });
    
    $("#submitButton").click(function(){
       return true; 
    });
});