
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
