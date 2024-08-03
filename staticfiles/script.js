document.getElementById('signupForm').addEventListener('submit', function(event) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        var div =document.getElementById("passnotmatch");
        div.textContent = 'Password does not match';
        event.preventDefault();
    }
});