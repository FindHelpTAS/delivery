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

    # Embed Google Places Autocomplete using HTML iframe
    html_code = """
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAftn7kB6TxdRyuN2uSK-c22J0TEcD0mjI&libraries=places"></script>
    <input id="location" type="text" placeholder="Start typing location..." style="width: 100%; padding: 10px; font-size: 16px;">
    
    <script>
        function initAutocomplete() {
            const input = document.getElementById('location');
            const options = {
                componentRestrictions: { country: 'AU' },
                types: ['(regions)']
            };
            const autocomplete = new google.maps.places.Autocomplete(input, options);

            autocomplete.addListener('place_changed', function() {
                const place = autocomplete.getPlace();
                if (place && place.geometry) {
                    const location = place.formatted_address;
                    window.parent.postMessage({ location }, '*');
                }
            });
        }
        google.maps.event.addDomListener(window, 'load', initAutocomplete);
    </script>
    """
    st.components.v1.html(html_code, height=100)

    # Display message when location is received from iframe
    st.write("Once you select a location, it will be processed.")
