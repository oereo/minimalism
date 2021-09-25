$(document).ready(function() {
    $("#fromLeftid_1").unbind('click').on('click', function() {
        $("#page1").hide();
        $("#page2").show();
        $("#page3").hide();
        $("#page4").hide();
    });
});

$(document).ready(function() {
    $("#fromLeftid_2").unbind('click').on('click', function() {
        $("#page1").hide();
        $("#page2").hide();
        $("#page3").show();
        $("#page4").hide();
    });
});

$(document).ready(function() {
    $("#fromLeftid_3").unbind('click').on('click', function() {
        $("#page1").hide();
        $("#page2").hide();
        $("#page3").hide();
        $("#page4").show();
    });
});

$(document).ready(function() {
    $("#fromLeftsubmit").unbind('click').on('click', function() {
        var numberOfchecked = 0;
        if($("input:checkbox[id='c1']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c2']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c3']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c4']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c5']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c6']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c7']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c8']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c9']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c10']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c11']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c12']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c13']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c14']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c15']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c16']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c17']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c18']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c19']").is(":checked") == true) {
            numberOfchecked++;
        }
        if($("input:checkbox[id='c20']").is(":checked") == true) {
            numberOfchecked++;
        }
     
        $("#numberOfchecked").val(numberOfchecked);
       
    });
});