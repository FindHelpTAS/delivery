import streamlit as st

# Title for the Streamlit app
st.title("Service Options")

# Checkbox options
outreach = st.checkbox("We come to you (Outreach)")
in_centre = st.checkbox("Visit our Centre")
online = st.checkbox("Online Consultation")

# If the outreach option is selected, display the location input
if outreach:
    st.write("Select your location:")

    # Embed Google Places Autocomplete using HTML iframe with error checking and logging
    html_code = """
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAftn7kB6TxdRyuN2uSK-c22J0TEcD0mjI&libraries=places" async defer></script>
    <input id="location" type="text" placeholder="Start typing location..." style="width: 100%; padding: 10px; font-size: 16px;">

    <script>
        // Function to initialize Google Places Autocomplete with logging and error handling
        function initAutocomplete() {
            try {
                console.log("Initializing Google Places Autocomplete...");
                const input = document.getElementById('location');
                if (!input) throw new Error("Location input field not found");

                const options = {
                    componentRestrictions: { country: 'AU' },
                    types: ['(regions)']
                };
                const autocomplete = new google.maps.places.Autocomplete(input, options);

                // Log if autocomplete has been attached successfully
                console.log("Google Places Autocomplete attached successfully");

                // Event listener for when a place is selected
                autocomplete.addListener('place_changed', function() {
                    try {
                        const place = autocomplete.getPlace();
                        if (!place) throw new Error("Place not found or could not be retrieved");

                        // Log place information for debugging
                        console.log("Place selected:", place);

                        // Extract and log formatted address if available
                        const location = place.formatted_address;
                        if (location) {
                            console.log("Selected location:", location);
                            window.parent.postMessage({ location }, '*');
                        } else {
                            throw new Error("Formatted address not available for selected place");
                        }
                    } catch (innerError) {
                        console.error("Error handling place selection:", innerError);
                    }
                });
            } catch (error) {
                console.error("Error initializing Google Places Autocomplete:", error);
                alert("An error occurred while loading location suggestions. Please check the console for more details.");
            }
        }

        // Load autocomplete when Google API is ready, with error checking
        if (typeof google !== 'undefined' && google.maps && google.maps.places) {
            google.maps.event.addDomListener(window, 'load', initAutocomplete);
        } else {
            console.error("Google Maps JavaScript API not loaded. Please check your API key and internet connection.");
            alert("Failed to load Google Maps API. Please check the console for more details.");
        }
    </script>
    """
    st.components.v1.html(html_code, height=150)

    # Display message to indicate that the location will be processed
    st.write("Once you select a location, it will be processed.")
