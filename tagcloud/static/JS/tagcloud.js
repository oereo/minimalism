$(document).ready(function() {
    var now = new Date(); // 전체
    var year = String(now.getFullYear()); // 년도
    var month = String(now.getMonth()+1); // 월
    if(month.length==1) {
        month = "0"+month;
    }
    var date = String(now.getDate()); // 일
    if(date.length==1) {
        month = "0"+date;
    }
    var mergedDate = year+month+date;
    var mergedDateYear = mergedDate.substring(0,4);
    var mergedDateMonthDate = String(parseInt(mergedDate.substring(4,9))*8);
    if(mergedDateMonthDate.length==3) {
        mergedDateMonthDate = String("0")+mergedDateMonthDate;
    }
    var mergedDateMath = mergedDateYear+mergedDateMonthDate;

    var tempDate = String("99990925");
    var tempDateYear = tempDate.substring(0,4);
    var tempDateMonthDate = String(parseInt(tempDate.substring(4,9))*8);
    if(tempDateMonthDate.length==3) {
        tempDateMonthDate = String("0")+tempDateMonthDate;
    }
    var tempDateMath = tempDateYear+tempDateMonthDate;

    var result = 5;

    for(var i = 0; i<$('li').length; ++i) {
        tempDate = String($("#"+i).attr("date"));

        tempDateYear = tempDate.substring(0,4);
        tempDateMonthDate = String(parseInt(tempDate.substring(4,9))*8);
        if(tempDateMonthDate.length==3) {
            tempDateMonthDate = String("0")+tempDateMonthDate;
        }
        tempDateMath = tempDateYear+tempDateMonthDate;

        result = parseInt(mergedDateMath) - parseInt(tempDateMath);

        // if(i==0||i==1) {
        //     alert(mergedDateMath);
        //     alert(tempDateMath);
        //     alert(result);
        // }

        $('#'+i).css("font-size",result*(1/500));
    }


    const inf = document.querySelector(".inf");
    document.addEventListener("mousemove", (e) => {
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        inf.style.left = mouseX + 'px';
        inf.style.top = mouseY + 'px';
    });

    $('li').hover(function(){
        $('.inf').css('opacity',0.7);
    }, function() {
        $('.inf').css('opacity',0);
    })
});

