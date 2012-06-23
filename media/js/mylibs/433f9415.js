  $('#forgot_password').click(function(){
    $('.register').empty();
    $('.register').append("<form id='registration_form' method='post' action='"+ forget_password +"'> "+ csrf_token +" <input style='margin-left:8px' id='id_email' type='text' name='email' maxlength='30' placeholder='Email Address' /> <input type='submit' value='Sign In' />");
    
  });
  
  $('#nav_register').click(function(e){
    e.preventDefault();
    $('.register').empty();
    $('.register').css('background','url("'+MEDIA_URL+'"img/register_bg.png');
    $('#nav_signin').css('background-position','0px 34px');
    $('#nav_register').css('background-position','153px 34px');
    $('.register').css('background','url("'+MEDIA_URL+'/img/register_bg.png")').append("<form method='post' id='registration_form' action='"+auth_register+"' style='margin-top:6px';>" + csrf_token +" <input style='margin-left:8px' id='id_username' type='text' name='username' maxlength='15' placeholder='USERNAME' /> <input id='id_email' type='text' name='email' maxlength='30' placeholder='EMAIL'/> <input type='password' name='password1' id='id_password1' placeholder='PASSWORD' /> <input type='password' name='password2' id='id_password2' placeholder='CONFIRM PASSWORD' /> <input id='register_button' type='submit' value='Register' /> <input type='hidden' name='next' value='{{ next }}' />");

  }); 
  $('#nav_signin').click(function(e){
    e.preventDefault();
    $('.register').empty();
    $('#nav_signin').css('background-position','0px 0px');
    $('#nav_register').css('background-position','154px 0px');
    $('.register').css('background','url("'+ MEDIA_URL +'/img/sign_in_bg.png")').append("<form id='registration_form' autocomplete='off' method='post' action='"+ url_login +"'> "+ csrf_token +" <input id='id_username' type='text' name='username' maxlength='30' placeholder='USERNAME' /> <input type='password' name='password' id='id_password' placeholder='PASSWORD' /> <br/><br/> <span class='remember_me'>Remember me</span> <input type='checkbox' name='remember' checked='checked' />  <input class='button_signin' type='submit' value='Sign In' /> <input type='hidden' name='next' value='' /> </form> <span class='forgot_wrapper'><a href='#' id='forgot_password'>FORGOT YOUR PASSWORD?</a></span>");

  });
