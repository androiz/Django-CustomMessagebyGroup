
var groups = null;
$.ajax({
    url:'/get_groups/',
    type:"GET",
    success:function(data){
        groups = data;
        console.log(groups);
        for (elem in data){
            console.log(elem);
            $("#id_"+groups[elem]+"_message").closest(".form-row").hide();
        }
    },
    error: function(){
        console.log("error");
    }
});
jQuery(function($) {
    $( "#id_role" ).change(function() {
        for (elem in groups){
            $("#id_"+groups[elem]+"_message").closest(".form-row").hide();
        }
        var option = $( "#id_role option:selected" ).val();
        $("#id_"+groups[option-1]+"_message").closest(".form-row").show();
    });
});

