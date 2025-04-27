// Select the elements
const signInButton = document.getElementById('sign-in-button');
const dropdownMenu = document.getElementById('dropdown-menu');

// Add click event to toggle the dropdown
signInButton.addEventListener('click', (e) => {
    e.preventDefault(); // Prevent the default link behavior
    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
});

// Close the dropdown menu if clicked outside
document.addEventListener('click', (e) => {
    if (!signInButton.contains(e.target) && !dropdownMenu.contains(e.target)) {
        dropdownMenu.style.display = 'none';
}
});