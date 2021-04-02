$(function () {

    var $username = $("#username_input");

    $username.change(function () {
        var username = $username.val().trim();

        if (username.length) {

            //    将用户名发送给服务器进行预校验
            $.getJSON('/axf/checkuser/', {'username': username}, function (data) {

                console.log(data);

                var $username_info = $("#username_info");

                if (data['status'] === 200){
                    $username_info.html("用户名可用").css("color", 'green');
                }else  if(data['status'] ===901){
                    $username_info.html("用户已存在").css('color', 'red');
                }

            })

        }

    })

    var $email = $("#email_input");
    $email.change(function () {
        var email = $email.val().trim();
        if(email.length){
             //    将邮箱发送给服务器进行预校验
            $.getJSON('/axf/checkemail/', {'email':email}, function (data) {
                console.log(data);
                var $email_info = $("#email_info");

                if (data['status'] === 201){
                    $email_info.html("邮箱可用").css("color", 'green');
                }else  if(data['status'] ===902){
                    $email_info.html("邮箱已被注册").css('color', 'red');
                }

            })
        }
    })



    var $password = $("#password_input");
    var $password_confirm = $("#password_confirm_input");

    $password_confirm.change(function () {
    var password = $password.val().trim();
    var password_confirm = $password_confirm.val().trim();


    var $password_confirm_info = $("#password_confirm_info");
    if(password !== password_confirm){

        console.log("确认密码不一致");

        $password_confirm_info.html("确认密码不正确").css("color", 'red');
    }else if(password === password_confirm){
        $password_confirm_info.html("√").css("color", 'green');
    }
    })



})


function check() {
    var $username = $("#username_input");

    var username = $username.val().trim();

    var $password_input = $("#password_input");

    var password_input = $password_input.val().trim();

    var $password_confirm_input = $("#password_confirm_input");

    var password_confirm_input = $password_confirm_input.val().trim();

    var $email = $("#email_input");

    var email = $email.val().trim();

    console.log("++++++++++++++++++++++++++++++++++++++++");

    if (!username){
        return false
    }

    var info_color = $("#username_info").css('color');

    console.log(info_color);

    if (info_color !== 'rgb(0, 128, 0)'){

        return false
    }

    var email_color = $("#email_info").css('color');

    console.log(email_color);

    if (email_color !== 'rgb(0, 128, 0)'){
        return false
    }


    if (password_confirm_input !== password_input){
        return false
    }

    if (!email){
        return false
    }

    return true
}
