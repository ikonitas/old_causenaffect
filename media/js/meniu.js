$(document).ready(function(){
    var myInterval = false;
    var menu = $(".left_middle");
    $('li', menu).mouseover(function(){
           e = this;
        myInterval = setInterval(function(){
            $(e).effect('highlight',{color: '#6fc7c1'},240);
        },300);

        $(this).mouseout(function(){
            clearInterval(myInterval);
            myInterval = false; 
        });
});
});  
