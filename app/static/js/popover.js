

function togglePopover(event) {
    event.stopPropagation(); // Prevents the event from propagating to the body
    const popover = document.getElementById('popover');

    // Get the position of the clicked element
    const rect = event.currentTarget.getBoundingClientRect();
    popover.style.top = `${rect.bottom + window.scrollY}px`;
    popover.style.left = `${rect.left + window.scrollX}px`;

    // Toggle the display of the popover
    if (popover.style.display === 'none' || popover.style.display === '') {
        popover.style.display = 'block';
    } else {
        popover.style.display = 'none';
    }
}

// Close the popover when clicking anywhere else
document.addEventListener('click', () => {
    const popover = document.getElementById('popover');
    popover.style.display = 'none';
});
