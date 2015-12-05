$(function() {
        function inputFocus(i){
            if(i.value==i.defaultValue){ i.value=""; i.style.color="#ffffff"; }
        }
        function inputBlur(i){
            if(i.value==""){ i.value=i.defaultValue; i.style.color="#ffffff"; }
        }

$('#AdvButton').on("click", function(){
    var item = document.getElementById("Advanced");
    console.log(item);
    console.log(item.style.display);
    if($(item).hasClass("hidden")){
        console.log('hide');
        $(item).show('slide', {direction: 'up'});
        $(item).toggleClass("hidden");
    }else{
        console.log('show');
        $(item).hide('slide', {direction: 'up'});
        $(item).toggleClass("hidden");
    }
})    
    
});