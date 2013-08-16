$(function() {
// OPACITY OF BUTTON SET TO 0%
$(".roll").css("opacity","1");
$(".textb").css("opacity","0");

 
// ON MOUSE OVER
$(".roll").hover(function(){
	$(this).stop().animate({
		opacity: .2
	}, 
	"slow");

$('.textb').stop().animate({
	opacity: 2
	}, "slow");
},
 
// ON MOUSE OUT
function () {
 
// SET OPACITY BACK TO 50%
$('.textb').stop().animate({
opacity: 0
}, "slow");
$(this).stop().animate({
opacity: 1
}, "slow");
});
});
// $(function() {
// 	$(".textb").css("opacity","0");
// 	$(".textb").hover(function () {
 
// // SET OPACITY TO 70%
// $(this).stop().animate({
// opacity: 0.8
// }, "slow");
// },
 
// // ON MOUSE OUT
// function () {
 
// // SET OPACITY BACK TO 50%
// $(this).stop().animate({
// opacity: 0
// }, "slow");
// });
// });