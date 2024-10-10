function setPatient(mrn) {
    fetch(`/set_patient/${mrn}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                if (data.redirect) {
                    window.location.href = data.redirect;
                }
            } else {
                console.error(data.message);
            }
        })
        .catch(error => console.error('Error:', error));
}
