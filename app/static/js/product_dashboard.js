 
document.addEventListener('DOMContentLoaded', function () {
    // Add hover effect sound (optional)
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            // You can add hover sound effect here
        });
    });

    // Add click feedback
    cards.forEach(card => {
        card.addEventListener('click', function (e) {
            // Add ripple effect or any other click feedback
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = 'translateY(-5px)';
            }, 100);
        });
    });
});
 


function TogglePopup(event,repos){
    const repo = context[repos]
    event.stopPropagation(); // Prevent event from propagating
    
    console.log(repo)
    const popover = document.getElementById("popover");
    console.log("zindex")
        // Check if githubRepo is a string
        if (typeof repo === 'string') {
        window.open(repo, "_blank");  // Redirect to the URL directly
        return;
    }
    
    // Check if githubRepo is an object (dictionary) with key-value pairs
    if (typeof repo === 'object' && !Array.isArray(repo)) {
        const keys = Object.keys(repo);
        if (keys.length === 1) {
            // If there's only one key-value pair, redirect to the URL
            window.open(repo[keys[0]], "_blank"); 
            return;
        }

            // Dynamically create the <ul> element with links
            popover.innerHTML = ""; // Clear any existing content
            let icon = document.createElement("div").appendChild(document.createElement("i"));
            icon.className = "fa fa-info-circle popoverCrossicon";
            popover.appendChild(icon);
            const ul = document.createElement("ul");
            icon.addEventListener('click', () => {
                popover.style.display = 'none';
            });
            keys.forEach(key => {
                const li = document.createElement("li");
                const a = document.createElement("a");
                if (key == "UserName" || key == "Password"){
                    
                }
                else{
                    a.href = repo[key];
                    a.target = "_blank"; // Open link in a new tab
                    a.textContent = key;
                    li.appendChild(a);
                }
                ul.appendChild(li);
            });
            keys.forEach(key => {
                const li = document.createElement("li");
                let div = document.createElement("div");
                if (key == "UserName" || key == "Password"){
                    div.innerHTML = `<span> ${key} </span> : <span id="${key}">${repo[key]}</span> <button onclick="copyText('${key}')" > Copy ${key} </button> `;
                    li.appendChild(div);
                }
                ul.appendChild(li);
            });
            popover.appendChild(ul); // Append the <ul> to the popover


        // If there are multiple key-value pairs, toggle the popover display
        if (popover.style.display === 'none' || popover.style.display === '') {
            popover.style.display = 'block';  // Show the popover
        } else {
            popover.style.display = 'none';  // Hide the popover
        }
    }
}



// Function to copy text from a div
function copyText(elementId) {
    // Create a temporary textarea element
    const textarea = document.createElement('textarea');
    
    // Get the text from the div
    const textToCopy = document.getElementById(elementId).innerText;
    
    // Set the text to the textarea
    textarea.value = textToCopy;
    
    // Append textarea to the document
    document.body.appendChild(textarea);
    
    // Select the text
    textarea.select();
    
    try {
        // Execute copy command
        document.execCommand('copy');
        // Optional: Show success message
        // alert('Text copied to clipboard!');
    } catch (err) {
        console.error('Failed to copy text:', err);
    } finally {
        // Remove the textarea from the document
        document.body.removeChild(textarea);
    }
}
