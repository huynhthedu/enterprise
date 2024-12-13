// color-modes.js

// Function to toggle between light and dark modes
function toggleColorMode() {
    const currentMode = document.body.getAttribute('data-bs-theme');

    if (currentMode === 'dark') {
        // Switch to light mode
        document.body.setAttribute('data-bs-theme', 'light');
        localStorage.setItem('color-mode', 'light'); // Save the choice to localStorage
    } else {
        // Switch to dark mode
        document.body.setAttribute('data-bs-theme', 'dark');
        localStorage.setItem('color-mode', 'dark'); // Save the choice to localStorage
    }
}

// Function to set the initial color mode based on the saved preference
function setInitialColorMode() {
    const savedMode = localStorage.getItem('color-mode');
    
    if (savedMode) {
        // Set the saved color mode when the page loads
        document.body.setAttribute('data-bs-theme', savedMode);
    } else {
        // If no preference is saved, default to light mode
        document.body.setAttribute('data-bs-theme', 'light');
    }
}

// Call the function to set the initial color mode when the page loads
document.addEventListener('DOMContentLoaded', setInitialColorMode);

// Add an event listener to the button or element that toggles the color mode
const toggleButton = document.getElementById('color-mode-toggle');
if (toggleButton) {
    toggleButton.addEventListener('click', toggleColorMode);
}
