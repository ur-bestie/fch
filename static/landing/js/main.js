(function($){$(document).ready(function(){$('.sandwich-btn').on('click',function(){$(this).parent().parent().toggleClass('open');});var openMenuItem=function(item){$(item).toggleClass('open');$(item).siblings().removeClass('open');};$('.menu-link.expand').on('mouseenter',function(e){e.stopPropagation();if($(this).closest('.header').hasClass('open')){return;}
openMenuItem(this);});$('.menu-link.expand').on('mouseleave',function(){if($(this).closest('.header').hasClass('open')){return;}
$('.menu-link.expand').removeClass('open');});$('.menu-link.expand').on('click',function(){openMenuItem(this);});$('.slider .owl-carousel .owl-nav button.owl-next, .slider .owl-carousel .owl-nav button.owl-prev').on('touchend',function(){this.onclick=function fix(){var el=this;var par=el.parentNode;var next=el.nextSibling;par.removeChild(el);setTimeout(function(){par.insertBefore(el,next);},0)};});var $promoVideo=$('#promo-video-link');if($promoVideo.length>0){$promoVideo.magnificPopup({type:'inline',midClick:true});}});})(jQuery);