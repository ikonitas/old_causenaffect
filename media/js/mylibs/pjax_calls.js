direction = "right";
$(document).ready(function(){

  $('.view_bsk, .left_middle li a, .next, .previous, .title a, .archive_year a, .archive_a, .archive_whole a, .title_archive a').live('click', function(e){
    e.preventDefault();
    $('.content').show('slide', { direction: direction});
    var name = $(this).attr("href").match(/\w+/);
    //var name = $(this).attr("href").replace(/\//g, '');
    $('.archive').empty();
    $.post("/archive/", { 'arch': name},
    function(data){
      $.each(data, function(key,value){
        if (key.length == 0){
          return false;
        }
        $('.archive').append('<div class="archive_year"><a href="/' +name+'/'+ key + '/">'+ key + '</a></div><div class="archive_whole"><a href="/'+name+'/archive/">VIEW FULL ARCHIVE</a></div><div class="archive_months"></div>&nbsp;&nbsp;'); 
        for (var i =0; i < value.length; i++) {
          var item = value[i];
          /*$('.archive').append('<a href='+ key +'/' + item +'/'>'' + item + "</a>");
          */
          $('.archive').append('<a class="archive_a" href="/' +name+'/' +key+'/'+item+'/">' + item + '</a> ');
        }
      });
    },"json");

    $.pjax({
            url: (this),
            container: '.content' });
    $('.content').fadeIn('slow', function(){
      mCustomScrollbars();
    });

  });
});

