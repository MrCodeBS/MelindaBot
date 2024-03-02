function sendMessage() {
    var user_input = document.getElementById('user-input').value;
    var user_name = "Bhupinder";  // Change the user's name here
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/get_response", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText).response;
            document.getElementById('chat-box').innerHTML += '<div class="user-message">' + user_input + '</div>';
            document.getElementById('chat-box').innerHTML += '<div class="bot-message">' + response + '</div>';
            document.getElementById('user-input').value = '';
        }
    }
    var params = 'user_input=' + user_input + '&user_name=' + user_name;
    xhr.send(params);
}
