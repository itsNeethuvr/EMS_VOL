console.log('App.js is loaded');

document.addEventListener('DOMContentLoaded', () => {
    const volunteerForm = document.getElementById('volunteer-form');

    if (volunteerForm) {  // Ensure the form element exists
        volunteerForm.addEventListener('submit', function(e) {
            e.preventDefault();  // Prevent the default form submission behavior

            // Get values from form inputs
            const nameInput = document.getElementById('name');
            const emailInput = document.getElementById('email');
            const roleInput = document.getElementById('role');
            const shiftStartInput = document.getElementById('shift-start');
            const shiftEndInput = document.getElementById('shift-end');

            // Check if any input is null
            if (!nameInput || !emailInput || !roleInput || !shiftStartInput || !shiftEndInput) {
                console.error('One or more input fields are not found in the DOM.');
                return;  // Exit early if inputs are not found
            }

            // Get values safely after checking
            const name = nameInput.value.trim();
            const email = emailInput.value.trim();
            const role = roleInput.value.trim();
            const shiftStart = shiftStartInput.value;
            const shiftEnd = shiftEndInput.value;

            // Create the data object for the volunteer registration
            const volunteerData = {
                name: name,     // Include name
                email: email,   // Include email
                role: role,
                shift_start: shiftStart,
                shift_end: shiftEnd
            };

            // Log the volunteer data to the console for debugging
            console.log('Volunteer Data:', volunteerData);

            // Send the POST request using axios
            axios.post('http://127.0.0.1:8000/api/volunteers/', volunteerData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(function (response) {
                // This is where you handle a successful response
                console.log('Response Data:', response.data);  // Log the response data
                alert('Volunteer registered successfully!');
                // Optionally reset the form
                volunteerForm.reset();
            })
            .catch(function (error) {
                // Handle error response
                if (error.response) {
                    // The request was made and the server responded with a status code
                    // that falls out of the range of 2xx
                    console.error('Response error:', error.response.data);
                    alert(`Error: ${error.response.data.detail || 'Could not register volunteer'}`);
                } else if (error.request) {
                    // The request was made but no response was received
                    console.error('No response received:', error.request);
                    alert('No response from server. Please try again later.');
                } else {
                    // Something happened in setting up the request that triggered an Error
                    console.error('Error', error.message);
                }
            });
        });
    } else {
        console.error('volunteerForm element not found');
    }
});
