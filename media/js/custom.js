
$(document).ready(function(){
        $('.fade').css('display','none');
        $('.fade').fadeIn(3500);

        $('a.transition').click(function(event){
            if(event.preventDefault) event.preventDefault();
                linkLocation = this.href;
                $('.fade').fadeOut(2000, redirectPage);
        });

        function redirectPage() {
            window.location = linkLocation;
        }
        });



                                                    
/* function alertas(){                              
      alert("hello");                               
}                                                   
                                                    
                                                    
function fadeinout(){                               
    $('body').css('display','none');                
    $('body').fadeIn(3500);                         
                                                    
    $('a.transition').click(function(event){        
        event.prevenDefault();                      
            linkLocation = this.href;               
            $('body').fadeOut(2000, redirectPage);  
    });                                             
    };                                              
                                                    
                                                    
                                                    
$(document).ready(function(){                       
    if ('                                           
        fadeinout();                                
    }                                               
});                                                 
*/                                                  
