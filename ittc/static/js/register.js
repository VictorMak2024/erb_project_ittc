$(document).ready(function () {
  const $loginForm = $("form.login");
  const $loginText = $(".title-text .login");
  const $loginBtn = $("label.login");
  const $registerBtn = $("label.register");
  const $registerLink = $("form .register-link a");

  // Register button click functionality
  $registerBtn.on("click", function () {
    $loginForm.css("margin-left", "-50%");
    $loginText.css("margin-left", "-50%");
  });

  // Login button click functionality
  $loginBtn.on("click", function () {
    $loginForm.css("margin-left", "0%");
    $loginText.css("margin-left", "0%");
  });

  // Register link click functionality
  $registerLink.on("click", function (e) {
    e.preventDefault(); // Prevent default link behavior
    $registerBtn.click(); // Simulate a register button click
  });

  // Automatically activate the register form on page load
  $registerBtn.click(); // Simulate a register button click to set the register view as default
});