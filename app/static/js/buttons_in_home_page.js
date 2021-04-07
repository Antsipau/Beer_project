$(document).ready(function() {
//$('.Contacts').click(function (e){
//alert ("You try to push id = button_contacts")
//})

$('#button_register').click(function (e){
    x = $("#frame_login").val()
    if (x.length < 3){
        alert ("Your login is too short")
        e.preventDefault()
    }
})

$('#button_register').click(function (e){
    x = $("#frame_login").val()
    if (x.length < 3){
        alert ("Your login is too short")
        e.preventDefault()
    }
})

//$('#button_about_us').click(function (e){
//    $.post(
//        "page_unknown",
//        {
//            "a": "Here"
//        },
//        function(response){
//            alert(response.message)
//        }
//    );
//})

$('#frame_login').blur(function() {
        $.post(
            "check_login",
        {
            "login": $('#frame_login').val()
        },
        function(response){
            if (response.exist == 1){
                alert("User already exists")
            }
        }
    );



});







});

