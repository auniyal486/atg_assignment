//signup and login form
$(document).ready(function(){
    $(".login-form").hide();
    $(".login").css("background", "#F7F7F7");
    $(".login").click(function(){
      $(".signup-form").hide();
      $(".login-form").show();
      $(".signup").css("background", "#F7F7F7");
      $(".login").css("background", "#fff");
    });
    $(".signup").click(function(){
      $(".signup-form").show();
      $(".login-form").hide();
      $(".login").css("background", "#F7F7F7");
      $(".signup").css("background", "#fff");
    });
  });
//validation signup
$(document).ready(function(){
    // Validate Username
    $('#username_check').hide();   
    $('#username').keyup(function () {
        validateUsername();
    });
     
    function validateUsername() {
      let usernameValue = $('#username').val();
      if (usernameValue.length==0) {
        $('#username_check').show();
        $('#username_check').html("**Name must not be empty");
        return false;
      }
      else if(usernameValue.length < 3){
          $('#username_check').show();
          $('#username_check').html("**Length of username must be more than 2");
          return false;
      }
      else {
          $('#username_check').hide();
          return true;
      }
    }
 
    // Validate Email
    $('#emailcheck').hide();
    $('#email').keyup(function () {
      validateEmail();
    });
    function validateEmail(){
      let EmailValue=$('#email').val();
      let regex=/^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
      if(regex.test(EmailValue)){
        $('#emailcheck').hide();
        return true;
      }
      else{
        $('#emailcheck').show();
        $('#emailcheck').html("Your email must be a valid email");
        return false;
      }
    }
     
   // Validate Password
    $('#passcheck').hide();
    $('#password').keyup(function () {
        validatePassword();
    });
    function validatePassword() {
        let passwrdValue =$('#password').val();
        if (passwrdValue.length == 0) {
            $('#passcheck').show();
            $('#passcheck').html("**Password must not be empty");
            return false;
        }
        else if (passwrdValue.length < 5) {
            $('#passcheck').show();
            $('#passcheck').html("**Length of your password must be more than 5");
            return false;
        } 
        else {
            $('#passcheck').hide();
            return true;
        }
    }
         
     
    // signup button
    $('#signup_btn').click(function () {
      if(validateUsername()&&validatePassword()&&validateEmail()){
        return true;
      }
      else{
        return false;
      }
    });
});
//validation login
$(document).ready(function(){
    //validate username
    $('#log_name_check').hide();   
    $('#log_username').keyup(function () {
        validateUsername();
    });
     
    function validateUsername() {
      let usernameValue = $('#log_username').val();
      if (usernameValue.length==0) {
        $('#log_name_check').show();
        $('#log_name_check').html("**Name must not be empty");
        return false;
      }
      else if(usernameValue.length < 3){
          $('#log_name_check').show();
          $('#log_name_check').html("**Length of username must be more than 2");
          return false;
      }
      else {
          $('#log_name_check').hide();
          return true;
      }
    }
    
    // Validate Password
    $('#log_passcheck').hide();
    $('#log_password').keyup(function () {
        validatelogPassword();
    });
    function validatelogPassword() {
        let passwordValue =$('#log_password').val();
        if (passwordValue.length == 0) {
            $('#log_passcheck').show();
            $('#log_passcheck').html("**password must not be empty");
            return false;
        }
        else if (passwordValue.length < 5) {
            $('#log_passcheck').show();
            $('#log_passcheck').html("**length of your password must be more than 5");
            return false;
        } 
        else {
            $('#log_passcheck').hide();
            return true;
        }
    }

    // Submit button
    $('#login_btn').click(function () {
      if(validatelogPassword()&&validatelogEmail()){
        return true;
      }
      else{
        return false;
      }
    }); 
});

//flash_message
$(document).ready(function(){
  $("#flash_message").click(function(){
    var div = document.getElementById('flash_container');
    div.parentNode.removeChild(div);
  });
}); 
//for searching
$(document).ready(function(){
  $("#Searching").on("keyup clear change", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
