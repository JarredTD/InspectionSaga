var bool_button = { 
    returnTrue: function() {
        const button = document.getElementById("myButton");
        button.addEventListener('click', function() {
            const xhr = new XMLHttpRequest();
            xhr.open('GET', '/inspection_data');
            xhr.onload = function() {
                if (xhr.status == 200) {
                    console.log(xhr.responseText);
                } else {
                    console.log("Error: " + xhr.status);
                }
            }
            xhr.send();
        });
    }
};