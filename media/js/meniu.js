$(document).ready(function(){
    var myInterval = false;
    $('li').mouseover(function(){
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
